from time import sleep
from selenium.webdriver.common.by import By
from Sv_burger_project.pages.welcome_page import Test_welcome_page

base = Test_welcome_page()
driver = base.test_nav_to_welcome_page()
sleep(5)
base.test_click_on_SignUp(driver)
sign_up = driver.find_elements(By.CLASS_NAME, "form-control")
sign_up[0].send_keys("Nadav")
sign_up[1].send_keys("Hen")
sign_up[2].send_keys("nadav123") # you must always change email if you want it will work
sign_up[3].send_keys("123456")
sign_up[4].send_keys("123456")
sign_up_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
sign_up_button.click()
sleep(5)
Url = "https://svburger1.co.il/#/SignUp"
assert driver.current_url == Url, "ABORT THE SHIP THE TEST WENT WRONG"
base.test_end_burger(driver)
