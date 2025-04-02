from time import sleep
from selenium.webdriver.common.by import By
from Sv_burger_project.pages.welcome_page import Test_welcome_page

base = Test_welcome_page()
driver = base.test_nav_to_welcome_page()
sleep(5)
base.test_click_on_SignIn(driver)
sign_in = driver.find_elements(By.CLASS_NAME, "form-control")
sign_in[0].send_keys("nadav1")
sign_in[1].send_keys("000254")
sign_in_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
sign_in_button.click()
sleep(5)
print("ERROR MESSAGE APPEARS TEST SUCCESSES")
base.test_end_burger(driver)