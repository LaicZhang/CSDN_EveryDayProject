"""
题目 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

程序分析 这里用字典的形式直接将对照关系存好。
"""
weekT={'h':'thursday',
       'u':'tuesday'}
weekS={'a':'saturday',
       'u':'sunday'}
week={'t':weekT,
      's':weekS,
      'm':'monday',
      'w':'wensday',
      'f':'friday'}
a = week[str(input('请输入第一位字母:')).lower()]
if a == weekT or a == weekS:
    print(a[str(input('请输入第二位字母:')).lower()])
else:
    print(a)

