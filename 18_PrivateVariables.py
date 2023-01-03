# 🔥"私有变量", Python 没有那种只有在类里边才能访问的便利
# 🔥🔥用两个 __ 来定义私有变量！
# _XXX 变量一般是内部的，不建议修改的  XXX_ 结尾的变量一般是系统变量，不建议修改的
class A:
	def __init__(self, x):
		self.__xxy = x

	def set_x(self, x):
		self.__xxy = x  # 修改私有变量 x 的值

	def get_x(self):
		print(self.__xxy)  # 修改私有变量 x 的值

a = A(150)
# print(a.__xxy) # 会报错！因为 __xxy 是私有变量，只能通过外露的 set 跟 get 方法来访问！
a.get_x()



# 🔥存放构造函数的位置在字典内
print(a.__dict__)
a.__dict__['name'] = 'zen' # ⚡️在构造函数内添加一个属性
print(a.name)



