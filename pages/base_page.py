from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from utils.logger import Logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger()
        
    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except NoSuchElementException:
            self.logger.exception(f"Element not found: {by}={value}")
            raise

    def click(self, by, value):
        element = self.find_element(by, value)
        self.highlight_element(element)
        element.click()
        self.logger.info(f"Clicked on element: {by}={value}")

    def enter_text(self, by, value, text):
        element = self.find_element(by, value)
        self.highlight_element(element)
        element.clear()
        element.send_keys(text)
        self.logger.info(f"Entered text '{text}' in element: {by}={value}")

    def read_text(self, by, value):
        element = self.find_element(by, value)
        self.highlight_element(element)
        text = element.text
        self.logger.info(f"Read text '{text}' from element: {by}={value}")
        return text

    def set_dropdown_value_by_index(self, by, value, index):
        element = self.find_element(by, value)
        self.highlight_element(element)
        element.click()
        options = element.find_elements_by_tag_name('option')
        if 0 <= index < len(options):
            options[index].click()
            self.logger.info(f"Set dropdown value by index: {by}={value}, index={index}")
        else:
            self.logger.exception(f"Invalid index for dropdown: {index}")
            raise IndexError(f"Invalid index for dropdown: {index}")

    def set_dropdown_value_by_text(self, by, value, option_text):
        element = self.find_element(by, value)
        self.highlight_element(element)
        element.click()
        options = self.driver.find_elements(By.TAG_NAME, 'option')
        for option in options:
            if option.text == option_text:
                option.click()
                self.logger.info(f"Set dropdown value by text: {by}={value}, text='{option_text}'")
                return
        self.logger.exception(f"Option '{option_text}' not found in dropdown: {by}={value}")
        raise ValueError(f"Option '{option_text}' not found in dropdown: {by}={value}")

    def highlight_element(self, element):
        original_style = element.get_attribute('style')
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "border: 2px solid red;")
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style)
        
    def click_radio_button_by_text(self, name, text):
        locator = (By.XPATH, f"//input[@name='{name}' and @type='radio' and following-sibling::label[text()='{text}']]")
        radio_button = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        radio_button.click()

    def capture_screenshot(self, test_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{test_name}_{timestamp}.png"
        file_path = f"screenshots/{file_name}"
        self.driver.save_screenshot(file_path)
        self.logger.info(f"Screenshot captured: {file_path}")
        return file_path
