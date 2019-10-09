import csv #导入csv模块
from itertools import islice #从itertools导入islice，后边让其默认跳过第一行使用
from time import sleep
from selenium import webdriver
#from moudule import baidumodule

driver = webdriver.Chrome()
driver.get('http://www.topeduol.com.cn')

#unnitest中的setup会首先执行 tearDown在unnitest固定写法setup 中会最后只行
#测试用例可以定义多个，但是必须以test开头
#用例名称不是以test开头不会被执行，多条用例名称一致只会执行一条


