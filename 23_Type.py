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
