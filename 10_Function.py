#函数
# 🔥创建函数
def myfunc():
	pass #空语句, 一般用于占位符后续才实现


# 🔥函数的参数(默认就是位置参数)
def NewYear(year, count):
	for i in range(count): # 次数
		print(F"Happy New Year {year}!")

NewYear(2023, 6)





# 🔥关键字参数
def Msg(a="Hellow", b="World"):
	return "".join((b, a))

print(Msg())





# 🔥默认参数(⚡️⚡️默认参数需要放在最后！！不然会报错)
def Food(jam, bread="面包"):
	return "".join((jam, 'with', bread))

print(Food("草莓", "馒头"))




# 🔥函数的返回值
def Division(x, y):
	if y == 0:
		return "除数不能为 0!"
	else:
		z = x / y
		return z

print(Division(10, 2))




# / 左边不支持关键字参数, 右侧支持
def Sum(a, /, b):
	return a + b

# Sum(a=1, 2) # 将会报错




# 🔥收集参数（可多可少）
def Coll(*args):
	print("有{}个参数".format(len(args))) # len(args) 表示获取参数的长度
	return args# 最终将返回一个元组，可以进行解包


Coll("你", "好", "吗", "?")
a,b,c,d = Coll("你", "好", "吗", "?") # 对返回的元组进行解包
print(a, b, c, d)



def Collect(*args, a, b):
	print(*args)

Collect(1, 2, 3, a = 4, b = 5) #🔥收集参数如果放前面的话，后面的参数就需要用关键字参数传递！！！





# 🔥收集为字典
def CollectDict(**kwargs): ## 🔥** 表示收集为字典
	print(kwargs)

CollectDict(a = 1, b = 2, c = 3) # ⚡️要收集为字典的话，需要用关键字参数的形式传递！！！





# 🔥把元组解包再传入函数内
t = (1, 2, 3, 4)
def BestFn(a, b, c, d):
	print(a, b, c, d)

BestFn(*t) # ⚡️把元组解包再传入函数内





# 🔥把字典解包为关键字参数再传入函数内
d = {"a": 1, "b": 2, "c": 3}
def BestFn2(a, b, c):
	print(a, b, c)

BestFn2(**d) # ⚡️把字典解包为关键字参数再传入函数内


