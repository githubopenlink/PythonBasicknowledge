class Amimai:
    
    def __init__(self,name):
        self.name=name

    def shoe_info(self):
        print('猫的名字叫{}'.format(self.name))

    def move(self):
        print('喵..喵喵....')

class Cat(Amimai):   #子类继承父类的语法，在括号中加入父类名，括号中可以加入多个父类名，按顺序继承

    def __init__(self,name,age):
        super().__init__(name)   #super()调用父类中实例变量
        self.age=age

cat=Cat(' 喵星人',3)
cat.move()
print(cat.shoe_info())