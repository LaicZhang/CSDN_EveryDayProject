"""
实例041：类的方法与变量
题目 模仿静态变量的用法。

程序分析 构造类，了解类的方法与变量。
"""
def dummy():
    i = 0
    print(i)
    i += 1

class cls:
    i = 0
    def dummy(self):
        print(self.i)
        self.i+=1

a = cls()
for i in range(50):
    dummy()
    a.dummy()
