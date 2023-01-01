# 🔥高阶函数

# 需要导入 funtoolss 模块, 该模块提供了一些高阶函数
import functools #⚡️⚡️记得导入！

def Add(x, y):
	return x + y

res = functools.reduce(Add, [1, 2, 3, 4, 5]) # ⚡️⚡️Reduce 的作用是接收【函数】和【可迭代对象】作为参数，将【函数】作用在【可迭代对象】的每个元素上，然后返回一个结果
print(res)



# 不用 reduce 的话，可以这样写
def Cal():
	sum = 0
	for i in [1, 2, 3, 4, 5]:
		# 结果相加
		sum += i
	return sum

print(Cal())




# 用 reduce 计算 10 的阶乘
functools.reduce(lambda x, y : x * y, range(1, 11))




# 🔥偏函数 partial , 把函数拆分为多个参数进行返回 (底层是类似之前闭包的方式)
square = functools.partial(pow, exp = 2) # pow 计算数字的幂
square(2) # 4




