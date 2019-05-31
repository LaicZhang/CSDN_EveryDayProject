"""
题目 利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

程序分析 用条件判断即可。
"""
points=int(input('输入分数：'))
if points>=90:
    grade='A'
elif points<60:
    grade='C'
else:
    grade='B'
print(grade)
