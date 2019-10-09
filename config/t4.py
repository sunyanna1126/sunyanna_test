#coding:utf-8

from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
     #登录成功后的返回值
    def get_login_username(self):
        try:
            d1 = self.driver.find_element_by_class_name("user-name").text
            print(d1)
            return d1
        except:
            return "false"
    def is_alert_exist(self):
        #判断alert是不是在
        time.sleep(2)
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept() #用alert点alert
            return text
        except:
            return "false"



    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://47.105.140.152:8686/")
        print("打开浏览器")
    def test_01(self):
        print("第一条测试用例")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='zentao']").click()
        self.driver.find_element_by_id("account").send_keys("sunyanna")
        self.driver.find_element_by_name("password").send_keys("admin123456")
        #点击登录按钮
        time.sleep(2)
        self.driver.find_element_by_id("submit").click()
        d1 =self.get_login_username()

        #判断是否登录成功
        # time.sleep(3)

        # if d1 =="孙艳娜":
        # print("pass")
        # else :
        # print("登录失败")
        #unnitest  框架自带的断言
        username1 = "孙艳娜"
        self.assertEqual(username1,d1)
    def test_02(self):
        print("第二条测试用例")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='zentao']").click()
        self.driver.find_element_by_id("account").send_keys("sunyanna")
        self.driver.find_element_by_name("password").send_keys("admin")
        #点击登录按钮
        time.sleep(2)
        self.driver.find_element_by_id("submit").click()

        #判断是否登录成功
        # time.sleep(3)
        d2 =self.get_login_username()
        # if d1 =="孙艳娜":
        # print("pass")
        # else :
        # print("登录失败")
        #unnitest  框架自带的断言
        username2 = "孙艳娜"
        self.assertEqual(username2,d2)
    def tearDown(self):
        self.is_alert_exist()
        print("关闭浏览器")
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
