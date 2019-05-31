"""
题目 暂停一秒输出。

程序分析 使用 time 模块的 sleep() 函数。
"""
import time
for i in range(4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)
