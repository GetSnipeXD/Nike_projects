from selenium.webdriver.common.by import By


class selecting_shoes_size:
    def select_size_40(self,driver):
        click_on_size_40=driver.find_elements(By.CLASS_NAME,"u-full-width.u-full-height.d-sm-flx.flx-jc-sm-c.flx-ai-sm-c")
        click_on_size_40[2].click()
