# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://pc.topeduol.com.cn/")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[1]").send_keys(
            "15201129744")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[2]/following::div[4]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='忘记密码?'])[1]/following::div[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[2]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[2]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[2]").send_keys("123123")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[3]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='忘记密码?'])[1]/following::div[1]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/preceding::div[1]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='全部课程'])[1]/following::span[1]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='本期直播课2019-11-02结课，质保期到2021-05-16'])[1]/following::a[1]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='预计开始时间：2019-06-03 19:00'])[1]/following::span[1]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='预计开始时间：2019-06-03 19:00'])[1]/following::div[1]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='共1节课'])[5]/following::div[1]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='PDF课件'])[3]/following::div[1]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
