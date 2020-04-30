import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AAF_Test13(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_method(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://doctoronlineapp.herokuapp.com/")
        #elem = driver.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').click()
        login_dropdown = driver.find_element_by_xpath('/html/body/nav/div/li[1]/a').click()
        patient_login = driver.find_element_by_xpath('/html/body/nav/div/li[1]/div/a[2]').click()
        #time.sleep(0.5)
        #time.sleep(1)
        #elem = driver.find_element_by_xpath('//*[@id="navbarText"]/li[1]/div/a[1]').click
        #time.sleep(0.5)
        elem = driver.find_element_by_id("exampleInputEmail1")
        elem.send_keys("staff@gmail.com")
        elem = driver.find_element_by_id("exampleInputPassword1")
        elem.send_keys("Team@123")
        elem = driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
        elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[2]/a').click()


        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('/html/body/div/h2')
            assert True
        except NoSuchElementException:
            self.fail("patient details Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()