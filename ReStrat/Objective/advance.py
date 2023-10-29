"""
	类方法 (少用)
		类方法通过【@classmethod】装饰器实现, 和普通的方法区别是【类方法只能访问类变量跟方法, 不能访问实例变量跟方法】
  
	静态方法 (超少用)
		静态方法方法通过【@classmethod】装饰器实现, 【静态方法】让实例不会自动传入 self, 所以让【实例】跟【类】的关系隔离开, 除非手动传入【类】
  
	属性方法
		把一个方法变成一个静态的属性（或变量）
"""


# 类方法
print("类方法基础————————————")
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





print("类方法场景————————————")
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






# 静态方法
print("静态方法 ————————————")
class Student2:
	role = "Stu"
	
	def __init__(self, name):
		self.name = name
		
	@staticmethod # 🔥🔥 静态方法的修饰器是 @staticmethod, 让实例无法访问这个方法, 除非手动传入【类】
	def fly(self):
		print(f"{self.name} is flying") # 👈会报错, 因为不能访问!
  
s3 = Student2("小王")
s3.fly(s3) # 🔥要手动的传入 self 也就是 s3 !!!


# 属性方法, 好处是方法被调用后可以执行一系列的动作 
print("属性方法 Property ————————————")
class Student3:
	def __init__(self, name):
		self.name = name

	@property # 🔥🔥🔥 把一个方法变成一个静态的属性（或变量）
	def fly(self):
		return f"{self.name} is flying..."

s4 = Student3("小李")
print(s4.fly) # 👈👈👈 直接调用方法, 就像【调用属性】一样, 不需要加括号!


# 属性方法的实际场景(比如去哪儿网站： 1.连接网站 2.查询信息 3.返回数据并解析数据 4.显示给用户  最终返回给用户的也是几个数据)
class Flight:
	def __init__(self, name):
		self.flightName = name

	def checkingStatus(self):
		print("connecting airline company api...")
		print(f"checking flight status {self.flightName}")
		return 200

	@property
	def flightStatus(self):
		status = self.checkingStatus()
		if status == 0:
			print("📅 flight got canceled")
		elif status == 100:
			print("⏰ flight is on time")
		elif status == 200:
			print("✈️ flight has departured already...")
		else:
			print("❌ Can not confirm the flight status, please check later")
	
f = Flight("CA999") # 用户输入航班信息
f.flightStatus # 用户查询航班信息

