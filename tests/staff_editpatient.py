import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

class AAF_Test11(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_method(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://doctoronlineapp.herokuapp.com/")
        login_dropdown = driver.find_element_by_xpath('/html/body/nav/div/li[1]/a').click()
        staff_login = driver.find_element_by_xpath('/html/body/nav/div/li[1]/div/a[2]').click()
        time.sleep(0.5)
        login_email_address = driver.find_element_by_id("exampleInputEmail1")
        login_email_address.send_keys("staff@gmail.com")
        login_email_pwd = driver.find_element_by_id("exampleInputPassword1")
        login_email_pwd.send_keys("Team@123")
        time.sleep(3.0)
        login = driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
        time.sleep(3.0)
        view_mentor_button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[2]/a').click()
        edit_button = driver.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr[1]/td[5]/a').click()
        middle_name = driver.find_element_by_id('id_first_name').send_keys("Test")
        submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/form/input[2]').click()
        try:
            edited_student = driver.find_element_by_xpath('/html/body/div/h2')
            assert True
        except NoSuchElementException:
            self.fail("editing patient failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
