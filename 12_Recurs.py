# 🔥递归
# 安全的递归（1: 有限制条件， 2: 每次调用都向着限制条件前进）
def Print_Ten(i):
	if i > 0:
		print("调用了第 %d 次" % i) # % 符号用于格式化字符串，并在字符串中插入变量
		# print("调用了")
		i -= 1
		Print_Ten(i)
	
print(Print_Ten(10))


# 递归的例子: 更简便的实现斐波那契数列
def Fib(n):
	if n == 1 or n == 2:
		return 1 
	else:
		return Fib(n-1) + Fib(n-2) # 递归，自己调用自己, 

print(Fib(12)) #递归会有效率问题





# 🔥汉诺塔(递归的例子)
def HanOi(n, x, y, z):
	if n == 1:
		print(x, '-->', z) # 如果只有 1 层，则直接将金片从 x 移动到 z
	else:
		HanOi(n - 1, x, z, y) # 将 x 上的 n-1 个金片移动到 y
		print(x, '-->', z) # 将最底下的金片从 x 移动到 z
		HanOi(n - 1, y, x, z) # 将 y 上的 n-1 个金片移动到 z

Num = int(input('请输入汉诺塔金片的层数:'))
HanOi(Num, 'X', 'Y', 'Z')