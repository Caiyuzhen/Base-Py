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
	i += 1
	
print(sum)



