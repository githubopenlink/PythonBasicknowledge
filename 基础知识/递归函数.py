#递归函数就是自己调用自己

def text01(n):
    print('测试',n)
    if n==0:                 #设置终止条件，否则会无限制循环
        print('测试结束')
    else:
        text01(n-1)

        print('先出去的栈桢',n)   #打印的是先出去的栈桢
 
text01(5)




#阶乘
def jiecheng(n):
    if n==1:
        return(1)
    else:
        return n*jiecheng(n-1)
print(jiecheng(64))