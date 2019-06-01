"""
题目 练习函数调用。

程序分析 无。
"""
def hello():
    print('Hello World!')
def helloAgain():
    for i in range(2):
        hello()

if __name__=='__main__':
    helloAgain()
