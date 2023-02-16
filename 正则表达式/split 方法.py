import re

'''
re.split(pattern, string[, maxsplit=0, flags=0])

pattern	    匹配的正则表达式
string	    要匹配的字符串。
maxsplit	分割次数，maxsplit=1 分割一次，默认为 0，不限制次数。
flags	    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
'''

a=re.split('\W+', 'runoob, runoob, runoob.')
b=re.split('(\W+)', ' runoob, runoob, runoob.') 
c=re.split('\W+', ' runoob, runoob, runoob.', 1) 
d=re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
print(a)
print(b)
print(c)
print(d)