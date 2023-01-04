# 🔥Property 函数（需要传入⚡️三个函数参数，分别是【获取】、【写入】、【删除】）, 类似装饰器的原理！！
class CC:
	def __init__(self):
		self.x = 250

	def getX(self): #【第一个函数参数 - 获取】
		return self.x

	def setX(self, value): #【第二个函数参数 - 写入】
		self.x = value

	def delX(self): #【第三个函数参数 - 删除】
		del self.x

	y = property(getX, setX, delX) #⚡️⚡️ y 用来代理 x!!


zen = CC()
print(zen.y)

del zen.y #⚡️ 删除 x 属性
print(zen.__dict__) #⚡️ x 属性被删除




# 如何不用 property 函数来实现上面的 y 代理 x 的功能呢？
class DD:
	def __init__(self):
		self.x = 996

	def __getattr__(self, name):
		if name == 'y': #🔥🔥如果是 y 的话，就返回 x
			return self.x
		else:
			super().__getattribute__(name) #不是 y 的话，就交回给父类, 把 name 返回

	def __setattr__(self, name, value): #🔥🔥不能 self.name = value，否则会陷入死循环！！！⚡️\
		if name == 'y':
			super().__setattr__('x', value) # 是 y 的话，就把 value 赋值给 y
		else:
			super().__setattr__(name, value) # 不是 y 的话，⚡️就交回给父类, 把 value 赋值给 name
		
	def __delattr__(self, name):
		if name == 'y':
			super().__delattr__('x') # 是 y 的话，就把删除 y 属性
		else:
			super().__delattr__(name) # 不是 y 的话，⚡️就交回给父类, 把删除 name 属性
	
dd = DD()
print(dd.y)

del dd.y
print(dd.__dict__)





# 🔥Property 函数的另一个好处！ 让【属性只读】！！
# ⚡️原理是因为只传入一个【函数参数】, 因为第一个参数代表【获取、只读】, 所以【这个属性】就只能【获取】，不能【写入】和【删除】！！
class EE:
	def __init__(self):
		self.x = 888

	@property  #⚡️⚡️ 把 Property 函数当做装饰器来使用！！
	def y(self):  #⚡️⚡️ y 代理 x！！
		return self.x   #⚡️⚡️ y 代理 x！！


ee = EE()
print(ee.y) #可以读取
# ee.y = 999 #不能写入！！



# 🔥Property 函数装饰器的使用！
class GG:
	def __init__(self):
		self.x = 555

	@property  #⚡️⚡️ 把 Property 函数当做装饰器来使用！！这样就可以直接调用 y 了！！不用调用 y() ！！
	def y(self):  #⚡️⚡️ y 代理 x！！
		return self.x   #⚡️⚡️ y 代理 x！！

	@y.setter #⚡️⚡️ 把 Property 函数当做装饰器来使用！！property 身上的 setter 装饰器！
	def y(self, value):  #⚡️⚡️ y 代理 x！！
		self.x = value

	@y.deleter #⚡️⚡️ 把 Property 函数当做装饰器来使用！！property 身上的 deleter 装饰器！
	def y(self):  #⚡️⚡️ y 代理 x！！
		del self.x #删除属性


gg = GG()
print(gg.y) #可以读取, 🎃🎃🎃因为上面使用了 @property 装饰器，所以这里可以直接调用 y 了！！不用调用 y() ！！

del gg.y #可以删除
print(gg.__dict__)




# 🔥🔥多个装饰器的使用
# Case 1: 不用多个装饰器, 需要调用函数
class Say():
	@classmethod
	def __doc__(cls):
		return f"这是一个类方法, 来自{cls.__name__}" #🔥🔥cls 表示 Says 本身！

say = Say()
print(say.__doc__()) #调用函数




# Case 2: 用多个装饰器, 就不需要调用函数了, 直接调用属性
class SayHi():
	@classmethod # 顺序 2,  多个装饰器的执行顺序是自下而上的！
	@property    # 顺序 1,  多个装饰器的执行顺序是自下而上的！
	def __doc__(cls):
		return f"这是一个类方法, 来自{cls.__name__}" #🔥🔥cls 表示 Says 本身！

sayHi = SayHi()
print(sayHi.__doc__) #调用属性



	

