"""
题目 打印出如下图案（菱形）:

    *
   ***
  *****
 *******
  *****
   ***
    *

程序分析 递归调用即可。
"""
def draw(num):
    a = "*" * (2 * (4 - num) + 1)
    print(a.center(9,' '))
    if num != 1:
        draw(num - 1)
        print(a.center(9,' '))
draw(4)
