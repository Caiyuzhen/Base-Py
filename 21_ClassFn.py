# 🔥🔥类方法跟静态方法表现类似,当【操作不涉及类属性或属性的引用】时,可以使用【静态方法】,当【操作主要是统计实例对象】时,可以使用【类方法】
# 🔥🔥类方法（classmethod), 以往类里边定义的方法, 类本身是无法调用的, 需要实例化的绑定类来使用, 类方法就是可以直接使用类来调用的方法
class CC:
	count = 0
	
	@classmethod #类方法
	def add(cls):#⚡️⚡️⚡️ cls 是传入一个类！！!
		cls.count += 1

	def __init__(self):
		self.add() #当实例化对象的时候, __init__ 这个构造函数就会去调用类方法, 从而实现类属性的统计(⚡️子类去调用的话, self 就是子类, 所以就能够实现子类的数量统计！！)

	@classmethod #类方法, 不会有继承问题, 🔥🔥也不会因为实例改变了 count 的值, 而影响到类的 count 的值
	def getCount(cls): #⚡️⚡️cls 代表的是类本身, ⚡️⚡️⚡️ cls 是传入一个类！！!
		print(f'当前类的实例化对象个数为: {cls.count}')  #⚡️⚡️cls 代表的是类本身
		# return cls.count #⚡️⚡️cls 代表的是类本身



a = CC() #实例化 1 个对象
b = CC() #实例化 2 个对象
c = CC() #实例化 3 个对象
print(c.getCount())


class D(CC): # 继承情况
	count = 0

class E(CC): # 继承情况
	count = 0

c1 = CC()
d1, d2 = D(), D()
e1, e2, e3 = E(), E(), E() # count = 552 +1 +1

print(d1.count) #
print(e2.getCount()) 






# 🔥🔥静态方法 (在类里边定义一个不需要绑定的函数)
# 案例一
class AA:
	@staticmethod
	def func():
		print('静态方法') #静f方法，不需要绑定实例来调用！
		return '静态方法'

aa = AA()
aa.func()
print(AA.func())





# 案例二
class BB:
	count = 0
	def __init__(self):
		BB.count += 1

	@staticmethod
	def getCount():
		print(BB.count) #⚡️⚡️静态方法，直接通过 BB 类名来调用类里边的属性！！！不用担心子类的属性被覆盖从而导致无法统计子类数量！! 因为是通过【类】本身来调用的！！
		return BB.count

b1 = BB()
b2 = BB()
b3 = BB()
b4 = BB()
print(b3.getCount())