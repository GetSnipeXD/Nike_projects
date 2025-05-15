from selenium.webdriver.common.by import By


class add_to_bag:
    def click_add_to_bag(self,driver):
        click_add_to_bag=driver.find_element(By.CLASS_NAME,"nds-btn.mb3-sm.css-dnr0el.btn-primary-dark.btn-lg")
        click_add_to_bag.click()