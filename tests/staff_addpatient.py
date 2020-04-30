import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class AAF_Test9(unittest.TestCase):

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
        view_button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[2]/a').click()
        elem = driver.find_element_by_xpath('/html/body/div/div[1]/a/span').click()
        patient_first_name = driver.find_element_by_id('id_first_name').send_keys("Rama")
        patient_last_name = driver.find_element_by_id('id_last_name').send_keys("S")
        patient_phone = driver.find_element_by_id('id_phone').send_keys("1234567890")
        patient_email = driver.find_element_by_id('id_email').send_keys("rama@gmail.com")
        patient_Gender = Select(driver.find_element_by_id('id_gender'))
        (patient_Gender).select_by_visible_text('Male')
        patient_age= driver.find_element_by_id('id_age').send_keys("18")
        patient_address = driver.find_element_by_id('id_address').send_keys("14523 widger street")
        patient_medications = driver.find_element_by_id('id_previous_medications').send_keys("NA")
        dob = driver.find_element_by_id('id_dateofbirth').send_keys("06/10/2008")
        date_created = driver.find_element_by_id('id_date_created').send_keys("2020-09-29")

        submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/form/input[2]').click()
        try:
            added = driver.find_element_by_xpath('/html/body/div/h2')
            assert True
        except NoSuchElementException:
            self.fail("adding failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
