# 🔥Lambda 表达式（匿名函数, 可以不定义函数名）, 用于简化代码, 一般用于简单的需求！
# 传统例子: 计算参数的平方
def SquareX(x):
	return x * x

print(SquareX(3))


# Lambda 例子: 计算参数的平方
SquareY = lambda y : y * y
print(SquareY(3))



# ⚡️Lambda 表达式例子: 把每个数字 + 1 再返回
Mapped = list(map(lambda X : X + 1, [996])) # 996要放入列表！！才能是可迭代对象！! list() 用于将可迭代对象（例如字符串、元组、迭代器）转换为列表
print(Mapped)



# ⚡️Lambda 表达式例子: 求 10 以内的奇数
Filtered = list(filter(lambda Y : Y % 2, range(10)))
print(Filtered)




# 🔥生成器(⚡️每次被调用都会提供一个数据)
def Counter():
	i = 0
	while i <= 5:
		yield i # ⚡️⚡️⚡️创建生成器方法一, 每次被调用都会提供一个数据!!跟列表还有元组不一样，⚡️它们是早已准备好的数据！
		i += 1 # 下次调用就从这里开始!!

for i in Counter():
	print(i)


Res = Counter() # 生成器, 相当于一个特殊的迭代器, !!⚡️无法使用下标索引
print(next(Res)) #0
print(next(Res)) #1
print(next(Res)) #2
print(next(Res)) #3


# ⚡️生成器例子: 斐波那契数列
def Fibonacci():
	a, b = 0, 1
	while a <= 200:
		yield a
		a, b = b, a + b # a = b,   b = a + b

Result = Fibonacci()

print(next(Result))
print(next(Result))
print(next(Result))
print(next(Result))
print(next(Result))
print(next(Result))
print(next(Result))
print(next(Result))

for i in Result: # 生成斐波那契数列，到 200 就停止了
	print(i)




# 🔥生成器表达式（列表有推导式，元组没有, 因为元组会生成一个生成器对象）
# ⚡️⚡️生成器表达式每次调用返回一个值，⚡️⚡️列表推导式会一下子将所有数据一次性返回！
# 例子: 计算 0 ~ 9 之间元素的平方值
T = (i ** 2 for i in range(10) ) # ⚡️⚡️⚡️创建生成器方法二
print(next(T))
print(next(T))
print(next(T))
print(next(T))
print(next(T))