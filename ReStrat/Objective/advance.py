"""
	类方法
		类方法通过【@classmethod】装饰器实现, 和普通的方法区别是【类方法只能访问类变量, 不能访问实例变量】
	静态方法
"""
# 类方法
class Dog:
	name2 = "小黑" # 类变量
	
	def __init__(self, name):
		self.name = name
		
	@classmethod # 🔥🔥加了这个属性后, 传入的 cls 就不是【类的实例】了, 而是【类本身】!! 因此只能访问到【类】身上的成员变量! 因为传进来的不是实例!
	def eat(cls):
		print(f"{cls.name2} 正在吃饭") #👈不会报错, 因为可以访问类变量！
		# print(f"{self.name} 正在吃饭") #👈会报错, 因为无法访问实例属性!

dog1 = Dog("旺财")
dog1.eat()



print("————————————")


# 类方法的场景 => 比如【共享数据】=> 统计总数
# HOW？ 通过类方法来约束只能【类本身】才能够修改私有变量!! =>  一个类创建了一个实例才去修改类的私有属性, 比如统计总数 !!
class Student:
	__count = 0
 
	def __init__(self, name):
		self.name = name
		self.addNum(self) # 🚀 在初始化时, 调用增加学生的方法, 这样外部就不能够够随意的修改总数了! 【传入 self】来判断是否真正生成了实例！
		print(f"{self.name} 正在初始化")
		
	@classmethod
	def addNum(cls, obj): # 🚀 obj 是传入的实例, 用来判断是否真正生成了 Student 实例！
		if obj.name: # 🔥 只有实例有 name !!
			cls.__count += 1
			print(f"学生总数: {cls.__count}")
  
		
s1 = Student("小明")
s2 = Student("小红")
# print(Student)



print("————————————")


