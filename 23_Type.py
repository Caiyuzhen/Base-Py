# 🔥Type 、isinstance 用来判断对象的类型
print(type(1)) # <class 'int'>
print(type(3.14))
print(type('hello'))
print(type([1,2,3]))
print(type((1,2,3)))
print(type({1,2,3}))
print(type({1:2, 3:4}))

print(type(True))
print(type(None))
print(str(3.14))
print(int(3.14))
print(float(3.14))
print(bool(0))

print(type(250)('996')) # 相当于 int('996'), 因为 type(250) -> 会变成 int
print(type([])('hello')) # 相当于 list('hello'), 因为 type([]) -> 会变成 list
print(type({}).fromkeys(['hello', 'world']))# 相当于 dict.fromkeys('python'), 因为 type({}) -> 会变成 dict， 会根据传入的参数来【作为字典的 key】


class C:
	def __init__(self, name):
		self.name = name

c = C('小明')
print(type(c)) 

d = type(c)('小李') # d 也是一个 C 类的实例, 相当于 d = C('小李')!!
print(type(d)) #🌟查看对象类型的方法一
print(d.__class__) #🌟查看对象类型的方法二



# 🔥🔥类本身也是 type！git
print(type(C)) # type



print(' \n __分割线__ \n')


# 🔥🔥利用 type 的方式来定义类
# 普通的类定义的方式
class C:
	pass


# type 定义类的方式, 第一个参数传入类名
A = type('C', (), {}) # 第一个参数是类名, 第二个参数是父类(用于继承)并且第二个参数需要是个元祖类型所以要加个【, 逗号】, 第三个参数是类的属性和方法, 需要传入字典
a = A() # a 是一个 C 类的实例

print(a.__class__)
print(A.__base__) # 因为没有指定类型, 所以 A 的父类是 object





# type 定义类的方式, 第二个参数传入父类
D = type('D', (C, ), {}) #⚡️⚡️第二个参数需要是个元祖类型所以要加个【, 逗号】!!
d = D()
print(d.__class__) # d 的类型是 D
print(D.__bases__) # d 的父类是 C




# type 定义类的方式, 第三个参数传入属性
E = type('E', (), dict(x=1, y=2))





# type 定义类的方式, 第三个参数传入函数
def funC(self, name='world'):
	print(f'hello {name}')

F = type('F', (), dict(sayHi = funC)) # 第三个参数可以传入函数方法
f = F()
f.sayHi('Zen') #⚡️⚡️调用 F 类的 funC 方法并传入参数





# __init_subclass__ 用于管理子类
class CC:
	def __init_subclass__(cls): #用于管理子类！！
		print('你好~触发了父类')
		cls.x = 996

class DD(CC):
	xx = 1

print(DD.x) # 996 #还是父类的 x 属性， 因为上面调用了 __init_subclass__ 方法！子类没法修改其属性




class GG:
	def __init_subclass__(cls, value):
		print('你好~触发了父类')
		cls.x = value

class KK(GG, value=996):#value 传给父类
	x = 88 # 会被父类所拦截

print(KK.x) # 996, ⚡️还是会被父类所拦截！





#type 定义类的方式, 第四个参数传入【元类的属性】字典！
class Glass:
	def __init_subclass__(cls, value1, value2):
		print('你好~触发了 Glass 父类')
		cls.x = value1
		cls.y = value2

KP = type('KP', (Glass,), dict(x=3333), value1=777, value2=333) #value 传给父类
print(KP.x) #👉🔥🔥不是 333, 🔥🔥而是会被父类拦截为 cls.x = value1 =  777!!












