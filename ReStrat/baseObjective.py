# 面向对象, 需要 self, 把对象的属性绑定在自身上

class ATM:
    def __init__(self, 编号, 银行, 支行):
        self.编号 = 编号
        self.银行 = 银行
        self.支行 = 支行
        
class Money:
    def __init__(self, 面值, 发行年份):
        self.面值 = 面值
        self.发行年份 = 发行年份
        
        
atm1 = ATM("001", "招商银行", "南园支行")
money1 = Money(100, 2018)





class CuteCat:
    def __init__(self, catName, catAge, catColor):
        self.catName = catName
        self.catAge = catAge
        self.catColor = catColor
        
    def speak(self):
        print("喵" * self.catAge) # 根据年龄来 喵 几次
        
cat1 = CuteCat("饭团", 3, "White")
cat1.speak()

class Student:
	def __init__(self, name, student_id):
		self.name = name
		self.student_id = student_id
		self.grades = {"语文": 0, "数学": 0, "英语": 0} # 定义字典
	
	#设置成绩
	def set_grade(self, course, grade):
		if course in self.grades:
			self.grades[course] = grade #更新字典
   
	#打印学生信息
	def print_grades(self):
		print(f"学生:{self.name} 学号:{self.student_id} 的成绩为:")
		for course in self.grades: # 🔥从字典中取出成绩
			print(f"{course}: {self.grades[course]}分")



studen1 = Student("小李", "20230303")
studen1.set_grade("语文", 100)
studen1.set_grade("数学", 99)
studen1.set_grade("英语", 98)
studen1.print_grades() #👉学生:小李 学号:20230303 的成绩为: XXX
