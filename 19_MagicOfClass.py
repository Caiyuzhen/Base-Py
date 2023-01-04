# 🔥对象的"魔法方法", 能够在不同时机下【拦截】对象的操作, 类似 hook ？

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



# 🔥增强赋值运算符
class S2(str):
	def __iadd__(self, other):
		return len(self) + len(other)

s11 = S2('Apple')
s22 ='Orange'
s11 += s22 # 12 个字符 s11 = s11 + s22
print(s11)





# 🔥将对象转化为整数（数字)（支持中文, 转化为整数）
class ZH_INT:
	def __init__(self, num):
		self.num = num

	def __int__(self): #🔥改写 int 方法!
		try:
			return int(self.num)

		except ValueError:
			# 定义一个字典
			zh = {'零':0, '一':1, '二':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9}

			result = 0

			for each in self.num:
				if each in zh:
					result += zh[each]#每个中文对应一个数字
					
				else:
					result += int(each)
				result *= 10

			return result // 10


n = ZH_INT('996')
print(int(n)) # 996


m = ZH_INT('一零七')
int(m) # 107
print(int(m)) # 107






# 🔥访问对象属性的魔法方法
class Super:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __setattr__(self, name, value):
		self.__dict__[name] = value #⚡️不能用 self.name = name, 因为会无限递归（self 就是自己）！⚡️⚡️所以要访问 __dict__, 用字典的方式来访问！！

	def __delattr__(self, name):
		del self.__dict__[name] #⚡️不能用 self.name = name, 因为会无限递归（self 就是自己）！⚡️⚡️所以要访问 __dict__, 用字典的方式来访问！！

	# def __getattribute__(self, attrName): ##获取属性值时会拦截并进行输出
	# 	print('拿来吧你')
	# 	return super().__getattribute__(attrName)

# ⚡️检测对象是否包含某个属性
superman = Super('小李', 18)
print(hasattr(superman, 'name')) # True

# ⚡️获取对象的属性值
print(getattr(superman, 'name')) # 小李

# ⚡️删除对象的某个属性
delattr(superman, 'name')





# 🔥对对象进行【索引】、【切片】、【迭代】的魔法方法
class BigData:
	def __init__(self, data):
		self.data = data

	def __getitem__(self, index):#⚡️⚡️【进行索引】 或 【进行for 操作】都会进行拦截
		print('进行索引了:')
		print(self.data[index])
		return self.data[index] #⚡️⚡️返回实例的索引值

	def __setitem__(self, index, value): 
		self.data[index] = value
		print('进行切片了:')
		print(self.data[index])  #⚡️⚡️返回实例进行切片修改的值

bigData = BigData([1, 2, 3, 4, 5,6,7])
bigData[2] # 3
bigData[2:6] = [99, 88]

for i in bigData: # i = bigData.__getitem__(i)!! 会传入魔法方法！
	print(i) # 1 2 99 88 5 6 7




# 🔥🔥iter() 和 next() 的魔法方法
# 🔥for 循环的底层原理: 用 iter() 创建一个迭代器, 然后不断调用 next() 方法来输出下一个值

x = [9, 8, 7]

mokeForFn = iter(x)
while True:
	try:
		i = mokeForFn.__next__() #next 魔法方法
	except StopIteration: # ⚡️迭代到尽头会抛出异常
		break
	print(i, end='')

# mokeForFn()





# 🔥在类中使用的 Case, 数字翻倍
class Double:
	def __init__(self, start, stop):
		self.value = start - 1
		self.stop = stop

	def __iter__(self): #⚡️⚡️定义 __iter__ 方法后就是一个可迭代对象了！！
		return self

	def __next__(self): #⚡️删掉真正的进行迭代输出
		if self.value == self.stop:
			raise StopIteration #⚡️⚡️迭代到头就停止, 比如 5 

		self.value += 1 #比如传入 5 , 就一直递增到 5
		return self.value * 2 # 0*2, 1*2, 2*2, 3*2, 4*2, 5*2


ddd = Double(1, 5) # start = 1, stop = 5, 迭代到 5 就停止
for iii in ddd:
	print('打印双倍:')
	print('\n', iii, end='')





# 🔥判断实例是否包含某个属性 __contains__ 魔法方法
class Contain():
	def __init__(self, data):
		self.data = data

	def __contains__(self, item): # item 就是从的实例传入的属性
		print("判断是否包含中...")
		return item in self.data

contain = Contain([99, 88, 77])
print(88 in contain) # '包含, True, 88 就是传入 item 的值!!
print(8 in contain) # '不包含, False, 8 就是传入 item 的值!!





# 🔥跟比较运算符相关的方法
class S(str):
	def __It__(self, other): # It 就是 < 的意思, 会拦截小于号
		return len(self) < len(other)

	def __gt__(self, other): # gt 就是 > 的意思, 会拦截大于号
		return len(self) > len(other)

	def __eq__(self, other): # It 就是 = 的意思, 会拦截等于号
		return len(self) == len(other)
	
	__eq__ = None # 取消某个魔法方法

s1 = S('ZENO')
s2 = S('zeno')
print('--分割一下--')
print(s1 > s2) # False 比较的是字符串呢的长度







# 🔥位运算(扩展阅读)
# 复习下运算符
# and 左右都为 true, 结果才为 true
# or 左右有一个为 true, 结果就为 true
# not 取反
# 3 & 2 # 2
# 3 | 4 # 7
# print(bin(3))
# print(bin(2))
# print(bin(4))
# 8 / pow(2, 3) # 1.0
# 9 >> 2 # 2







# 🔥🔥🔥🔥🔥像调用函数一样去调用一个对象, 利用 __call__ 方法
# 在类被调用时, 就会自动触发的魔法方法
# 🌟🌟🌟案例一: 无参数
class Auto():
	def __call__(self):
		print('调用类, 自动触发了～')

welcome = Auto()
welcome() # ⚡️⚡️⚡️调用类, 自动触发了～





# 🌟🌟🌟案例二:有参数
class Auto2():
	def __call__(self, *args, **kwargs): #⚡️⚡️⚡️支持位置参数以及关键字参数, 🌟一颗星 * 为位置参数, 🌟🌟两颗星 * 为关键字参数, (🔥🔥默认就是位置参数, 可以指定一个值; 关键字参数可以指定一个键值对！！)
		print(f'位置参数 => {args} \n 关键字参数 => {kwargs}')

welcome2 = Auto2()
welcome2( # 👈👈👈这里传入参数！！！传给 __call__ 方法的 args 跟 kwargs!!!🔥🔥🔥	
	'参数1', 2,  # 位置参数
	x = 998, y = 996, # 关键字参数
) 





# 🌟🌟🌟案例三: 可以替代闭包实现工厂函数的方式
class Power:
	def __init__(self, exp):
		self.exp = exp

	def __call__(self, base):
		return base ** self.exp #⚡️表示 base 的 exp 次方, 记得加上 self, 因为是实例属性


square = Power(2) # exp = 2
res = square(2)  # 传入魔法方法！base = 2!
print(res) # 2 * 2 =4






# 🔥将参数转换为字符串
print(123)
print('123')

# 🔥将参数去引号后执行
print(eval('1 + 2'))




# 🔥🔥🔥类中将参数转换为字符串的魔法方法 __repr__ 比 __str__ 更适用
class tranStr():
	def __init__(self, data):
		self.data = data

	def __str__(self):
		return f'data = {self.data}'

	def __repr__(self):
		return f'result({self.data})' # 直接访问实例的显示形式（没有试出来，后续看看）

	def __add__(self, other):
		self.data += other


ccc =tranStr(250) # 🌟🌟 str 参数会调用 __str__ 方法
print(ccc) # data = 250 


ccc + 250 # 250 + 250 = 500 ， 🌟🌟 + 运算会会调用 __add__ 方法
print(ccc) # data += 250   =>   500


