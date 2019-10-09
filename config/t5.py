import unittest

class LoginTest(unittest.TestCase):
    @classmethod #修饰 告诉程序是类方法
    def setUpClass(cls):
        print("用例前只执行一次")
    @classmethod
    def tearDownClass(cls):
        print("用例后只执行一次")
    #每个用例前都会执行一次  实例方法 每个用例都会执行
    # def setUp(self):
    #     print("先打开浏览器")
    # def tearDown(self):
    #     print("关闭浏览器")

    def test_01(self):
        #断言一般放到最后一句话，一条失败之后 不会影响第二条 但是第一条会报错 不再往下运行
        self.assertEqual((1+2),3)
        self.assertEqual(0+1,1)
        print("111111111")
        a = "admin"
        b = "admin"
        #判断a 等于 b  不等于： ！==
        self.assertEqual(a,b)
        #判断a 包含于 b   不包含： not in
        #self.assertEqual(a in b)




    def test_02(self):
        self.assertEqual((1 + 10), 11)
        self.assertEqual(0 + 2, 2)
        print("2222222222")


if __name__ == '__main__':
    unittest.main()