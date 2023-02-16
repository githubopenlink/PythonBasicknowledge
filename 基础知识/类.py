class Studen:          #类名首字母大写,多个单词采用驼峰原则
    
    #定义构造方法
    def __init__(self,name,score):  #self指当期对象本身,必须位于第一个参数位置  前后各两个下划线
        self.name=name
        self.score=score

    #定义普通方法
    def say_score(self):    #self为第一个参数
        print('{0}的分数是:{1}'.format(self.name,self.score))

s=Studen('李乐浠',100)
s.say_score()





class Dog:
    #构造方法
    def __init__(self,name,age,sex='雌性'):
        self.name=name      #创建和初始化实例变量name
        self.age=age        #创建和初始化实例变量age
        self.sex=sex        #创建和初始化实例变量sex
       
d1=Dog('球球',2,'雄性')
d2=Dog('旺财',1)
d3=Dog(name='大黄',sex='雄性',age=3)

print('我家狗名字叫{}:现在{}了,是{}哦'.format(d1.name,d1.age,d1.sex))
print('我家狗名字叫{}:现在{}了,是{}哦'.format(d2.name,d2.age,d2.sex))
print('我家狗名字叫{}:现在{}了,是{}哦'.format(d3.name,d3.age,d3.sex))






class Dog:
    #构造方法
    def __init__(self,name,age,sex='雌性'):
        self.name=name      #创建和初始化实例变量name
        self.age=age        #创建和初始化实例变量age
        self.sex=sex        #创建和初始化实例变量sex
    
    #实例方法
    def run(self):
        print('{}在跑....'.format(self.name))

    #实例方法
    def speak(self,sound):
        print('{}在叫....,{}'.format(self.name,sound))

dog=Dog('旺财',1)
dog.run()
dog.speak('旺')




class Accout:
    interest_reat=0.0256    # 类变量
    def __init__(self,owner,amout):
        self.owner=owner
        self.amout=amout
    
    @classmethod            # 类方法 需要在前面加装饰器（就是在函数前做一些解释和定义）声明一下
    def interest_by(cls,amt):        #cls是class的简写，调用的是Accout这个类
        return cls.interest_reat*amt

interest=Accout.interest_by(12000.0)
print('计算利息：{0:.4f}'.format(interest))





class Accout:
    __interest_reat=0.0256      #私有化变量就是在变量前面加双下划线
    def __init__(self,owner,amout):
        self.owner=owner        #创建和初始化实例变量ovner
        self.__amout=amout      #创建和初始化私有实例变量amout

    def desc(self):
        print('{0}金额：{1}利率：{2}'.format(self.owner,self.__amout,Accout.__interest_reat))






class Dog:
    #构造方法
    def __init__(self,name,age,sex='雌性'):
        self.name=name     
        self.__age=age  
        self.sex=sex    

    #实例方法
    def run(self):
        print('{}在跑....'.format(self.name))

    #get（取值）方法
    def get_age(self):
        return self.__age  #返回私有实例变量__age

    #set(赋值)方法
    def set_age(self,age):
        self.__age=age     #通过age参数更新私有实例变量__age

dog=Dog('旺财',1)
print(' 狗狗年龄：{}'.format(dog.get_age()))
dog.set_age(3)
print(' 修改后狗狗年龄：{}'.format(dog.get_age()))