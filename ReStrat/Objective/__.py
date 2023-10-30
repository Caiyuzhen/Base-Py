"""
	类的双下划线方法(内置方法)
 
		__len__ 返回整数 (没啥用)
	
		__item__ 把一个对象转化成一个字典, 并赋予增删改查方法
  
		__repr__  把对象改为字符串格式来展示  (返回的必须是字符串才能用！否则会报错！)
		__str__  把对象改为字符串格式来展示
  
		__del__ 析构方法, 在对象消失时会执行  (最后执行)
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






        




