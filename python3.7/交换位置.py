"""
实例067：交换位置
题目 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

程序分析 无。
"""
li = [3,2,5,7,8,1,5]

li[-1],li[li.index(min(li))] = li[li.index(min(li))],li[-1]

m = li[0]
ind = li.index(max(li))
li[0] = li[ind]
li[ind] = m

print(li)
