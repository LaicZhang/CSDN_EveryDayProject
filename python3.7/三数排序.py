"""
题目 输入三个整数x,y,z，请把这三个数由小到大输出。

程序分析 练练手就随便找个排序算法实现一下，偷懒就直接调函数。
"""
raw=[]
for i in range(3):
    x=int(input('int%d: '%(i)))
    raw.append(x)
    
for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i]>raw[j]:
            raw[i],raw[j]=raw[j],raw[i]
print(raw)


raw2=[]
for i in range(3):
    x=int(input('int%d: '%(i)))
    raw2.append(x)
print(sorted(raw2))

