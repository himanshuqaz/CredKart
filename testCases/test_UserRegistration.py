import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pageObject.User_registrtion_page import Userregisterationclass


# driver = webdriver.Chrome()
# driver.get("https://automation.credence.in/shop")


class Test_registration:

    def test_registration_001(self,setup):
        self.driver=setup
        self.rp=Userregisterationclass(self.driver)
        time.sleep(5)
        self.rp.click_lint_register()
        time.sleep(10)
        self.rp.enter_username("testuser8")
        self.rp.enter_email("test758968@credane.in")
        self.rp.enter_password("test@123")
        self.rp.enter_confirmpassword("test@123")
        self.rp.click_register_button()
        if self.rp.status()== True:
            self.driver.save_screenshot("E:\\pythonautomationrevision\\Automation_credkart\\Screenshot\\test_registration_001_pass.png")
            assert True
        else:
            self.driver.save_screenshot(
                "E:\\pythonautomationrevision\\Automation_credkart\\Screenshot\\test_registration_001_fail.png")
            assert False
        self.driver.close()

    def test_mul(self):
        print(5*20)
