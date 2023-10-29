"""
    对象跟对象之间的关系
        1.交互关系（比如攻击）
		2.依赖关系(附属)
        3.关联关系（比如亲友、员工与老板 => 纽带、契约）
        4.组合关系（比如器官、大脑、心脏, 比聚合还要紧密, 一个坏就全部坏, 组件本身不能独立运行, 需要组合在身体(宿主）上）
        5.聚合关系（比如电脑跟零部件, 一个坏没事可以安装到另一处身上）
		6.继承关系（比如父子）
  

	面向对象的三大特征
		继承、封装、多态
"""



print("交互关系 ——————————————————————")



"""交互关系:"""
class Monster:
    role = "monster"
    
    def __init__(self, name, breed, attackLev):  # 姓名, 种类, 攻击力
        self.name = name
        self.breed = breed
        self.attackLev = attackLev # 🔥 攻击力
        self.lifeValue = 100 #生命值固定

    def bite(self, person):
        person.lifeValue -= self.attackLev  # 🔥扣除攻击人后, 人的生命值
        print(f"攻击了 {person.name}, {person.name} 扣除 {self.attackLev} 点生命值, 生命值剩余: {person.lifeValue}")
  
  
class Person:
    role = "humen"
    
    def __init__(self, name, sex, attackLev):
        self.name = name
        self.sex = sex
        self.attackLev = attackLev
        self.lifeValue = 200  # 生命值固定
        
    def attack(self, monster):
        monster.lifeValue -= self.attackLev
        print(f"攻击了 {monster.name}, {monster.name} 扣除 {self.attackLev} 点生命值, 生命值剩余: {monster.lifeValue}")
  
  
monster1 = Monster("吉米", "小怪", 10)
person1 = Person("小明", "男", 20)
monster1.bite(person1)
person1.attack(monster1)
monster1.bite(person1)
person1.attack(monster1)



print("依赖关系 ——————————————————————")



"""依赖关系:"""
class Animals:
    def __init__(self, name: str, age: int, master: object, **kwds: any):
        self.name = name
        self.age = age
        self.master = master # 🔥应该传进来对象
        self.sayHey() # 🔥实例话后默认会调用自己的实例方法!
        # 👇检查 master 参数是否是对象
        if not isinstance(master, object):
            raise TypeError("master 参数必须是一个对象")
        
    def sayHey(self):
        print(f"👋 {self.master.name} 你好~ 我是 {self.name}!") # 🔥这里产生依赖关系, 需要有 Person 才能执行这个方法!
        
        
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def walk_dog(self, catObj: object):
        print(f"{self.name} 正在溜 {catObj.name}")

   
superMan = Person2("Jimmy", "27") # 🔥要先实例化 人 才能实例化 Animals
cuteAnimals =  Animals("嘟嘟", 2, superMan)




print("关联关系 ——————————————————————")




"""关联关系:"""
class Person3:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.partner = None # 初始化第一个人的时候没法填
        
    def set_partner(self, person: object): # 🚀🚀 双向绑定写法一: 内部一个方法
        self.partner = person
        person.partner = self
        
    def __str__(self): # 🔥🔥使用此方法可以让别人在【打印对象的实例】时候可以看到实例的全部属性, 而不是看到内存地址 <__main__.Person3 object at 0x1050c5cd0> <__main__.Person3 object at 0x1050c5c90> !
        return f"Name: {self.name}, Age: {self.age}"
        
        
# p1 = Person3("Kim", 24)
# p2 = Person3("Annie", 29)
# p1.set_partner(p2)
# p2.set_partner(p1)

# print(f"p1 的 partner 是: {p1.partner}, p2 的 partner 是: {p2.partner}")




# 🚀🚀 双向绑定写法二, 抽象出一个结婚的方法
class RelationShip:
    def __init__(self):
        self.couples = []
        
    def make_couple(self, person1: object, person2: object):
        if (person1.partner is not None or person2.partner is not None): #🔥如果其中一人有 partner就打印以下
            print("❌ 其中一人已经有 partner 了")
        else:
            person1.set_partner(person2)
            person2.set_partner(person1)
            self.couples.append((person1, person2))
    
    
p1 = Person3("Kim", 24)
p2 = Person3("Annie", 29)
relationship = RelationShip()
relationship.make_couple(p1, p2)
print(f"p1 的 partner 是: {p1.partner}, p2 的 partner 是: {p2.partner}")




print("组合关系 ——————————————————————")




"""组合关系(人和武器是一个组合):"""
class Monster2:
    role = "monster"
    
    def __init__(self, name: str, attackLev: int):  # 姓名, 种类, 攻击力
        self.name = name
        self.attackLev = attackLev # 🔥 攻击力
        self.lifeValue = 100 #生命值固定

    def bite(self, person):
        person.lifeValue -= self.attackLev  # 🔥扣除攻击人后, 人的生命值
        print(f"攻击了 {person.name}, {person.name} 扣除 {self.attackLev} 点生命值, 生命值剩余: {person.lifeValue}")
    
    
        
class Weapon: # ✋🏻 定义各种武器, 不用实例化（不能独立运行）
	def gun(self, aim: object):  # 👈 aim 为目标攻击对象
		self.attackLev = 40  # 🔥 攻击力 40
		aim.lifeValue -= self.attackLev  # 🔥扣除被攻击对象 40 的血量
		self.print_log(aim)
  
	def knife(self, aim: object):  # 👈 aim 为目标攻击对象
			self.attackLev = 20  # 🔥 攻击力 40
			aim.lifeValue -= self.attackLev  # 🔥扣除被攻击对象 40 的血量
			self.print_log(aim)

	def print_log(self, aim):
		print(f"{aim.name} 被攻击了, 血量扣除{self.attackLev}, {aim.name} 的血量剩余 {aim.lifeValue} ")
        
     
        
class Person2:
    role = "humen"
    
    def __init__(self, name: str):
        self.name = name
        self.weapon = Weapon() # 🔥🔥【装载武器!】直接实例化 Weapon, 依附于 person 来实例化！
        self.lifeValue = 200  # 生命值固定
        
    def attack(self, monster):
        monster.lifeValue -= self.attackLev
        print(f"攻击了 {monster.name}, {monster.name} 扣除 {self.attackLev} 点生命值, 生命值剩余: {monster.lifeValue}")
        


sueprMonster = Monster2("小怪", 5)
superPerson = Person2("Kim")

sueprMonster.bite(superPerson) # 怪物咬了人一口
superPerson.weapon.gun(sueprMonster) # 人使用武器攻击怪物





print("继承 ————————————————————————————————————————————————————————————————————————————————————————")
print("重写父类(单继承) ——————————————————————")



"""重写父类(在父类基础上进行补充):"""
class Father:
	a_type = "父类"
	
	def __init__(self, name: str, money: int = 100): # 初始家产为 100, 让子类继承
		self.name = name
		self.money = money
		
	def run1(self, speed):
		print(f"跑步速度: {speed}")
  
  
  
class Child(Father):
    a_type = "子类"
    
    def __init__(self, name: str, money: int = None, hobbit = None): # 【🔥子类没有构造函数的话, 会调用父类的构造函数, 有的话则会执行子类的构造函数！】 hobbit 为子类单独定义的属性, hobbit 为可选参数, 默认为 None
        super().__init__(money) # 使用 super() 调用父类的 __init__ 的初始化函数,  money 则继承父类的初始值（__init__)
        # 让子类的 money 继承自父类
        # Father.__init__(self, name, money)
        self.name = name # 名字来自子类
        self.hobbit = hobbit # 兴趣也是子类的
    
    def run(self, speed):
        super().run1(speed) # 【🔥执行父类的跑步方法也是 super().XXX !】, 父类会打印 speed 的, 具体的 speed 则由子类传入
        


p3 = Father("SuperAnnie", 9999)
p31 = Child("Annie") # 子类的 money 继承自父类的初始化家产
p31.run(20)
print(p31.money)



print("重写父类(多继承) ——————————————————————")

class AnimalsBase:
	def __init__(self, id = 3):
		self.id = id
	
	def run(self, speed = 200):
		print(f"动物祖先的跑步速度: {speed}")
  
	def fly(self, speed = 1200):
		print(f"动物祖先的飞行速度: {speed}")
  
  
class PersonBase:
	def __init__(self, name = "始祖"):
		self.name = name
		
	def fly(self, speed = 900):
		print(f"人类始祖的飞行速度: {speed}")
  



class Animals2(AnimalsBase):
	def __init__(self, id = 7):
		self.id = id
	
	def run(self, speed = 100):
		print(f"跑步速度: {speed}")
  
		
	
class Persons4(PersonBase):
	def __init__(self, name = "小明"):
		self.name = name
  
	def run(self, speed = 30):
		print(f"跑步速度: {speed}")
		
	def drive(self, speed):
		print(f"驾驶速度: {speed}")
  
	def fly(self, speed = 299):
		print(f"普通人类的飞行速度: {speed}")



class Students(Animals2, Persons4): # 多继承, 如果有相同的属性或方法则优先继承第一个父类
    def __init__(self, name = None, id = None):
        Animals2.__init__(self, id)
        Persons4.__init__(self, name)
        
    def study(self, subject):
        print(f"学习了 {subject}")
        

superStudent = Students("007")
print(superStudent.id)
superStudent.run() # 🚀 调用继承自父类的方法（优先调用左侧 Animals2 的 run 方法）
superStudent.fly()  # 🔥 深度优先而非广度优先, 优先调用左侧 Animals2 , 没有的话就再向上找 AnimalsBase 的 fly 方法! 【🔥有个坑, 如果两个始祖类又继承自同一个类, 那么就会变成广度优先!! -> C3 算法】
print(Students.mro())#打印继承顺序





print("封装 ————————————————————————————————————————————————————————————————————————————————————————")
"""
	封装可以防止外部随意修改类身上的数据, 保证【属性】或【方法】的安全性、隐私性
	仅在实例的内部可以访问这些数据
	或者在外部通过接口进行访问
 
	使用私有属性来定义实例变量、成员变量
 """

class Hotel:
	def __init__(self, room):
		self.room = room
		self.__income = 10000  # 🚀增加两个 __ 就会变为私有属性 !! 在类【内部】可以访问, 🚀在【外部】只能通过接口（内部定义的方法）进行访问
  
	def get_income(self):  # 🔥读取私有属性的方法 (只能通过这个方法获得收入的值) => ⚡️ 封装读取私有属性的方法
		print("得到收入:", self.__income)
		return self.__income
 
	def cutdown_income(self, amount):  # 🔥写入私有属性的方法 (只能通过这个方法修改收入的值) => ⚡️ 封装修改私有属性的方法
		self.__income -= amount
		print("扣除后的收入:", self.__income)
		return self.__income

	# 定义私有方法
	def __privateMethod(self): # 🚀私有方法, 只能在内部进行调用, 外部无法调用 !!
		print("这是一个私有方法")
  
	# 公有方法
	def got_attack(self):
		return self.__privateMethod() # 🚀在内部调用私有方法 !!


smartHotel = Hotel("superRoom")
smartHotel.get_income()
smartHotel.cutdown_income(999) # 扣除私有属性的值
smartHotel.got_attack() # 调用方法 -> 方法再去调用私有方法

# 强行访问 私有属性/私有方法 的方法 [实例名._类名__方法名]
print(f"强行访问了私有属性: {smartHotel._Hotel__income}")




print("多态 ————————————————————————————————————————————————————————————————————————————————————————")
"""多态: 一个接口, 多种形态
		比如动物都有吃, 但吃的方式不一样
  		比如按钮都可以点击, 但按钮的样式不一样
"""
# 【函数接口多态】的实现方式
class superDog:
    def sound(self):
        print("汪汪叫")
        
class superCat:
    def sound(self):
        print("喵喵叫")
        
def make_sound(animal_type):
    """调用统一的接口"""
    animal_type.sound() # 不管传进来什么动物, 都调用发声方法

superDogObj = superDog()
superCatObj = superCat()
make_sound(superDogObj)
make_sound(superCatObj)


# 【抽象类接口多态】的实现方式
class Document:
	def __init__(self, name):
		self.name = name
	
	def show(self):
		raise NotImplementedError("Subclass must implement abstract method")  # ⚡️异常时候就报错, 这样【🔥强制让子类需要重写】 show 方法！
		print("Document is opening")
		

class Pdf(Document):
	def show(self):  # 🔥子类中重新实现 show 方法 => 这样才不会报错！因为上面的抽象类定义了 raise 报错!
		print("PDF is showing")
        
class Word(Document):
    def show(self): # 🔥子类中重新实现 show 方法 => 这样才不会报错！因为上面的抽象类定义了 raise 报错!
        print("Word is showing")
        
        
pdf = Pdf("未命名 PDF")
word = Word("未命名 Word")

objArr = [pdf, word]
for content in objArr:
    content.show() # 统一调用 show 方法
        






















