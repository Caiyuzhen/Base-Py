"""
	类的双下划线方法(内置方法)
 
		__len__ 返回整数 (没啥用)
	
		__item__ 把一个对象转化成一个字典, 并赋予增删改查方法
  
		__repr__  把对象改为字符串格式来展示  (返回的必须是字符串才能用！否则会报错！)
		__str__  把对象改为字符串格式来展示
  
		__del__ 析构方法, 在对象消失时会执行  (最后执行)
  
		__new__ 会在 init 方法之前执行(注意, 写了 new 后需要手动调用 init !!), 可以用来做【单实例】
  
		__call__ 像调用函数一样去调用一个对象, 利用 __call__ 方法可以在类被调用时, 就会自动触发
  
		type 是所有类的宗师, 可以用来动态的创建类
  
		isinstance(obj, cls) 判断一个对象是否是一个类的实例
  
		issubclass(sub, super) 判断某个类是否是另一个类的子类
"""



print("__len__ 方法 ————————————————————————————————————————————————————")


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def __len__(self):
		print("触发了__len__方法")
		return 2

p = Person("Jimmy", 30)
print(len(p))




print("__item__ 方法, 👍 很好用, 用字典来收集参数 ————————————————————————————————————————————————————")


class Brand:
	def __init__(self, name, area):
		self.name = name
		self.area = area

	def __getitem__(self, item):
		print("获取 KEY", item)
		print("收集参数成为字典：",  self.__dict__) # 👈🔥 当前类的所有属性 name、area 都存在 self.__dict__ 中
		print(self.__dict__[item]) #从字典中取值

	def __setitem__(self, key, value):
		print("设置一个 KEY ...", key)
		self.__dict__[key] = value

	def __delitem__(self, key):
		print("删除某个 KEY", key)
		self.__dict__.pop(key)


b = Brand("品牌 A", "亚洲")  # 参数收集为： {'name': '品牌 A', 'area': '亚洲'}
b["name"] # 🔥设置为字典后, 可以通过字典的方式获取 name
b["area"] # 🔥设置为字典后, 通过字典的方式获取 area
b["area"] = "Europe"
b["area"] 
del b["area"] # 删除字典中的某个属性




print("__repr__  |  __str__  方法, 👍 在打印对象实例时, 可以让属性以字符串的形式进行展示 (返回的必须是字符串才能用！否则会报错！) ————————————————————————————————————————————————————")

class School:
	def __init__(self, name, address, type):
		self.name = name
		self.address = address
		self.type = type
		
	def __repr__(self):
		return (f"repr 处理后的属性: {self.name}, {self.address}, {self.type}")

	def __str__(self):
		return (f"str 处理后的属性: {self.name}, {self.address}, {self.type}")


s1 = School("学校 A", "ShangHai", "公立")
print(s1)

s2 = School("School B", "ShenZhen", "私立")
print(str(s2))





print("__del__ 方法, 👍  析构方法, 在对象消失时会执行 (最后执行) ————————————————————————————————————————————————————")
class Sweet:
	def __init__(self, name):
		self.name = name
		
	def __del__(self):
		print("对象被移除了..执行了析构方法...")
  
sun1 = Sweet("honey")






print("__new__ 方法, 会在 init 方法之前执行(注意, 写了 new 后需要手动调用 init !!), 可以用来做【单实例】————————————————————————————————————————————————————")
# 🌟 基本逻辑（在 __init__ 之前执行）
class SuperCat:
	def __init__(self, name):
		self.name = name
		print("第二执行")
	
	def __new__(cls, *args, **kwargs):
		print(cls, args, kwargs, "第一执行")
		return object.__new__(cls) # 写了 new 后需要手动调用 init !! 🚀 需要 return 一下！
	
superCat = SuperCat("超级猫")


# 🌟 单实例的方式 (比如系统的设置面板或者是打印机, 调用后从不同的位置只会打开同一个设置面板跟打印机, 而不会打开多个)
class Printer:
	tasks = [] # 🔥 用于存放任务, 任务会共享, 但是实例是单独的, 🚀 内存地址不一样
	hasInstance = None # 🔥 存放第一次实例化的对象
	
	def __init__(self, name) -> str:
		self.name = name
		
	def add_task(self, job) -> None:
		self.tasks.append(job)
		print(f"添加了一条新任务 {self.name} {job}, 总任务数量: {len(self.tasks)}")
	
	def __new__(cls, *args, **kwargs): # 只有第一次实例化时才执行, 🚀 cls 是类对象的引用,  用来进行实例化或者获取里边的参数!
		if cls.hasInstance is None:
			# 🚀🚀 如果还没有实例化, 就进行实例化, 并把实例化后的对象存在 cls.hasInstance 里边
			obj = object.__new__(cls)  # 实例化一个对象, 🚀 cls 是类对象的引用,  用来进行实例化或者获取里边的参数!
			print("obj", obj)
			cls.hasInstance = obj
		return cls.hasInstance # 🚀🚀 如果已经进行了实例化, 则返回上一次的实例
        
	 
		 
p1 = Printer("Word app")
p2 = Printer("Excel app")
p3 = Printer("Pdf app")

p1.add_task("文档文件 1")
p2.add_task("Exlce 文件 1")
p3.add_task("pdf 文件 1")

print(p1, p2, p3) # 🚀 进行单实例后, 打印出的内存地址就都一样了





print("__new__ 方法, 像调用函数一样去调用一个对象, 利用 __call__ 方法可以在类被调用时, 就会自动触发 ————————————————————————————————————————————————————")
class Water:
	def __init__(self, nameNum):
		self.nameNum = nameNum
		
	def __call__(self, num, *args, **kwargs) -> int:
		print(f"获得乘法的结果: {self.nameNum * num}")
		return self.nameNum * num
  
w = Water(99)
print(w(666))




print("用 type 动态的创建一个类 ————————————————————————————————————————————————————")
class Animals:
    def __init__(self, name):
        self.name = name
        
cuteCat = Animals("嘟嘟")

def __init__(self, name):
    self.name = name
CatClass = type("Animals", (object,), {"role" : "cat", "__init__" : __init__}) # 🔥放入字典, role 为类属性, __init__ 为类方法
cuteCat2 = CatClass("饭团")
print(cuteCat2.role)




print("用 ininstance 判断一个对象是不是一个类的实例 ————————————————————————————————————————————————————")
class Foo():
    pass

obj = Foo
instance(obj, Foo)




print("用 issubclass 判断某个类是否是另一个类的子类 ————————————————————————————————————————————————————")
class Foo2:
    pass

class Bar(Foo2):
    pass

issubclass(Bar, Foo2)
    

    




        




