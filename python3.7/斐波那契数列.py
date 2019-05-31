"""
题目 斐波那契数列。

程序分析 斐波那契数列（Fibonacci sequence），从1,1开始，后面每一项等于前面两项之和。图方便就递归实现，图性能就用循环。
"""
# 递归实现
def Fib(n):
    return 1 if n<=2 else Fib(n-1)+Fib(n-2)
print(Fib(int(input())))
    
# 朴素实现
target=int(input())
res=0
a,b=1,1
for i in range(target-1):
    a,b=b,a+b
print(a)

