def return_num():
    return [10,20]  #return可以返回元祖，列表，字典等
def num(b):
    print(b)
value=return_num()
print(value)
num(value)         #第一个函数的返回值可以作为第二个函数的参赛




#传递不定长参数，在参数前面加*  返回是元祖
#包裹位置参数传递
def uner_info(*age):
    print(age)
uner_info('Car',20,30,'hello')

#传递不定长参数，在参数前面加**  返回是字典
#包裹关键字参数传递
def uner_info(**age):
    print(age)
uner_info(name='wang',age=23)




def return_num():
    return 10,20
values=return_num()
print(values[0])    #可以通过索引调用，也可以通过赋值元祖中相同数量变量拆包

v1,v2=return_num()
print(v1)
print(v2)


a,b=1,2  
a,b=b,a   #变量值交换
print(a)
print(id(a))  
print(type(a))   