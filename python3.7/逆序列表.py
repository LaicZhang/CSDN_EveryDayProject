"""
实例040：逆序列表
题目 将一个数组逆序输出。

程序分析 依次交换位置，或者直接调用reverse方法。
"""
lis = [1,10,100,1000,10000,100000]
for i in range(int(len(lis) / 2)):
    lis[i],lis[len(lis) - 1 - i] = lis[len(lis) - 1 - i],lis[i]
print('第一种实现：')
print(lis)


lis=[1,10,100,1000,10000,100000]
print('第二种实现：')
lis.reverse()
print(lis)

