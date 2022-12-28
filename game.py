# coding=utf-8
import random


count = 3
Myresult = random.randint(1, 10) # 生成 1 到 10 之间的随机数
print(Myresult)

while count > 0:
	temp = input("猜猜我心里想的是哪个数字:") # input 能够获取用户输入的内容，然后赋值给变量 temp
	result = int(temp) # 将一个字符串或数字转换为数字

	if result == Myresult:
		print("🎉 猜对了！")
		break # 跳出循环体
	else:
		if(result < Myresult):
			print("小了")
		else:
			print("大了")

		count = count - 1  # 大了小了都要减一次机会（注意缩进问题！）
print("💣 游戏结束")





