from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


class cart_page:

    def click_back_to_menu_button(self,driver):
        back_to_menu=driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[6]/div[2]/button")
        back_to_menu.click()


    def click_send_button(self,driver):
        send_button = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[6]/div[1]/button")
        send_button.click()


    def click_on_first_product_scroll_list(self,driver):
        scroll_list=driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/input")
        scroll_list.click()

    def click_on_second_product_scroll_list(self,driver):
        second_scroll_list=driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div/input")
        second_scroll_list.click()

    def click_on_third_product_scroll_list(self,driver):
        third_scroll_list=driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[1]/div/input")
        third_scroll_list.click()

    def click_on_table_number(self,driver):
        click_table=driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[5]/div[5]/input")
        click_table.click()


    def click_on_coupon(self,driver):
        coupon=driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[5]/div[3]/input")
        coupon.click()



