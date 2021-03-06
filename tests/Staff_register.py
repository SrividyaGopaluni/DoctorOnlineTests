import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AAF_Test4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_method(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://myomknew.herokuapp.com/")
        signup_dropdown = driver.find_element_by_xpath('/html/body/nav/div/li[2]/a').click()
        staff_signup = driver.find_element_by_xpath('/html/body/nav/div/li[2]/div/a[2]').click()
        time.sleep(0.5)
        register_email_address = driver.find_element_by_id("exampleInputEmail1")
        register_email_address.send_keys("staff108@gmail.com")
        register_email_pwd = driver.find_element_by_id("exampleInputPassword1")
        register_email_pwd.send_keys("maverick1a")
        register_confirm_pwd = driver.find_element_by_id("exampleInputPassword2")
        register_confirm_pwd.send_keys("maverick1a")
        time.sleep(3.0)
        register = driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/button').click()
        time.sleep(3.0)
        try:
            # attempt to find the plus button - if found, logged in
            logout = driver.find_element_by_xpath('//*[@id="navbarText"]/li[2]/a')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
