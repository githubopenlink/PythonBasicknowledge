#lambda表达式用来声明匿名函数的
#lambda表达式的语法：lambda 形式参数:表达式

t=lambda a,b,c:a*b*c
print(t)
print(t(2,3,4))


g=[lambda a:a**3,lambda b:b*2,lambda c:c+5]    #列表中放多个lambda表达式
print(g)
print(g[0](2),g[1](2),g[2](3))                 #调用某个参数，赋值参数


def num(a,b,c):
    return a*b*c
print(num(2,3,4))
print(num(3,4,5))

