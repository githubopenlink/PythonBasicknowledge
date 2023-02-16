'''
习题集一
习题1：判断是否匹配成功，并输出对应匹配信息
'''

import re
source = "1huhongqiang"
if re.match("hu",source):#if re.match is not None
    print("可以匹配到")
else:
    print ("没有匹配到")

if re.search("hu",source):
    print ("可以匹配到")
else:
    print("没有匹配到")


#习题2： 找出一个字符串中是否有连续的5个数字
print(re.search(r"\d{5}","1234aadd222222").group())


#习题3：出一个字符串中的连续5个数字，要求数字前后必须是非数字
re.search(r'(\D\d{5}\D)|(^\d{5}\D)|(\D\d{5}$)|(^\d{5}$)','12567').group()


#习题4:统计一个文件中单词的数量
with open("d:\\word.txt","r") as file_obj:
    print(len(re.findall(r"(\b[A-Za-z]+\b)",file_obj.read())))

#习题5:把a1b23c4d非字符内容拼成一个字符串
print("".join(re.findall(r"[^A-Za-z]","a1b23c4d")))

#习题6:取最后一个字母
re.findall(r"[A-Za-z]","ab12cd")[-1]
re.search(r"[A-Za-z]$","ab12cd").group()

#习题7:找出一个字符串中的所有数字
pattern = re.compile(r"\d+")
pattern.findall("a1cd33dd99kddd")
pattern = re.compile(r"\d")
pattern.findall("a1cd33dd99kddd")

#习题8:把一个字符串中的所有字母找出并拼成一个字符串
pattern = re.compile(r"[A-Za-z]")
"".join(pattern.findall("a1cd34dsf0dsfkjk"))

#习题9:输出句子中的所有单词
s = "I am a boy! you are a girl!"
pattern = re.compile(r"([A-Za-z]+)")
pattern.findall(s)

'''
习题集二：
1、匹配一行文字中的所有开头的字母内容
'''
import re
s="i love you not because of who you are!"
print(re.findall(r"\b\w",s))

#2、匹配一行文字中的所有开头的数字内容
import re
s="12i love 34you not 56because of 7who 8999!"
print(re.findall(r"\b\d",s))

#3、匹配一行文字中的所有开头的数字内容或数字内容
import re
s="12i love 34you not 56beca11use of 7who 8999!"
print(re.findall(r"\d+",s))

#4、 只匹配包含字母和数字的行
import re
s="because\n12sd 34er 56\ndf e4 54434"
print(re.findall(r"\w+",s,re.M))

#5、写一个正则表达式，使其能同时识别下面所有的字符串：'bat','bit', 'but', 'hat', 'hit', 'hut‘
import re
s="'bat', 'bit', 'but', 'hat', 'hit', 'hut','yat','har','hot'"
print(re.findall(r"..t",s))
print(re.findall(r"[bh][aiu]t",s))

#6、匹配所有合法的python标识符
import re
s="awoeur awier !@# @#4_-asdf3$^&()+?><dfg$\n$"
print(re.findall(r".*",s,re.DOTALL))

#7、提取每行中完整的年月日和时间字段
import re
s="我出生时间为1990-01-01 00:00:00,今天时间为2019-04-20 12:20:00"
for i in s.split(","):
     result=re.search(r"[12][0-9]{3}-([0][1-9]|[1][0-2])-([0-2][0-9]|[3][01]) ([01][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])",i)
     if result:
         print(result.group())
     else:
         continue

#8、将每行中的电子邮件地址替换为你自己的电子邮件地址
# coding:utf-8
import re
s="""
1234867@qq.com
lihuali@sdcion.com
"""
s1="guolingping@sdcion.com"
for i in s.split("\n"):
    result=re.search(r"[\w]+@[\w]+.com",i)
    if result:
        s=s.replace(result.group(),s1)
    else:
        continue
print(s)

#9、匹配\home关键字：
import re
s="123ahjfh\home123\homertuy"
for i in re.findall(r"\\home",s):
    print(i)

 

#10、使用正则提取出字符串中的单词
# coding:utf-8
import re
s="I am a boy, my is 19 year!"
print(" ".join(re.findall(r"\b[a-zA-Z]+\b",s)))

'''
11、使用正则表达式匹配合法的邮件地址：
国际域名格式如下：
域名由各国文字的特定字符集、英文字母、数字及“-”(即连字符或减号)任意组合而成, 但开头及结尾均不能含有“-”，“-”不能连续出现。域名中字母不分大小写。域名最长可达60个字节(包括后缀.com、.net、.org等)。
'''
import re
s="lisi_1234@qq.org"
result=re.match(r"^[\w]([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+[\.][a-z]{2,3}([\.][a-z]{2})?$",s)
if result:
    print(result.group())

#12、提取字符串中合法的超链接地址比如：s = '<a href="http://www.gloryroad.cn">光荣之路官网</a>'要求，给出的正则表达式能兼顾所有链接地址。
import re
s='<a href="http://www.gloryroad.cn">光荣之路官网</a>'
print(re.search(r'\w+://[w]{3}.\w+.\w{2,3}',s).group())

#13、统计文件中单词个数
# coding:utf-8
import re
s="I am a boy, my is 19 year!"
result=re.findall(r"\b[a-zA-Z]+\b",s)
print(result)
print("单词个数为：",len(result))

#14、写一个函数，其中用正则验证密码的强度
import re
"""
密码长度大于或等于8位数
强：字母+数字+特殊字符
中：字母+数字，字母+特殊字符，数字+特殊字符
弱：纯数字，纯字母，纯特殊字符
"""
def checklen(pwd):
    if len(pwd)>=8:
        return True
    else:
        return False

def is_strong_pwd(pwd):
    pattern=re.compile(r"^(?![a-zA-z]+$)(?!\d+$)(?![!@#$%^&*]+$)(?![a-zA-z\d]+$)(?![a-zA-z!@#$%^&*]+$)(?![\d!@#$%^&*]+$)[a-zA-Z\d!@#$%^&*]+$")
    result=pattern.findall(pwd)
    if result:
        return True
    else:
        return False

def is_inter_pwd(pwd):
    pattern=re.compile(r"^(?![a-zA-z]+$)(?!\d+$)(?![!@#$%^&*]+$)[a-zA-Z\d!@#$%^&*]+$")
    result=pattern.findall(pwd)
    if result:
        return True
    else:
        return False

def is_weak_pwd(pwd):
    pattern=re.compile(r"^(?:\d+|[a-zA-Z]+|[!@#$%^&*]+)$")
    result=pattern.findall(pwd)
    if result:
        return True
    else:
        return False

def checkpassword(pwd):
    #判断密码长度是否合法
    lenOK=checklen(pwd)
    #判断是否强：字母+数字+特殊字符
    strongOK=is_strong_pwd(pwd)
    #判断是否中：字母+数字，字母+特殊字符，数字+特殊字符
    interOK=is_inter_pwd(pwd)
    #判断是否弱：纯数字，纯字母，纯特殊字符
    weakOK=is_weak_pwd(pwd)

    print(lenOK)
    print(strongOK)
    print(interOK)
    print(weakOK)
    if lenOK:
        if strongOK:
            print("密码的强度为强的！")
        elif interOK:
            print("密码的强度为中的！")
        elif weakOK:
            print("密码的强度为弱的，建议修改！")
    else:
        print("密码长度不合格！")

checkpassword("Helloworld#123")

#15、匹配ip的正则表达式:
r'^(([1-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}([1-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$'

# coding:utf-8
import re
s='172.16.23.189'
s1='11.2.123.1'
s2='255.255.255.255'
s2='0.0.0.0'
pattern=re.compile(r'^(([1-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}([1-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$')
print(pattern.match(s).group())