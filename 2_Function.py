# 🔥input 用于跟用户进行交互, 能够获取用户输入的内容，赋值给变量 zen
zen = input("猜猜我叫什么名字？")
print(zen)



# 🔥int 用于把字符串转换成整数(数字)
ab = input("请输入一个数字：")
cc = int(ab)
print(cc)



# 🔥条件分支语句、比较运算符
if(cc > 10):
	print("大于 10 了，好贵！")



# 🔥条件分支语句
temp2 = input("输入一个数字")
guess = int(temp2)

if guess == 8:
	print("🎉 猜对了！")
else:
	if(guess < 8):
		print("小了")
	else:
		print("大了")



# 🔥循环语句 white XXX 只要条件成立就会一直去循环
counts = 3
while (counts > 0):
	print("这是一个大于 3 的数字") # 打印 3 次
	counts = counts - 1



# 🔥导入模块（比如导入生成随机数的方法）
import random
Myresult = random.randint(1, 10) # 生成 1 到 10 之间的随机数
print(Myresult)