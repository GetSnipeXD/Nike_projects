from selenium.webdriver.common.by import By


class nav_to_products:
    def click_on_shoes_product(self,driver):
        click_on_shoes = driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div[5]/div/div[5]/div[2]/main/section/div/div[7]/div/figure/a[2]/div/img")
        click_on_shoes.click()