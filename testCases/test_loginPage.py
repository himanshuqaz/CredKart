from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageObject.UserLoginPage import UserLoginClass
from pageObject.User_registrtion_page import Userregisterationclass


class Test_Login:

    def test_login_002(self, setup):
        self.driver = setup

        self.lp = UserLoginClass(self.driver)
        self.lp.Click_LinkLogin()

        self.lp.Enter_Email("test@credence.in")

        self.lp.Enter_Password("test@123")

        self.lp.Click_Login_Button()
        self.rp = Userregisterationclass(self.driver)
        if self.rp.status() == True:
            self.driver.save_screenshot(
                "E:\\pythonautomationrevision\\Automation_credkart\\Screenshot\\test_login_002_pass.png")
            assert True
        else:
            self.driver.save_screenshot(
                "E:\\pythonautomationrevision\\Automation_credkart\\Screenshot\\test_login_002_fail.png")
            assert False
        self.driver.close()