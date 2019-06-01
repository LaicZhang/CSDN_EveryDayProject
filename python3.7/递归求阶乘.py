"""
题目 利用递归方法求5!。

程序分析 递归调用即可。
"""
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1
print(factorial(5))
