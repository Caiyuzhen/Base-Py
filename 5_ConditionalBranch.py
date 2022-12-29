# 🔥条件分支语句
if("饭团" == "嘟嘟"):
	print("饭团是嘟嘟")
else:
	print("饭团不是嘟嘟")



cul = input("请输入你的成绩：")
result = int(cul)

if(result < 60):
	print("差")
elif(result > 60 and result < 80):
	print("中等")
elif(result > 80 and result < 90):
	print("良好")
else:
	print("优秀")




# 🔥另一种条件分支的写法（表达式）, 成立要做什么 if XXX else 不成立要做什么
age = 17
print("抱歉你还不能访问") if age < 24 else print("欢迎访问")





# 🔥条件循环语句， 用 break 退出循环
i = 1
sum = 0
while i <= 100:
	sum += i
	i += 1 # i = i + 1
print(sum) # 5050




# 🔥 continue 跳过本次循环，继续下一次循环
ii = 0 
while ii < 10:
	ii += 1
	if ii % 2 == 0: # 取模运算，求余数，当没有余数时，说明是偶数
		continue
	print(ii) # 1 3 5 7 9



# 🔥 while 循环
iii = 0
while iii < 5:
	print("循环内, 值为:", iii)
	if(iii == 2):
		break # 有 break 的话，会结束整个循环，不会执行 else 语句
	iii += 1
else: 
	print("循环结束")



# 例子: 坚持一周学习
day = 1
while day <= 7:
	answer = input("今天有好好学习吗？")
	if answer != "有":
		print("你还是好好学习吧")
		break
	day += 1
else:
	print("你已经坚持了一周了，加油！")



