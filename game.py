# python 小游戏
temp = input("猜猜我心里想的是哪个数字:")
guess = int(temp)

if guess == 8:
	print("🎉猜对了！")
	print("猜中了也没奖励！")
else:
	print("猜错了，我心里想的是 8 !")
	print("游戏结束，不玩啦 ^_^ ")