"""
题目 将一个整数分解质因数。例如：输入90,打印出90=233*5。

程序分析 根本不需要判断是否是质数，从2开始向数本身遍历，能整除的肯定是最小的质数。
"""
target=int(input('输入一个整数：'))
print(target,'= ',end='')

if target<0:
    target=abs(target)
    print('-1*',end='')

flag=0
if target<=1:
    print(target)
    flag=1


while True:
    if flag:
        break
    for i in range(2,int(target+1)):
        if target%i==0:
            print("%d"%i,end='')
            if target==i:
                flag=1
                break
            print('*',end='')
            target/=i
            break
        
