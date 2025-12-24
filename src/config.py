from dataclasses import dataclass
from configparser import ConfigParser
from pprint import pformat
import os
import logging

# Defining how our config should be, with all the fields, their types and default values.
@dataclass
class Config:
    url_cardapio: str = 'https://sistemas.prefeitura.unicamp.br/apps/cardapio/index.php'
    week_meals_file: str = 'weekly-data.json'
    msgs: str = 'perso_messages.json'
    relationships: str = 'relationships.json'
    config_file: str = 'config.ini'
    chrome_dir: str = 'chromium-chatbot'
    headless: bool = True # Faz com que o chrome rode sem interface grafica. Usado para rodar no server
    group_name: str = ''
    debug:bool = False

    def load(self):
        config = ConfigParser()
        if not os.path.exists(self.config_file):
            self.save()
            return

        config.read(self.config_file)
            
        if "config" in config:
            c = config["config"]
            self.url_cardapio = c.get("url_cardapio", self.url_cardapio)
            self.week_meals_file = c.get("week_meals_file", self.week_meals_file)
            self.msgs = c.get("msgs", self.msgs)
            self.relationships = c.get("relationships", self.relationships)
            self.chrome_dir = c.get("chrome_dir", self.chrome_dir)
            self.headless = c.getboolean("headless", self.headless)
            self.group_name = c.get("group_name", self.group_name)
            self.debug = c.getboolean("debug", self.debug)
        return

    def save(self):
        config = ConfigParser()
        config["config"] = {
                "url_cardapio": self.url_cardapio,
                "week_meals_file": self.week_meals_file,
                "config_file": self.config_file,
                "msgs": self.msgs,
                "relationships": self.relationships,
                "chrome_dir": self.chrome_dir,
                "headless": self.headless,
                "group_name": self.group_name,
                "debug": self.debug
                }
        with open(self.config_file, "w") as file:
            config.write(file)



# Loading the config and making it acessible as variable
config = Config()
config.load()

# Configuring logs
logger = logging.getLogger(__name__)
loglevel = logging.INFO

if config.debug:
    loglevel = logging.DEBUG

logging.basicConfig(level=loglevel,
                    format="%(asctime)s [%(levelname)s] - %(message)s"
                    )

logger.debug("Config file loaded")
logger.debug(f"Config fields: {pformat(config)}")
# Making sure we got the group name and its not empty

if not config.group_name.strip():
    logger.error("Group name not found in config file. Exiting.")
    config.save()
    exit()
