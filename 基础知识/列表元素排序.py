#列表排序
#修改原列表，不建新列表的排序
a=[20,30,5,6,1,60,35]
a.sort()    #默认是升序排列
print(a)
a.sort(reverse=True)  #降序排列
print(a)

import random
random.shuffle(a)
print(a)    #随机排序



#建立新列表的排序
#内置函数storted()创建新列表，不对原列表做修改
