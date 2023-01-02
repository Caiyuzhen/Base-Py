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

	def run(self): #self 是一个形参，代表的是当前对象，如果没有 self 会报错!!
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





# ⚡️🔥多态