import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class AAF_Test7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_method(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://doctoronlineapp.herokuapp.com/")
        #elem = driver.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').click()
        login_dropdown = driver.find_element_by_xpath('/html/body/nav/div/li[1]/a').click()
        patient_login = driver.find_element_by_xpath('/html/body/nav/div/li[1]/div/a[1]').click()
        #time.sleep(0.5)
        #time.sleep(1)
        #elem = driver.find_element_by_xpath('//*[@id="navbarText"]/li[1]/div/a[1]').click
        #time.sleep(0.5)
        elem = driver.find_element_by_id("exampleInputEmail1")
        elem.send_keys("patient@gmail.com")
        elem = driver.find_element_by_id("exampleInputPassword1")
        elem.send_keys("Team@123")
        elem = driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
        elem = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/a').click()





        #elem = driver.find_element_by_xpath('//*[@id="app-layout"]/nav/div/div[1]/p/a[4]').click()
        add_park = driver.find_element_by_xpath('//*[@id="id_doctor"]').click()
        select_doctor_name = Select(driver.find_element_by_id('id_doctor'))
        (select_doctor_name).select_by_visible_text('Manohar Gopaluni')
        #time.sleep(0.5)

        startDate = driver.find_element_by_id('id_date')
        startDate.send_keys('06/06/2020')
       # time.sleep(0.5)

        starttime = driver.find_element_by_xpath('//*[@id="id_time"]').click()
        select_time_slot = Select(driver.find_element_by_id('id_time'))
        (select_time_slot).select_by_visible_text('09:00 – 10:00')

        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Raazi")
        elem = driver.find_element_by_xpath(
            '//*[@id="form-wrapper"]/form/button[1]').click()

        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('/html/body/div/h1')
            assert True
        except NoSuchElementException:
            self.fail("Doctor slot booking Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()