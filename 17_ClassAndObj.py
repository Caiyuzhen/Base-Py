# 🔥Python 的类和对象
# 对象 = 属性 + 方法 （比如猫，猫静态属性 = 花色，猫静态方法 = 奔跑）
# 类 = 对象的抽象
# 类名需要大写开头

# ⚡️🔥封装一个对象
class Cat:
	head = 1
	eyes = 2
	legs = 4
	hair = 5

	def run(self): #self 代表的是当前对象的实例对象本身！用来做绑定对象，如果没有 self 会报错!!
		print("猫在爬行")

	def eat(self):
		print("猫在吃鱼")

	def drink(self):
		print("猫在喝水")


# ⚡️实例化对象
dudu = Cat()
print(dudu.head)
dudu.run()
dudu.drink()


# ⚡️修改对象的属性
dudu.hair = 4
print(dudu.hair)

dudu.mouse = 1
print(dudu.mouse)








# ⚡️🔥继承
# 子类继承父类
class A:
	x = 996
	z = 9
	def Says(self):
		print('🌞Hey~')

class B(A):  #继承 A 类！
	x = 998 #会覆盖 A 类的 x 属性
	pass

b = B()
b.Says() # 可以访问到 A 的方法
print(b.x)

print(isinstance(b, A)) # 判断 b 实例是否是 A 的实例, 返回 True
print(issubclass(B, A)) # 判断 B 是否是 A 的子类, 返回 True









# 🔥多重继承！！(继承多个类) ⚡️继承的前提是有从属关系！！
class C:
	x = 88
	y = 99
	def Says(self):
		print('🌛Good Night~')

class D(A, C): # 继承 A 和 C 类, 访问顺序从左往右！
	pass

D = D()
D.Says() # 会优先调用 C 类的方法, 覆盖 A 类的方法
print(D.z) # 会调用到 A 类的 z 属性, 因为在当前类中找不到








# ⚡️🔥类的组合 (⚡️没有从属关系的话，就使用组合而不是继承！)
class Turtle:
	def say(self):
		print('讲真理')

class Person:
	def say(self):
		print('说谎')

class Cat:
	def say(self):
		print('喵喵叫')

class Room: # ⛰️⛰️⛰️类似单实例的模式！
	t = Turtle()
	p = Person()
	c = Cat()

	def says(self):
		self.t.say()
		self.p.say()
		self.c.say()


R = Room()
R.p.say()





# 🔥self 绑定, 比如给实例新增一个属性, 其他实例就访问不到的！
class AA:
	pass

aa = AA()
aa.name = '太阳'  

bb = AA()
# print(bb.name) # 报错, 因为 bb 实例没有 name 属性, 只有 aa 实例有 name 属性





# 🔥查看类的所有属性
print(aa.__dict__) # 内省，查看 aa 实例的所有属性



# 🔥🔥🔥在实例上, 通过类里边的方法来设置实例属性？ 在 self 身上进行设置
class BestCat:
	def setProperties(self, name):
		self.x = name

best = BestCat()
best.setProperties('饭团') # 相当于设置为 x = '饭团', 注意，只设置到了 best 这个实例身上！
print(best.__dict__) # {'x': '饭团'}
print(best.x) # 饭团







# 👇不建议直接给类添加额外属性！使用场景可能只有下面这个（把类当成字典来使用）
BestCat.x = '200'


# 🔥类和对象的属性就是通过字典进行存储的！可以定义一个最小的类，然后通过字典的方式进行访问！⚡️比字典更快更方便！
class Small:
	pass

small = Small() # 🔥一般通过类的实例来模拟字典，不直接改类！
small.x = 250
small.y = 'Hellow World~'
small.z = [1, 2, 3]

print(small.x, small.y, small.z) # 250 Hellow World~ [1, 2, 3]




# 👆用字典的方式改写上面的代码, 但是效率会更慢
SmallTwo = {}
SmallTwo['x'] = 250
SmallTwo['y'] = 'Hellow World~'
SmallTwo['z'] = [1, 2, 3]

print(SmallTwo['x'], SmallTwo['y'], SmallTwo['z']) # 250 Hellow World~ [1, 2, 3]




# ⚡️🔥构造函数
class SuperMan:
	def __init__(self, x, y):  #⛰️⛰️ __init__ 用来定义构造函数, 会在实例化的时候自动调用
		self.x = x # 右边的 x 是传入的参数, 左边的 x 是实例的属性
		self.y = y

	def add(self):
		return self.x + self.y

	def mul(self):
		return self.x * self.y


superman = SuperMan(2, 3)
print(superman.add()) # 2 + 3 = 5
print(superman.mul()) # 2 * 3 = 6




# 🔥🔥🔥子类对父类的【重写】
class Hero(SuperMan): # 继承自 SuperMan 父类
	def __init__(self, x, y, z): #多一个 z 的参数, self.z 是当前 SuperHero 类的属性
		SuperMan.__init__(self, x, y)  #🔥🔥🔥调用【父类】的构造函数！！这样就可以省写 self.x = x, self.y = y
		self.z = z
	
	def add(self):
		return SuperMan.add(self) + self.z # 🔥🔥🔥重写父类的方法, SuperMan.add(self) 相当于调用父类的 add 方法, 最终为 x + y + z!!

	def mul(self):
		return SuperMan.mul(self) * self.z # 🔥🔥🔥重写父类的方法, SuperMan.add(self) 相当于调用父类的 mul 方法, 最终为 x * y * z!!


hero = Hero(2, 3, 4)
print(hero.add()) # 2 + 3 + 4 = 9
print(hero.mul()) # 2 * 3 * 4 = 24



# 🔥🔥🔥利用 Super 去查找父类的方法来避免 💎钻石继承的问题！
class AAA:
	def __init__(self):
		print('AAA')

class BBB_1(AAA):
	def __init__(self):
		# AAA.__init__(self) # 💎这样会有钻石继承的问题，AAA 会被调用多次！
		super().__init__()
		print('BBB_1')


class BBB_2(AAA):
	def __init__(self):
		# AAA.__init__(self) # 💎这样会有钻石继承的问题，AAA 会被调用多次！
		super().__init__()
		print('BBB_2')

class CCC(BBB_1, BBB_2):
	def __init__(self):
		# BBB_1.__init__(self) # 💎这样会有钻石继承的问题，AAA 会被调用多次！因为 BBB_1 继承了 AAA
		# BBB_2.__init__(self) # 💎这样会有钻石继承的问题，AAA 会被调用多次！因为 BBB_2 继承了 AAA
		super().__init__() # 🔥会自己遍历 BBB_1 跟 BBB_2 !!
		print('CCC')

ccc = CCC() # AAA BBB_1 BBB_2 CCC
print(CCC.mro())# 底层 mro 方法的调用顺序是：CCC -> BBB_1 -> BBB_2 -> AAA






# 🔥Mix-in 模式（设计模式）
# 案例一
class Animal:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def say(self):
		print(F'我是 {self.name}, 我今年 {self.age} 岁了！')


class AbilityMixin: # ⚡️一般来说, 带Mixin 就是后期补充的功能
	def fly(self):
		print('我会飞')


class Dog(Animal, AbilityMixin): # ⚡️继承多个父类时, 先左后右执行！
	def swim(self): # 这个方法是 Animal 类没有的
		print('我会游泳')


dog = Dog('小黑', 3)
dog.say() # 我是 小黑, 我今年 3 岁了！
dog.swim() # 我会游泳
dog.fly()





# 🔥案例二 (最终是创建一个 subclass.txt 再写入一段文字)
class Displayer:
	def display(self, message):
		print(message)


class LoggerMixin: # ⚡️一般来说, 带Mixin 就是后期补充的功能
	def log(self, message, filename='logfile.txt'):
		with open(filename, 'a') as f:
			f.write(message)

	def display(self, message):
		super().display(message) # 🔥因为没写父类, 根据 MRO 顺序, 会自动找到 Displayer 的 display 方法
		self.log(message) # 在运行的时候, self 指向的是 MySubClass 的实例对象, 所以会调用 MySubClass 的 log 方法


class MySubClass(LoggerMixin, Displayer): # ⚡️继承多个父类时, 先左后右执行！
	def log(self, message):
		super().log(message, filename='subclasslog.txt')

subclass = MySubClass()
subclass.display('This is a test~')









# ⚡️⚡️⚡️多态(同一个接口，在不同的上下文中有着不同的实现)
# ⚡️案例一 len() 函数技能获取【字符串】的长度（数量）, 也能获取【列表内元素】的长度（数量）
print(len('Zennn')) # 5
print(len([1, 2, 3])) # 3
print(len({'a': 1, 'b': 2})) # 2, key 的长度（数量）



# ⚡️案例二
class Shape: # 基类
	def __init__(self, name):
		self.name = name

	def area(self): # 计算面让子类来实现
		pass



class Square(Shape):
	def __init__(self, length):
		super().__init__('正方形') # 调用父类的 name
		self.length = length # 用于计算面积
	
	def area(self):
		return self.length * self.length # 正方形的面积为 边长 * 边长



class Circle(Shape):
	def __init__(self, radius):
		super().__init__('圆形') # 调用父类的 name
		self.radius = radius # 用于计算面积
	
	def area(self):
		return 3.14 * self.radius * self.radius # 圆形的面积为 3.14 * 半径的平方



class Triangle(Shape):
	def __init__(self, bottom, height):
		super().__init__('正方形') # 调用父类的 name
		self.bottom = bottom # 用于计算面积
		self.height = height # 用于计算面积
	
	def area(self):
		return self.bottom * self.height / 2 # 三角形的面积 = 底 * 高 / 2


circle = Circle(3)
print(circle.area()) # 28.26

square = Square(3)
print(square.area()) # 9

triangle = Triangle(3, 4) # 底为 3, 高为 4
print(triangle.area()) # 6.0




# ⚡️案例三
class SuperCat:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def intro(self):
		print(F'我是 {self.name}, 我今年 {self.age} 岁了！')

	def say(self):
		print('我是一只超级猫！')



class SuperDog:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def intro(self):
		print(F'我是 {self.name}, 我今年 {self.age} 岁了！')

	def say(self):
		print('我是一只超级狗！')
		


class SuperFish:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def intro(self):
		print(F'我是 {self.name}, 我今年 {self.age} 岁了！')

	def say(self):
		print('我是一只超级鱼！')


superCat = SuperCat('饭团', 3)
superDog = SuperDog('鸡腿', 2)
superFish = SuperFish('鱼鱼', 1)


from typing import TypeVar # ⚡️⚡️注释为范型！
T = TypeVar('T', SuperCat, SuperDog, SuperFish) # ⚡️⚡️定义范型！

 # 多态函数！🔥🔥🔥传入的参数是一个对象的实例, 根据不同的实例, 执行不同的方法！！
def SuperAnimal(x: T):
	x.intro()
	x.say()

SuperAnimal(superCat)
SuperAnimal(superDog)
SuperAnimal(superFish)





# ⚡️案例四（鸭子类型, 具备相同方法的话, 也可以被包装进多态函数内！也可以被 SuperAnimal 调用！不管它是什么类型, 什么类型是人定的语义)
class SuperBicycle:
	def intro(self):
		print('跨越山丘')

	def say(self):
		print('我是一辆自行车')

superBicycle = SuperBicycle()
SuperAnimal(superBicycle) #🔥🔥🔥只要具备相同的方法, 就可以被包装进多态函数内