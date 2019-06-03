"""
实例043：作用域、类的方法与变量
题目 模仿静态变量(static)另一案例。

程序分析 综合实例041和实例042。
"""
class dummy:
    num = 1
    def Num(self):
        print('class dummy num:',self.num)
        print('global num: ',num)
        self.num+=1

n = dummy()
num = 1
for i in range(5):
    num *= 10
    n.Num()
