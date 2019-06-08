"""
实例068：旋转数列
题目 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

程序分析 无。
"""
from collections import *

li = [1,2,3,4,5,6,7,8,9]
deq = deque(li,maxlen=len(li))
print(li)
deq.rotate(int(input('rotate:')))
print(list(deq))
