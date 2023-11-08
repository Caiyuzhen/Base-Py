# 闭包: 函数 A 内再定义函数 B, 并且函数 B 调用了函数 A 的参数, 那么函数 B 就是闭包
def set_func(func):
    def call_func(*args, **kwargs):
        print("第一: 调用装饰器后, 先执行这个闭包函数内的代码")
        return func(*args, **kwargs)
    
    return call_func


# 使用装饰器, 在函数执行之前先调用装饰器的函数
@set_func 
def a(x):
    print("第二: 执行这个")
    return x

res = a(10)
print(res)




# 🌟用 装饰器把 url 跟 函数 对应上！ 🌟____________________________________________________________________
URL_ROUTE = dict()

def route(yy): # 传入 index.py
    def set_func(func): # 🔥 func 指向原函数 => 调用这个装饰器的 bb() 函数, 印象下方 return 了函数
        URL_ROUTE[yy] = func # 🌟 在这一步把 URL_ROUTE['/index.py'] 对应为 aa() 函数 🌟
        def call_func(*args, **kwargs):
            print("第一: 调用装饰器后, 先执行这个闭包函数内的代码")
            return func(*args, **kwargs)
        return call_func
    return set_func # 此时 aa = setfunc(x)




@route('/index.py') # 当用户访问 /index.py 时, 调用 aa(x) => 实际是调用 call_func
def aa(x): # 🔥 使用装饰器后, bb() 指向上方装饰器的 call_func
	print("第二: 执行这个")
	return x


@route('/register.py') # 当用户访问 /register.py 时, 调用 bb(x) => 实际是调用 call_func
def bb(x): # 🔥 使用装饰器后, bb() 指向上方装饰器的 call_func
	print("第二: 执行这个")
	return x


print(URL_ROUTE) # => 使用装饰器装饰后, 最终输出 '/index.py': func()  =>  字符串 + 函数的字典形式
res2 = bb()
print(res2)