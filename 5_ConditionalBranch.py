# 🔥条件分支语句 ————————————————————————————————————————————————————————————
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





# 🔥两种条件循环语句，一种是 for，另一种是 while 用 break 退出循环 ————————————————————————————————————————————————————————————
# 一: while 循环
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



# 例子
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
		break # ⚡️⚡️⚡️break 的场景只要有一次跳出了，就不会执行下面的 else 语句，于是坚持失败！
	day += 1
else:
	print("你已经坚持了一周了，加油！")



# 例子: 99 乘法表, k 代表行，j 代表列
# k = 1 
# while k <= 9:
# 	j = 1
# 	while j <= k:
# 		print(j, "*", k, "=", j * k, end=" ")
# 		j += 1
# 	print() # 换行
# 	i += 1




# 例子: 每天学习的时长 8 小时，一周学习 7 天
dayy = 1
hourr = 1
while dayy <= 7:
	while hourr < 8:
		hourr += 1  # 大于一个小时就放弃了
		if hourr >= 1:
			print("你已经学习了", hourr, "小时了，放弃吧")
			break # ⚡️⚡️⚡️break 每次只跳出一层循环体！所以 dayy 还能 +1, 所以会打印 7 次！
	dayy += 1





# 二: for 循环
for each in "饭团很爱吃饭团":
	print(each) # 饭 团 很 爱 吃 饭 团 (每个字符都会打印出来)


# 如何用 while 实现上面的语句? len 能够获取一个对象的长度
p = 0
while p < len("饭团很爱吃饭团"):
	print("饭团很爱吃饭团"[p])
	p += 1



# 用 range() 函数，能够生成一个数字序列, 里边可以传入 （stop) 或 (start, stop) 或（start, stop, step） 几个参数
for a in range(11): #不包含 11, 默认为每次 +1
	print(a)


for aa in range(0, 11): #0~10, 默认为每次 +1
	print(aa)


for aaa in range(0, 11, 2): #每次 +2
	print(aaa)



# 例子: 计算 1 加到 100
summ = 0
for n in range(101):
	summ += n # 结果为 5050




# 例子: 找出 10 以内的素数 (除了 1 以外, 无法被其他自然数整除)
for yy in range(2, 10):
	for xx in range(2, yy):
		if yy % xx == 0: # 有余数，说明不是素数，没有余数说明能够被整除
			print(yy, '=', xx, '*', yy // xx)
			break
	else:
		print(yy, '是素数')