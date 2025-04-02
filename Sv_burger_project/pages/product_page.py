from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class product_page:

    def click_on_log_out_button(self,driver):
        log_out = driver.find_elements(By.CLASS_NAME, "btn btn-primary")
        log_out[0].click()

    def click_on_reserve_button(self,driver):
        reserve_button = driver.find_elements(By.CLASS_NAME, "btn btn-primary")
        reserve_button[1].click()


    def click_on_combo_meal_button(self,driver):
        combo_meal=driver.find_elements(By.CLASS_NAME,"col-md-8")
        combo_meal[0].click()

    def click_on_kids_meal_button(self,driver):
        combo_meal=driver.find_elements(By.CLASS_NAME,"col-md-8")
        combo_meal[1].click()

    def click_on_burger_button(self,driver):
        combo_meal=driver.find_elements(By.CLASS_NAME,"col-md-8")
        combo_meal[2].click()

    def click_vegan_button(self,driver):
        combo_meal=driver.find_elements(By.CLASS_NAME,"col-md-8")
        combo_meal[3].click()

    def click_on_sides_button(self,driver):
        combo_meal=driver.find_elements(By.CLASS_NAME,"col-md-8")
        combo_meal[4].click()



