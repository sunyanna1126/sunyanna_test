#coding:utf-8

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.topeduol.com.cn/portal/home")

time.sleep(2)

driver.find_element_by_xpath(".//*[@class='ant-btn' and type='button']").click()
