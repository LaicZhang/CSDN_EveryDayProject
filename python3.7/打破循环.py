"""
实例046：打破循环
题目 求输入数字的平方，如果平方运算后小于 50 则退出。

程序分析 无
"""
while True:
    try:
        n = float(input('输入一个数字：'))
    except:
        print('输入错误')
        continue
    dn = n**2
    print('其平方为：',dn)
    if dn < 50:
        print('平方小于50，退出')
        break
