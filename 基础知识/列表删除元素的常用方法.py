#删除元素的常用方法，本质上都是内存的复制移动
a=[100,200,888,300,400]
b=a.pop(2)          #括号内是索引，有返回值
print(a)
print(b)            #返回值赋值给b

a=[100,200,888,300,400]
del a[2]            #括号内是索引，并且没有返回值
print(a)

a=[100,200,888,300,400]
b=a.remove(888)     #括号内是元素，并且没有返回值
print(a)
print(b)            #返回值是空值