import re

'''
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表

re.findall(pattern, string, flags=0)
pattern.findall(string[, pos[, endpos]])

pattern 匹配模式。
string 待匹配的字符串。
pos 可选参数，指定字符串的起始位置，默认为 0。
endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
'''

result1 = re.findall(r'\d+','runoob 123 google 456')
 
pattern = re.compile(r'\d+')   # 查找数字
result2 = pattern.findall('runoob 123 google 456')
result3 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2)
print(result3)

result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)

'''
re.finditer(pattern, string, flags=0)
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
'''

it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group() )