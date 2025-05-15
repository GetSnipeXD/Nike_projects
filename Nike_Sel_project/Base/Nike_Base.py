from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class base_nike:

    def Base_start(self):
        print("Test start")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.nike.com/il/")
        driver.maximize_window()
        return driver

    def Base_end(self,driver):
        sleep(2)
        driver.quit()
        print("Test end")
