
from time import sleep


from selenium.webdriver.common.by import By


class Login_page :

    def Click_on_sign_in(self,driver):
        click_on_login=driver.find_element(By.PARTIAL_LINK_TEXT,"Sign")
        click_on_login.click()
        sleep(2)

    def insert_email(self,driver):
        insert_Email=driver.find_element(By.ID,"username")
        insert_Email.click()
        insert_Email.send_keys("nadav4433@gmail.com")


    def insert_password(self,driver):
        insert_password =driver.find_element(By.ID,"password")
        insert_password.click()
        insert_password.send_keys("nadav123")


    def click_Continue(self,driver):
        click_Continue=driver.find_element(By.CLASS_NAME,"nds-btn.css-13ply87.btn-primary-dark.btn-md")
        click_Continue.click()

    def click_sign_in_after_inserting_email(self,driver):
        click_sign_in=driver.find_element(By.PARTIAL_LINK_TEXT,"Sign")
        click_sign_in.click()





