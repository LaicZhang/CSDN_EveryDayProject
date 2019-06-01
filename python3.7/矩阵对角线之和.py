"""
实例038：矩阵对角线之和
题目 求一个3*3矩阵主对角线元素之和。

程序分析 无。
"""
mat=[[1,2,3],
     [3,4,5],
     [4,5,6]
    ]
res = 0
for i in range(len(mat)):
    res += mat[i][i]
print(res)
