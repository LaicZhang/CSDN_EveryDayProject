"""
实例047：函数交换变量
题目 两个变量值用函数互换。

程序分析 无
"""
def exc(a,b):
    return (b,a)
a = 0
b = 10
a,b = exc(a,b)
print(a,b)
