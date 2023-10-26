"""
    对象跟对象之间的关系
        1.交互关系（比如攻击）
          2.依赖关系(附属)
        3.关联关系（比如亲友、员工与老板 => 纽带、契约）
        4.组合关系（比如器官、大脑、心脏, 比聚合还要紧密, 一个坏就全部坏）
        5.聚合关系（比如电脑跟零部件, 一个坏没事可以安装到另一处身上）
          6.继承关系（比如父子）
"""



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



print("——————————————————————")




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



print("——————————————————————")




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