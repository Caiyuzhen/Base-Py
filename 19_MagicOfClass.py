# 🔥对象的"魔法方法"

# 🔥__new__(cls[...,...]) #创建对象时最开始执行的方法（一般不会改到 new 方法）
# 比如修改原来 string 的原始对象(全部变为大写)：

# class CapStr(str):
	# def __new__(cls, string):
	# 	string = string.upper()
	# 	return super().__new__(cls, string) # 把修改后的参数返回给父类！


# 🔥对象【被销毁前】执行的方法, 当对象不在被引用时, 会被垃圾回收机制给销毁
class C:
	def __init__(self):
		print('来了～')

	def __del__(self):
		print('走了～')

c1 = C()
d = c1
del c1 # ⚡️⚡️ del 是 Python 中的一个内置关键字，它的作用是删除一个对象的引用或一个变量。
del d # 所有被引用的对象都被销毁时, 才会执行 __del__ 方法





# 🔥在对象被销毁前, 把对象的 self 给送出去, 可以让对象【重生】
class D:
	def __init__(self, name, func): # 🔥 func 用来送出 self, 利用【闭包函数】来保存 self！！！
		self.name = name
		self.func = func

	
	def __del__(self):
		self.func(self) # 🔥调用 func 函数式


def outter(): # 🔥闭包函数, 默认为 none， 返回 y, 传入 self 时, 会修改 x, 返回 self
	x = 0
	def inner(y = None):
		nonlocal x # ⚡️⚡️⚡️nonlocal 用来修改外层函数的变量(⚡️⚡️否则无法修改！)
		if y:
			x = y
		else:
			return x

	return inner #返回闭包函数



f = outter()#外部使用不带参数, 默认为 none！！所以会返回 x
e = D('小李', f) #⚡️⚡️⚡️把函数作为参数传入, self 会传入到函数中！！



del e # 删除实例

g = f()
print(g.name)




# 🔥统计字符串相加的总数
class S(str):
	def __add__(self, other): #self 方法（⚡️第一个实例才会被重写）
		return len(self) + len(other) # 重写字符串的加法方法

s1 = S('abc') 
s2 = S('def')
s1 + s2 # 6 个字符