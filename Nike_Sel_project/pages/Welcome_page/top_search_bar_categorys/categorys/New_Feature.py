from selenium.webdriver.common.by import By


class New_feature:
    def nav_to_new_feature_page(self,driver):
        click_feature_page=driver.find_element(By.XPATH,"/html/body/div[4]/div/nav/header/div/div/div[2]/nav/ul/li[1]/div/a")
        click_feature_page.click()


