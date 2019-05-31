"""
题目 求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析 用字符串解决。
"""
a = input('被加数字：')
n = int(input('加几次？：'))
res = 0
for i in range(n):
    res += int(a)
    a += a[0]
print('结果是：',res)
