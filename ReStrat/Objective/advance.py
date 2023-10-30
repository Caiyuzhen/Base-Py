"""
	类方法 (少用)
		类方法通过【@classmethod】装饰器实现, 和普通的方法区别是【类方法只能访问类变量跟方法, 不能访问实例变量跟方法】
  
	静态方法 (超少用)
		静态方法方法通过【@classmethod】装饰器实现, 【静态方法】让实例不会自动传入 self, 所以让【实例】跟【类】的关系隔离开, 除非手动传入【类】
  
	属性方法
		把一个方法变成一个静态的属性（或变量）
  
	反射
		可以通过【字符串】的形式来操作对象的属性
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


# 【属性方法】, 好处是方法被调用后可以执行一系列的动作 
print("属性方法 Property ————————————")
class Student3:
	def __init__(self, name):
		self.name = name

	@property # 🔥🔥🔥 把一个方法变成一个静态的属性（或变量）
	def fly(self):
		return f"{self.name} is flying..."

s4 = Student3("小李")
print(s4.fly) # 👈👈👈 直接调用方法, 就像【调用属性】一样, 不需要加括号!


# 【属性方法】的实际场景(比如去哪儿网站： 1.连接网站 2.查询信息 3.返回数据并解析数据 4.显示给用户  最终返回给用户的也是几个数据)
class Flight:
	def __init__(self, name):
		self.flightName = name

	def checkingStatus(self):
		print("connecting airline company api...")
		print(f"checking flight status {self.flightName}")
		return 200 # 最终返回的飞机状态 （moke 为 200, 也可能收 100\0 等下面枚举的状态)

	@property
	def flightStatus(self):
		status = self.checkingStatus() # 解析返回的状态
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





# 反射 (比如对象不是自己创建的, 但又想改里边的属性, 此时需要先判断一下)
print("反射 ————————————")

"""
	反射的四种方法
		hasattr(obj, "str")  #判断
		getattr(obj, "str")  #获取
		setattr(obj, "str")  #设置
  		delattr(obj, "str")  #删除
    
	反射的应用场景
		🌟 比如根据用户的键盘输入调用对应的方法, 这样就不会报错
"""

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def walk(self):
		print("正在跑")
		
p = Person("Kim", 25)




if hasattr(p, "name"): # 判断 => 通过【反射方法】判断对象里边是否有某个属性
    print("该对象里边有 name 属性")

a = getattr(p, "name") # 获取 => 通过【反射方法】获取对象内的属性
print(a)

setattr(p, "sex", "Female") # 设置 => 通过【反射方法】增加对象内的【属性】
print(p.sex) 

delattr(p, "age") # 删除 => 通过【反射方法】删除对象内的【属性】

def talk(self):
    print(self.name, "is speaking~")
    
# setattr(p, "talkFn", talk) # 设置（设置实例） => 通过【反射方法】增加对象内的【方法】
# p.talkFn(p) # ⚡️ 给【实例】设置反射方法 => 需要自己传入 p => self !

setattr(Person, "talkFn", talk) # 设置（设置对象） => 通过【反射方法】增加对象内的【方法】
p.talkFn() # ⚡️ 给【实例】设置反射方法 => 不需要自己传入 p => self ! 【🔥一般都是这么绑定！不然还得自己传入 self !!】



# 🌟 根据用户输入的字符串属性调用方法
user_command = input("🌟 请输入你要调用的对象方法>>:").strip() #strip() 用于去除字符串两端的指定字符（默认为空格）
if hasattr(p, user_command):
    func = getattr(p, user_command) # 🔥定义一个函数
    func()
else:
	print("该对象里边没有这个属性")
 
 
 
# 🔥🔥 通过反射来判断指定【文件】下的【字符串属性】
"""
	__name__ 以字符串的形式代表模块本身,跟 __init__ 不同的是, __init__ 代表了一个对象, 能够调用方法
 	__name__ 在当前文件下主动执行时就是 模块本身, 在被其他模块导入执行的情况下, 就等于模块名
 """
 





    
    

