from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


class Test_welcome_page :

    def test_nav_to_welcome_page(self):
        print("Test start")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://svburger1.co.il/#/HomePage")
        driver.maximize_window()
        return driver

    def test_end_burger(self,driver):
        sleep(5)
        driver.quit()
        print("Test end")

    def test_click_on_SignIn(self, driver):
        sign_in_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
        sign_in_button.click()

    def test_click_on_SignUp(self,driver):
        all_elements = driver.find_elements(By.CLASS_NAME, "btn.btn-primary")
        all_elements[1].click()

    def test_sign_in(self,driver):
        sign_in = driver.find_elements(By.CLASS_NAME, "form-control")
        sign_in[0].send_keys("nadav152@gmail.com")
        sign_in[1].send_keys("123456")
        sign_in_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
        sign_in_button.click()


