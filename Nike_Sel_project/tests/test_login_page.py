from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from Nike_Sel_project.Base.Nike_Base import base_nike
from Nike_Sel_project.pages.Welcome_page.login_page import Login_page


login=Login_page()
base=base_nike()

driver=base.Base_start()
login.Click_on_sign_in(driver)
login.insert_email(driver)
login.click_Continue(driver)
driver.implicitly_wait(10)
login.insert_password(driver)
login.click_sign_in_after_inserting_email(driver)
driver.implicitly_wait(10)

base.Base_end(driver)
