import configparser
import os


class ConfigReader:
    def __init__(self):
        config_path = os.path.join(os.getcwd(), 'config', 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_timeout(self):
        return int(self.config.get('Settings', 'timeout'))

    def get_browser(self):
        return self.config.get('Settings', 'browser')

    def get_start_page_url(self):
        return self.config.get('Settings', 'start_page_url')
