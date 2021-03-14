from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path('./env/.env')
load_dotenv(dotenv_path=env_path)


class Account:

    def __init__(self, isPaper: bool = True):
        self.isPaper = isPaper
        self.urls = ('https://paper-api.alpaca.markets/v2/',
                     'https://api.alpaca.markets/v2/')
        self.ids = (os.getenv("PAPERID"), os.getenv("PRODUCTIONID"))
        self.secrets = (os.getenv("PAPERKEY"), os.getenv("PRODUCTIONKEY"))

    def GetURL(self):
        if self.isPaper:
            return self.urls[0]
        return self.urls[1]

    def GetId(self):
        if self.isPaper:
            return self.ids[0]
        return self.ids[1]

    def GetSecret(self):
        if self.isPaper:
            return self.secrets[0]
        return self.secrets[1]
