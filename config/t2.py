# coding:utf-8
from  selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('知乎')
driver.find_element_by_id('su').click()
#链接中的文本定位
driver.find_element_by_link_text('新闻')
driver.fi

xml.xpath("bookstore")表示选取bookstore元素的所有子节点
xml.xpath("/bookstore")表示选取根元素bookstore
xml.xpath("bookstore/book")表示选取bookstores下的所有book元素
xml.xpath("//book")选取所有book子元素，而不管他们在文中的位置
xml.xpath("bookstore/book")选择属于bookstore元素的后代的所有book元素，而不管他们位于bookstore之下的什么位置
xml.xpath("//@lang")选取名为lang的所有属性


使用css定位：
#表示使用ID定位
.表示使用class定位,使用

