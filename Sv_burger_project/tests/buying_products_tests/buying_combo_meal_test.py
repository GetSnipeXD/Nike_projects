from time import sleep
from selenium.webdriver.common.by import By
from Sv_burger_project.pages.cart_page import cart_page
from Sv_burger_project.pages.product_page import product_page
from Sv_burger_project.pages.welcome_page import Test_welcome_page
base_product = product_page
base_cart = cart_page
base = Test_welcome_page()
driver = base.test_nav_to_welcome_page()
sleep(5)
base.test_click_on_SignIn(driver)
sleep(2)
driver = base.test_sign_in(driver)
sleep(5)
combo_meal = driver.find_element(By.CLASS_NAME, "card text-center.mb-3")
combo_meal.click()
reserve_button = driver.find_elements(By.CLASS_NAME, "btn btn-primary")
reserve_button[1].click()
correct_money ="59$"
correct_path= driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/h2[1]")
sleep(5)
assert correct_money == correct_path.text
base.test_end_burger(driver)
