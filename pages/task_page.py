from logging import Logger
import time
from conftest import driver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.start_page import StartPage
from utils.config_reader import ConfigReader
from utils.element import Element
import re


class TaskPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        config = ConfigReader()
        self.timeout = config.get_timeout()
        
    EXPECTED_TEXT = (By.XPATH, "//td[contains(text(), 'Trail')]/code")
    ACTUAL_TEXT = (By.CSS_SELECTOR, "code.wrap")

    def go_to_start_page(self):
        start_page = StartPage(self.driver)
        start_page.open_page()


    def click_task_button(self, task_number):
        locator = f"(//div[@class='four columns'])[{task_number}]"
        self.click(*Element.XPATH_LOCATOR(locator))
        
    def press_button_with_text(self, text):
        locator = f"//button[contains(text(), '{text}')]"
        self.click(*Element.XPATH_LOCATOR(locator))
        
    def t1_step_1(self):
        text = self.read_text(By.XPATH, "(//code)[1]")
        self.press_button_with_text(text)
        
    def t1_step_2(self):
        text = self.read_text(By.XPATH, "(//code)[2]")
        self.press_button_with_text(text)
        
    def t1_step_3(self):
        text = self.read_text(By.XPATH, "(//code)[3]")
        self.press_button_with_text(text)
        
    def check_result(self):
        expected = self.read_text(self.EXPECTED_TEXT[0], self.EXPECTED_TEXT[1])
        actual = self.read_text(self.ACTUAL_TEXT[0], self.ACTUAL_TEXT[1])
        assert actual == expected
        
    def t2_step_1(self):
        text = self.read_text(By.XPATH, "(//code)[1]")
        #we can get the input from 'editbox text, just not now
        #Xpath: //input[contains(@id, translate((//*[contains(., 'editbox')])[last()]/*[last()]/text(), 'T', 't'))]
        self.enter_text(By.CSS_SELECTOR, "input", text)
        
    def t3_step_1(self):
        text = self.read_text(By.XPATH, "(//code)[1]")
        self.set_dropdown_value_by_text(By.CSS_SELECTOR, "div.row select", text)
        
        #we could read literally 'group 0' and find following sibling inputs as well
    def t4_step_1(self):
        text = self.read_text(By.XPATH, "(//code)[1]")
        group = re.search(r'\d', str(self.read_text(By.XPATH, "(//td[contains(., 'In the group')])[1]"))).group()
        self.logger.info(f"text 1: {text}")
        self.logger.info(f"group 1: {group}")
        self.click(By.XPATH, f"//input[@name='s{group}'][following-sibling::text()[contains(., '{text}')]]")
        
    def t4_step_2(self):
        text = self.read_text(By.XPATH, "(//code)[2]")
        group = re.search(r'\d', str(self.read_text(By.XPATH, "(//td[contains(., 'In the group')])[2]"))).group()
        self.logger.info(f"text 2: {text}")
        self.logger.info(f"group 2: {group}")
        self.click(By.XPATH, f"//input[@name='s{group}'][following-sibling::text()[contains(., '{text}')]]")
        
    def t4_step_3(self):
        text = self.read_text(By.XPATH, "(//code)[3]")
        group = re.search(r'\d', str(self.read_text(By.XPATH, "(//td[contains(., 'In the group')])[3]"))).group()
        self.logger.info(f"text 3: {text}")
        self.logger.info(f"group 3: {group}")
        self.click(By.XPATH, f"//input[@name='s{group}'][following-sibling::text()[contains(., '{text}')]]")
        
    def t4_step_4(self):
        text = self.read_text(By.XPATH, "(//code)[4]")
        group = re.search(r'\d', str(self.read_text(By.XPATH, "(//td[contains(., 'In the group')])[4]"))).group()
        self.logger.info(f"text 4: {text}")
        self.logger.info(f"group 4: {group}")
        time.sleep(5)
        self.click(By.XPATH, f"//input[@name='s{group}'][following-sibling::text()[contains(., '{text}')]]")