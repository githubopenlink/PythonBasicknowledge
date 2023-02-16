#while在条件不成立的时候停止，for循环在可迭代的序列被穷尽的时候停止

a=0
b=0
while a<=100:
    b=a+b
    a=a+1
print('0到100的总和是'+':',b)



#九九乘法口诀
for i in range(1,10):
    for j in range(1,10):
           print('{}X{}={}'.format(i,j,i*j))
print('结束')

#九九乘法表制表符2
for i in range(1,10):
    for j in range(1,10):
           print('{}X{}={}'.format(i,j,i*j),end='\t')
    print()      #起到换行的作用 

#九九乘法表制表符3
for i in range(1,10):
    for j in range(1,i+1):
           print('{}X{}={}'.format(i,j,i*j),end='\t')
    print('\n')      #起到换行的作用 




sum_all=0
sum_odd=0              #奇数和
sum_even=0             #偶数和
for x in range(101):   #把序列里面0——100的元素依次赋值给变量x
    sum_all+=x         #累加x
    if x%2==1:         #条件：变量x/2余1 
        sum_odd+=x     #累加x
    else:
        sum_even+=x    #条件不成立时候累加x
print('0——100之间整数和是{}，奇数和是{}，偶数和是{}'.format(sum_all,sum_odd,sum_even))


amouut=100
for year in range(1,9):
    amouut*=1.05**year
    print('year{}:${}'.format(year,int(amouut)))
print('复利计算公式')


while True:
    a=input('请输入一个字符(Q或q时退出):')
    if a=='Q'or a=='q':
        print('循环结束')
        break   #结束的是整个循环，如果有嵌入循环，则结束的是离的最近的循环
    else:
        print(a)
