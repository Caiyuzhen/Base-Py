# coding=utf-8

# 🔥input 用于跟用户进行交互, 能够获取用户输入的内容，赋值给变量 temp
temp = input("猜猜我心里想的是哪个数字:")
guess = int(temp) # 🔥int() 函数用于将一个字符串或数字转换为整型

if guess == 8:
	print("🎉猜对了！")
	print("猜中了也没奖励！")
else:
	print("猜错了，我心里想的是 8 !")
	print("游戏结束，不玩啦 ^_^ ")