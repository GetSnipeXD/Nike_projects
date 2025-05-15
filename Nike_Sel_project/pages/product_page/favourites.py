from selenium.webdriver.common.by import By


class add_to_fav:
    def add_to_favourites(self,driver):
        click_on_add_fav=driver.find_element(By.CLASS_NAME,"nds-btn.css-153hayi.ex41m6f0.btn-secondary-dark.btn-lg")
        click_on_add_fav.click()
