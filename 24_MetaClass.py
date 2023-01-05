# 🔥元类, 元类是用来创造类的模板, type 也是一种元类
# 类 -> 元类 -> type
# 🔥🔥🔥🔥🔥限制类实定义过程, 就用 __init__ 方法或 __new__ 方法！
class MetaC(type):
	def __new__(mcls, name, bases, attrs): #🔥跟 type 传递的参数一样！！类名、父类、指定的属性和方法、第四个参数 attrs 代表的是这个【元类的属性】字典
		print('MeatC 里边的__new__方法') #👉定义好【类】后, 元类里边的这里就会直接被触发
		return type.__new__(mcls, name, bases, attrs) #🔥🔥把参数返回给父类来实现！

	def __init__(cls, name, bases, attrs):
		print('MeatC 里边的__init__方法') #👉定义好【类】后, 元类里边的这里就会直接被触发
		return type.__init__(cls, name, bases, attrs) #🔥🔥把参数返回给父类来实现！ 父类就是 type


class C(metaclass=MetaC): #引入元类来创造类
	def __new__(cls):
		print('C 里边的__new__方法') #👉在类实例化对象的那一刻才被触发
		return super().__new__(cls) #🔥🔥或把参数返回给父类来实现！ 父类是 object

	def __init__(self): #👉在类实例化对象的那一刻才被触发
		print('C 里边的__init__方法')


c = C()






# 🔥🔥🔥🔥🔥限制类实例化过程, 就用 __call__ 方法
# 🔥🔥类中定义的 __call__ 方法就是拦截【对象被当作函数调用】的操作, 元类中定义的 __call__ 方法就是拦截【类实例化对象】的操作
class MetaA(type):
	def __call__(cls, *args, **kwargs):
		print('MetaA 里边的__call__方法') #👉在类实例化对象的那一刻才被触发


class AA(metaclass=MetaA):
	pass

a = AA() #👉在类实例化对象的那一刻才会调用 __call__ 方法






# 🔥🔥🔥🔥🔥限制类实定义过程, 就用 __init__ 方法或 __new__ 方法！
# 🔥🔥元类的实际应用场景 1: 🔥🔥🔥比如给所有类都添加一个（作者）的属性
class MetaB(type):
	def __new__(mcls, name, bases, attrs): #⚡️⚡️⚡️第四个参数 attrs 代表的是这个【元类的属性】字典
		attrs['author'] = '小明'
		return type.__new__(mcls, name, bases, attrs)

	def __init__(cls, name, bases, attr): #⚡️⚡️⚡️第一个参数传入【类】
		cls.editor= '小李'
		return type.__init__(cls, name, bases, attr)



class BB(metaclass=MetaB):
	pass

class DD(metaclass=MetaB):
	pass

print(BB.author) #👉小明
print(BB.editor) #👉小李
print(DD.author) #👉小明
print(DD.editor) #👉小李




# 🔥🔥🔥🔥🔥限制类实定义过程, 就用 __init__ 方法或 __new__ 方法！
# 🔥🔥元类的实际应用场景 2: 🔥🔥🔥比如统一类名的定义规范, 需要统一为大写形式！
class MetaIsTitle(type):
	def __init__(cls, name, bases, attrs):
		if not name.istitle(): #标题格式, 即首字母大写, 其他字母小写, not 表示取反（不是大写的情况）
			raise TypeError('类名必须是大写形式！')

		type.__init__(cls, name, bases, attrs) #如果是大写就交给 type 来实现



# class abc(metaclass=MetaIsTitle): #会报错
	# pass




# 🔥🔥🔥🔥🔥限制类实例化过程, 就用 __call__ 方法
# 🔥🔥元类的实际应用场景 3: 把对象的所有属性值都变为大写
class MetaChange(type):
	def __call__(cls, *args, **kwargs): #🌋🌋🌋因为这里要影响类实例化的过程, 所以用 __call__ 方法(在元类中的 call 方法是在类实例化过程中触发的【而不是】类被当作函数调用时触发！)
		new_args = [each.upper() for each in args if isinstance(each, str)]#🌋🌋🌋因为要改变类中传入的属性值, 所以要收集类中的属性值！！upper() 用于将字符串中的所有字母转换为大写
		return type.__call__(cls, *new_args, **kwargs) #🔥🔥🔥 *args 改变为大写后, 返回给父类！！！

class Text(metaclass=MetaChange):
	def __init__(self, name):
		self.name = name

text = Text('zen')
print(text.name) #👉ZEN




# 🔥🔥元类的实际应用场景 4: 限制类实例化时传参的方式（比如不能传入位置参数）
class MetaLimit(type):
	def __call__(cls, *args, **kwargs): # args 代表关键字参数  kwargs 代表位置参数!!!
		if args:
			raise TypeError('仅支持关键字参数！')

		print('👌')
		return type.__call__(cls, *args, **kwargs) #如果是关键字参数就交给 type 来实现（实现类的定义等等..)


class ARG(metaclass=MetaLimit):
	def __init__(self, name):
		self.name = name

# arg = ARG('zen') #👉仅支持关键字参数！
arg = ARG(name='zen') #👉OK 👌





# 🔥🔥🔥🔥🔥限制类实例化过程, 就用 __call__ 方法
# 🔥🔥元类的实际应用场景 5 : 禁止类被实例化
class NoInstances(type):
	def __call__(cls, *args, **kwargs):
		raise TypeError('禁止实例化！')




class WellDone(metaclass=NoInstances):
	@staticmethod #🔥🔥虽然禁止被实例化, 但是可以使用静态方法！！
	def static_ok():
		print('可以访问静态方法')

	@classmethod
	def class_ok(cls): #⚡️⚡️⚡️ cls 是传入一个类！！! 会把 WellDone 传入进来！！
		print('可以访问类方法')



# well = WellDone() #👉禁止实例化！
WellDone.static_ok() #👉可以访问静态方法
WellDone.class_ok() #👉可以访问类方法






# 🔥🔥🔥🔥🔥限制类实例化过程, 就用 __call__ 方法
# 🔥🔥元类的实际应用场景 5 : 只允许实例化一个对象！
# 不太好的写法, 第二个不能被返回
# class OnlyOne(type):
# 	count = 0

# 	def __call__(cls, *args, **kwargs): #cls 是传入一个类！！! 会把 OnlyOne 传入进来！！
# 		if cls.count == 0:
# 			cls.count += 1
# 			return type.__call__(cls, *args, **kwargs)
# 		else:
# 			raise TypeError('只允许实例化一个对象！')

# class Only(metaclass=OnlyOne):
# 	pass

# one = Only()
# # one = Only()


# 优化写法, 第二个能被返回
class OnlyOne2(type):
	def __init__(cls, *args, **kwargs):
		cls.__instance = None # 🔥🔥用两个 __ 来定义私有变量！!
		type.__init__(cls, *args, **kwargs)
	
	def __call__(cls, *args, **kwargs):#实例化的时候, call 会被调用, 会检测
		if cls.__instance is None:
			cls.__instance = type.__call__(cls, *args, **kwargs) #实例化一个对象, 并且赋值给 __instance
			return cls.__instance#🔥🔥记得 return 给 cls 也就是类本身！！把之前的实例返回给它（限制第二次实例）
		else:
			return cls.__instance #把之前的实例返回给它（限制第二次实例）


class Only2(metaclass=OnlyOne2):
	pass

c1 = Only2()
c2 = Only2()
print(c1 is c2) #👉True


		
