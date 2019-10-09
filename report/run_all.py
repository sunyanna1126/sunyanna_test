import unittest
from common import HTMLTestRunner

#用例的路径
casePath = "E:\E\selemiumTest1\config"
rule = "t*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)

print(discover)

reportPath = "E:\E\selemiumTest1\\report\\"+"resault.html"
fp = open(reportPath,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="报告的名称",description="描述你的报告是干什么用的")
runner.run(discover)