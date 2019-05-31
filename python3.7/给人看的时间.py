"""
题目 暂停一秒输出，并格式化当前时间。

程序分析 同009.
"""
import time

for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)
