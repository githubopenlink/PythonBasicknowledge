num_a=int(input('请输入第一个数:'))
num_b=int(input('请输入第二个数:'))

'''
if num_a>=num_b:
    print(num_a,'大于或等于',num_b)
else:
    print(num_a,'小于或等于',num_b)
'''


print('使用表达式进行比较')
print( str(num_a)+'>='+str(num_b) if num_a>=num_b else str(num_a)+'<='+str(num_b ))
#if条件成立，执行if前面表达式，否则执行else后面表达式


'''
print(lambda num_a,num_b:num_a>=num_b or num_a<=num_b)#错误，现在不明白原因，等以后修改
'''
