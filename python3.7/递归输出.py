"""
题目 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

程序分析 递归真是蠢方法。
"""
def rec(string):
    if len(string) != 1:
        rec(string[1:])
    print(string[0],end='')

rec(input('string here:'))
