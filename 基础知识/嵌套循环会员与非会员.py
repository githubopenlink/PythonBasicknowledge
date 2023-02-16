answer=input('你是会员吗?y/n')
money=float(input('您购买的金额是:'))
if answer=='y':
    
    if  money>=200:
        print('恭喜您打八折，您的消费金额为:',money*0.8,'元')
    elif money>=100:
        print('恭喜您打九折，您的消费金额为:',money*0.9,'元')
    else:
        print('很遗憾您不打折，您的消费金额为:',money,'元')

else:
    
    if money>=200:
        print('恭喜您打9.5折，您的消费金额为:',money*0.95,'元')
    else:
        print('很遗憾您不打折，您的消费金额为:',money,'元')
