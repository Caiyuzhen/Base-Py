import time
# from middlewares.log_middleware import log_middlewareFn



# 👇定义用来存储 URL 以及 func() 对应关系的字典 ————————————————————————————————————————————————————————————————————————
URL_ROUTE = dict()

# 🚀 装饰器, 用来把 【url】 跟 【函数】的映射关系对应上
def route(url):  # url => "/login.py"
	def set_func(func): # func => 函数名
		URL_ROUTE[url] = func # 将 url 与 func 映射起来 => # 🌟 在这一步把 URL_ROUTE['/index.py'] 对应为 login() 函数 🌟
		def call_func(*args, **kwargs): # 收集 func 函数的所有参数, 并返回 func 函数!
			return func(*args, **kwargs)
		return call_func
	return set_func # 此时 login(x) = setfunc(x)




# 👇👇👇 在这里边进行数据库的查询 （比如 mySQL)!!! ————————————————————————————————————————————————————————————————————————
@route("/login.py")
def login():
	response_body = "⏰ 登录页面, 当前时间是: %s" % time.ctime()
	return response_body

@route("/register.py")
def register():
	response_body = "✏️ 注册页面"
	return response_body

@route("/detail.py")
def detail():
	response_body = "🛍️ 详情页"
	return response_body

@route("404")
def wrong_404():
	response_body = "❌ 404 页面不存在"
	return response_body
	
 
 
 
# 👇 统一返回页面
# 👇 1. 定义字典来将【路由】【函数】一一映射起来 ————————————————————————————————————————————————————————————————————————
# URL_ROUTE = { # 纯大写、全局变量
# 	"/login.py": login, # http://localhost:8080/login
#  	"/register.py": register, # http://localhost:8080/register
# 	"/detail.py": detail,
# 	"404": wrong_404
# }



# 👇 把数据返回给服务器 ————————————————————————————————————————————————————————————————————————
def application(env, call_func): # env 保存了请求 path 
	# 🔥回调(🚀返回页面), 执行 http_server,py 内的 set_status_headers 函数 !! 并且将状态码传递过去
	call_func("200 OK", [("Content-Type", "text/html; charset=utf-8"), ("Framework", "mini-web")]) # 🚀列表套元组(元组是不可变的, 一旦创建其元素便不能被修改), Content-Type 表示键, text/html; charset=utf-8 表示值
 
	# if env['PATH_INFO'] == '/login.py':
	# 	return login()
	# elif env['PATH_INFO'] == "/detail.py":
	# 	return detail()
	# elif env['PATH_INFO'] == "/register.py":
	# 	return register()
	# else:
	# 	return wrong_404()

	# 🔥 2. 根据字典定义的路由, 来调用不同的函数
	file_path = env['PATH_INFO'] # 获取请求的 path 
	# if file_path.endswith('.py'):
	# 	file_path = file_path[:-3]  # 去掉 '.py' 后缀
     
	# func = URL_ROUTE[file_path] # [🔥字典中自带了 get 方法, 使用 get 方法更加保险, 不会让程序崩溃！]
	func = URL_ROUTE.get(file_path) # [🔥字典中自带了 get 方法, 使用 get 方法更加保险, 不会让程序崩溃！]
	if not func: # 🔥如果没有找到 url => 在字典中没有找到对应的映射
		URL_ROUTE.get("404", lambda: "not found page 404") # 表示如果没有 404 页面, 则进行兜底
		
 
	# 🔥 3. 调用函数的引用
	response_body =  func()
 
	# 🔥 4. 返回数据给到 web 服务器
	return response_body

