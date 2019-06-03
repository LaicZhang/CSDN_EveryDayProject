"""
实例049：lambda
题目 使用lambda来创建匿名函数。

程序分析 无
"""
Max = lambda x,y:x * (x >= y) + y * (y > x)
Min = lambda x,y:x * (x <= y) + y * (y < x)

a = int(input('1:'))
b = int(input('2:'))

print(Max(a,b))
print(Min(a,b))
