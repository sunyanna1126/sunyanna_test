
#类和 方法s
class Gou(object):
    #类初始化  调用类的自动运行初始化  可在init中设置全局变量
    def __init__(self):
        self.age = 18
        print("本狗狗，今年18,貌美如花")
    def chigutou(self,aaa):
        print("111%s"%aaa)

    def chigutou1(self):
        d = "aaa"
        print("吃屎")

if __name__ == '__main__':
    g1 = Gou()
    g1.chigutou(222)


