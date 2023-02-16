 #多个子类继承父类，并重写父类方法，重写父类方法时是覆盖父类方法，子类创建的对象之间就是多态的

class Animaal:              
    def speak(self):
        print('动物')

class Dog(Animaal):
    def speak(self):
        print('狗')

class Cat(Animaal):
    def speak(self):
        print('猫')

an1=Dog()
an2=Cat()
an1.speak()
an2.speak()