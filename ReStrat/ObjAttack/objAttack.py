"""
	对象跟对象之间的关系
		1.交互关系（比如攻击）
  		2.依赖关系(附属)
    	3.关联关系（比如亲友）
		4.组合关系（比如器官、大脑、心脏）
		5.聚合关系（比如电脑跟零部件）
  		6.继承关系（比如父子）
"""
class Monster:
	role = "monster"
	
	def __init__(self, name, breed, attackLev):  # 姓名, 种类, 攻击力
		self.name = name
		self.breed = breed
		self.attackLev = attackLev # 🔥 攻击力
		self.lifeValue = 100 #生命值固定

	def bite(self, person):
		person.lifeValue -= self.attackLev  # 🔥扣除攻击人后, 人的生命值
		print(f"攻击了 {person.name}, {person.name} 扣除 {self.attackLev} 点生命值, 生命值剩余: {person.lifeValue}")
  
  
class Person:
	role = "humen"
	
	def __init__(self, name, sex, attackLev):
		self.name = name
		self.sex = sex
		self.attackLev = attackLev
		self.lifeValue = 200  # 生命值固定
		
	def attack(self, monster):
		monster.lifeValue -= self.attackLev
		print(f"攻击了 {monster.name}, {monster.name} 扣除 {self.attackLev} 点生命值, 生命值剩余: {monster.lifeValue}")
  
  
monster1 = Monster("吉米", "小怪", 10)
person1 = Person("小明", "男", 20)
monster1.bite(person1)
person1.attack(monster1)
monster1.bite(person1)
person1.attack(monster1)
