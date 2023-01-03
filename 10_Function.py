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




# 🔥全局变量直接修改值是会被覆盖，需要使用 global 关键字
x = 880
def ChangeFn():
	global x # 修改全局变量（不提倡）
	x = 999
	print(x)

ChangeFn()




# 🔥函数的嵌套
# 🍔🍔🍔嵌套函数的外层作用域具有记忆的特效！！！
def FunA():
	x = 996
	def FunB():
		x = 888 # ⚡️⚡️无法修改 FunA() 中的 x！！跟 js 不一样
		print(x ,'in fun B')
	FunB() # 调用嵌套函数
	print(x)

FunA()



# 🔥在嵌套函数中如何修改外部函数的变量！！⚡️⚡️使用 nonlocal 关键字!!
def FunA():
	x = 996
	def FunB():
		nonlocal x # 🔥🔥🔥修改外部函数的变量!!
		x = 888 
		print(x ,'in fun B')
	FunB() # 调用嵌套函数
	print(x)

FunA()




# 🔥🔥🔥利用闭包实现工厂函数（根据变量的传入改变函数的作用）
def Calculator(x):
	def CalOf(y):
		return y ** x # ⚡️表示 x 的 y 次方
	return CalOf # 最终返回的是嵌套函数的值！

square = Calculator(2) # 变成 2 次方的函数 (因为闭包逻辑，🔥 Calculator 的函数进行了闭包， x 记住了 x = 2)
cube = Calculator(3) # 变成 3 次方的函数（因为闭包逻辑，🔥 Calculator 的函数进行了闭包，x 记住了 x = 3）

print(square(2)) # 4 (2 的 2 次方), 🔥 因为 return CalOf , 所以最终执行的是 CalOf 函数函数！！ 传入的值是给到 CalOf 的 y！！
print(cube(5)) # 125 (5 的 3 次方), 🔥 因为传入的值是给到 , 所以最终执行的是 CalOf 函数函数！！ CalOf 的 y！！




# 🔥🔥🔥利用内层函数能够记住外层函数的特效，保存外层函数的值！！
def Outer():
	x = 0
	y = 0
	def Inner(x1, y1):
		nonlocal x, y # ⚡️⚡️⚡️nonlocal 用来修改外层函数的变量(⚡️⚡️否则无法修改！)
		x += x1
		y += y1
		print(F'现在, x = {x}, y = {y}')
	return Inner


move = Outer()
print(move(1, 2))
print(move(-2, 2))





# 🔥装饰器(不用修改原来的代码的前提下，给函数添加新的功能)
# 👇一般的函数（函数作为参数）
def IsFuncA():
	print('正在执行 A 函数...')

def Report(func):
	print('开始调用 A 函数...')
	func()
	print('A 函数调用结束')

Report(IsFuncA)





# 👇一般的函数（函数作为参数）, 用于计算函数的运行时间
import time 
def Time_Master(func):
	print('开始运行...')
	start = time.time()
	func() #运行函数
	stop = time.time()
	print('结束运行...')
	print(F'一共耗费了 {(stop - start):.2f}秒 ')  #保留两位小数点 -> .2f 用于将 stop - start 的值转换为带有两位小数的字符串


def Slow():
	time.sleep(2) #沉睡两秒后再运行
	print('Hey~')

Time_Master(Slow)






# 👇用装饰器(本质上是利用闭包的原理）, 实现上面的功能, 用于计算函数的运行时间
import time
def Time_Master_02(func):
	def call_func():
		print('🎉开始运行...')
		start = time.time()
		func() #运行函数
		stop = time.time()
		print('🎉结束运行...')
		print(F'🎉一共耗费了 {(stop - start):.2f}秒 ')
	return call_func

@Time_Master_02 # 👈👈👈装饰器的使用, ⚡️⚡️本质上就是去调用 call_func() 这个内部函数函数！

def Slow_02():
	time.sleep(2) #沉睡两秒后再运行
	print('😄Hey~')

Slow_02() # 👈👈👈装饰器的使用



# 🔥装饰器的调用顺序
def Add(func): # 最后执行
	def inner():
		x = func()
		return x +1
	return inner

def Cube(func): # 第二个执行
	def inner():
		x = func()
		return x ** 3
	return inner

def Square(func): # 第一个执行
	def inner():
		x = func()
		return x ** 2
	return inner

@Add
@Cube
@Square
def Result():  #⚡️⚡️相当于把 Result 丢到了 Square、Cube、Add 函数函数里面 的 inner 去作为参数(因为返回的是 inner)！！
	return 2

print(Result()) # 65   ->   (2 ** 2 + 1) ** 3






# 🔥如何给装饰器传递参数？
import time
def Longger(msg):
	def Time_Master(func):
		def Call_Func():
			start = time.time()
			func()
			stop = time.time()
			print(F"[{msg}] 一共耗费了 {(stop - start):.2f}")
		return Call_Func
	return Time_Master

@Longger(msg = '👍')
def FunA(): #⚡️⚡️相当于把 FunA 丢到了 Time_Master 函数函数里面去作为参数！！因为返回的是 return Time_Master
	time.sleep(1)
	print('正在调用 A 函数...')


@Longger(msg = '👎')
def FunB(): #⚡️⚡️相当于把 FunB 丢到了 Time_Master 函数函数里面去作为参数！！因为返回的是 return Time_Master
	time.sleep(1)
	print('正在调用 B 函数...')

FunA()
FunB()



