"""
实例036：算素数
题目 求100之内的素数。

程序分析 用else执行for循环的奖励代码（如果for是正常完结，非break）。
"""
lo = int(input('下限：'))
hi = int(input('上限：'))
for i in range(lo,hi + 1):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i)
