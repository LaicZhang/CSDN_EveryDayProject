"""
题目 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

程序分析 无
"""
high = 200.
total = 100
for i in range(10):
    high /= 2
    total += high
    print(high / 2)
    
print('总长：',total)
