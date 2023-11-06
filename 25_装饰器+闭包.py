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



# 🔥用装饰器把 url 跟 函数 对应上！____________________________________________________________________
URL_ROUTE = dict()

def xxx(yy): # 传入 index.py
    def set_func(func):
        URL_ROUTE[yy] = func
        def call_func(*args, **kwargs):
            print("第一: 调用装饰器后, 先执行这个闭包函数内的代码")
            return zz(*args, **kwargs)
        return call_func
    return set_func


@xxx('/index.py')
def bb(x):
	print("第二: 执行这个")
	return x

res2 = bb()
print(res2)