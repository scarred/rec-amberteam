from selenium.webdriver.common.by import By


class Element:
    @staticmethod
    def XPATH_LOCATOR(locator):
        return By.XPATH, locator
