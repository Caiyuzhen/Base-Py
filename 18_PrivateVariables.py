# 🔥"私有变量", Python 没有那种只有在类里边才能访问的便利
# 🔥🔥用两个 __ 来定义私有变量！
# _XXX 变量一般是内部的，不建议修改的  XXX_ 结尾的变量一般是系统变量，不建议修改的
class A:
	def __init__(self, x):
		self.__xxy = x

	def set_x(self, x):
		self.__xxy = x  # 修改私有变量 x 的值

	def get_x(self):
		print(self.__xxy)  # 修改私有变量 x 的值

a = A(150)
# print(a.__xxy) # 会报错！因为 __xxy 是私有变量，只能通过外露的 set 跟 get 方法来访问！
a.get_x()



# 🔥存放构造函数的位置在字典内 (__dict__ 方法)
# 🔥利用字典来存放内容是浪费空间（因为复用性不高）
print(a.__dict__)
a.__dict__['name'] = 'zen' # ⚡️在构造函数内添加一个属性
print(a.name)





# 🔥🔥利用 __slots__ 来限制实例可以添加属性的名称, 🔥🔥并且可以降低内存消耗！缺点就是失去了动态添加属性的能力（灵活性）！
# 案例一:
class C:
	__slots__ = ['x', 'y'] # 🔥🔥定义属性名称, 用 __slots__ 来限制实例可以添加属性的名称！
	def __init__(self, x):
		self.x = x

c = C(100)
print(c.x) # 100
# c.z = 200 # 🔥🔥会报错, 因为 __slots__ 限制了实例只能添加 x, y 两个属性！




# 案例二:
class D:
	__slots__ = ['x', 'y']
	def __init__(self, x, y):
		self.x = x
		self.y = y
		# self.z = z #🔥🔥会报错, 因为 __slots__ 限制了实例只能添加 x, y 两个属性！




# 案例三（🔥子类继承父类的话, __slot__ 会被子类继承但是【⚡️不会被父类的 __slot__ 限制】, 因为子类会生成一个 __dict__ 属性!!）:
class E(D):
	def __init__(self, x, y, z):
		super().__init__(x, y)
		self.z = z
	
e = E(100, 200, 300)
print(e.x)
print(e.z) # 300