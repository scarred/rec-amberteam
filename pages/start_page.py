from utils.config_reader import ConfigReader
from .base_page import BasePage
from selenium.webdriver.common.by import By


class StartPage(BasePage):
    #URL = ConfigReader().get_start_page_url()
    url = "https://antycaptcha.amberteam.pl/"

    def __init__(self, driver):
        super().__init__(driver)
        self.code_em_locator = (By.CSS_SELECTOR, "code em")
        self.driver = driver
    
    def open_page(self):
        self.logger.log(1,self.url)
        self.driver.get(self.url)
