from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class Userregisterationclass :
    click_linkregister_linkText = (By.LINK_TEXT,"Register")
    Text_username_ID = (By.ID,"name")
    Text_email_NAME = (By.NAME,"email")
    Text_password_ID = (By.ID,"password")
    text_confirmpassword_ID = (By.ID,"password-confirm")
    Click_register_classname = (By.CLASS_NAME,"btn")
    status_text_xpath = (By.XPATH,"//h2[normalize-space()='CredKart']")

    def __init__(self,driver):
        self.driver=driver

    def click_lint_register(self):
        self.driver.find_element(*Userregisterationclass.click_linkregister_linkText).click()

    def enter_username(self,username):
        self.driver.find_element(*Userregisterationclass.Text_username_ID).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*Userregisterationclass.Text_password_ID).send_keys(password)

    def enter_confirmpassword(self,password):
        self.driver.find_element(*Userregisterationclass.text_confirmpassword_ID).send_keys(password)

    def enter_email(self,email):
        self.driver.find_element(*Userregisterationclass.Text_email_NAME).send_keys(email)

    def click_register_button(self):
        self.driver.find_element(*Userregisterationclass.Click_register_classname).click()

    def status(self):
        try:
            self.driver.find_element(*Userregisterationclass.status_text_xpath)
            return True
        except NoSuchElementException:
            return False