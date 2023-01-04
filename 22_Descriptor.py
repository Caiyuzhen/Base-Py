# 🔥🔥描述符(类方法、静态方法、property 函数的底层实现)
# 只要是实现了 __get__、__set__、__delete__ 三个方法中的任意一个或多个方法的类，这个类就叫做描述符！！
# 跟魔法方法的差异是, 描述符是类级别的（管别人家的属性）, 而魔法方法是实例级别的 (管自己家的属性)

class DD:
	def __get__(self, instance, owner): 
		print(f'self -> {self} \n instance -> {instance} \n owner -> {owner}')

	def __set__(self, instance, value): 
		print(f'self -> {self} \n instance -> {instance} \n value -> {value}')

	def __delete__(self, instance):
		print(f'self -> {self} \n instance -> {instance}')

class C: # 🌟 owner 对应的是, 被【描述符】【拦截的属性】【所在的类】
	x = DD() # 🌟self 对应的是【描述符的实例对象】, 也就是 x  ->  把 x 属性变为描述符
	#上面描述符只能用在类属性！不能用在实例属性！比如 def __init__(self): self.x = DD() 会报错!!

c = C() #🌟 instance 对应的是, 被【描述符】【拦截的属性】【所在的类】的【实例对象】, 也就是 c
c.x = 250







# 🔥🔥🔥数据描述符: 实现了 __set__ 或 __delete__ 就是数据描述符, 只实现 __get__ 就是非数据描述符
# 实例属性优先级高于非数据描述符, 所以实例属性会覆盖描述符, 但是数据描述符的优先级又高于实例属性, 所以数据描述符不会被实例属性所覆盖！
print("\n ___这是一根分割线___ \n")


# 🔥🔥通过描述符拦截实例属性后, 进行进一步的操作(不够优雅的实现方式！！)
class PP:
	def __init__(self, name):
		self.name = name

	def __get__(self, instance, owner):
		print('get~aha~成功从对象中读取数据')
		return instance.__dict__.get(self.name) # 🌟把实例属性的操作交给了 dict__get 方法

	def __set__(self, instance, value):
		print('set~aha~成功写入数据到对象的字典中')
		instance.__dict__[self.name] = value


class KK():
	L = PP('Zeno') # 🌟把 L 赋值给描述符, 不优雅的方式, 因为要传入 name！👇下面那个方法更优雅！
 
kk = KK()
kk.L

kk.L = 250






# 🔥🔥🔥通过描述符拦截实例属性后, 进行进一步的操作(更加优雅的实现方式！！__set_name__ 方法)
class FG:
	def __set_name__(self, owner, name): #🌟🌟__set_name__ 就不用再在 AA() 属性中传入 name 了！！
		self.name = name

	def __get__(self, instance, owner):
		print('get~aha~成功从对象中读取数据')
		return instance.__dict__.get(self.name) # 🌟把实例属性的操作交给了 dict__get 方法

	def __set__(self, instance, value):
		print('set~aha~成功写入数据到对象的字典中')
		instance.__dict__[self.name] = value


class AA():
	L = FG() # 🌟把 L 赋值给描述符
 
aa = AA()
aa.L

aa.L = 250






print("\n ___这是一根分割线___ \n")





# 🔥🔥🔥函数装饰器, 用于拦截类的实例化过程, ⚡️⚡️⚡️在类实例化之前进行干预！！
def report(cls):
	def onCall(*args, **kwargs): #🔥🔥🔥🔥第二步, 收集参数, (1,2,3) 被打包成元祖, 传入 *args
		print('开始实例化对象...') #第三步

		a = cls(*args, **kwargs) #🔥🔥🔥🔥第四步,  *args 表示把元祖解包成 (1,2,3), 传入 cls 的构造函数

		print('实例化对象成功！') #第七步
		return a #第八步, 返回实例化对象, 赋值给下面的 final

	return onCall



@report #🔥🔥🔥🔥语法糖, 相当于 Res = report(Res)
class Res:
	def __init__(self, x, y, z): #第五步, 传入三个参数
		self.x = x
		self.y = y
		self.z = z
		print('构造函数被初始化调用成功！') #第六步

final = Res(1,2,3) #🔥🔥🔥🔥装饰器使然, 相当于 onCall(1,2,3)!! 第一步，传入参数









#🔥🔥🔥类装饰器
#案例: 不用类装饰器的实现, 利用类的 __call__ 方法, 实现一个统计被调用次数的类
class Counter:
	def __init__(self):
		self.count = 0

	def __call__(self):
		self.count += 1
		print(f'这是第 {self.count} 次被调用')


finalCount = Counter()
finalCount()
finalCount()



print("\n ___这是一根分割线___ \n")



#案例: 把类当作装饰器, 取装饰函数, 统计函数被调用的次数
class Counter2:
	def __init__(self, func): #获取函数 func
		self.count = 0
		self.func = func

	def __call__(self, *args, **kwargs): #⚡️⚡️收集参数, 打包成元祖, 传入 func
		self.count += 1
		print(f'这是第 {self.count} 次被调用')
		return self.func(*args, **kwargs) #⚡️⚡️调用函数 func, 传入元祖并解包, 最终返回结果


@Counter2 #🔥🔥👉相当于 sayCount = Counter2(sayCount) , 相当于让 sayCount 变成了 Counter2 的实例化对象！🔥🔥🔥 所以 sayCount() 相当于 Counter2()!!!
def sayCount():
	print('hello world~')

sayCount() # 🌟🌟👆返回的 sayCount() 已经 ⚡️⚡️被掉包成了 【Counter2 的实例化对象】 所以可以直接调用！
sayCount() #🔥🔥👆相当于把 Counter2 当作函数来调用，所以会触发 __call__ 方法!
