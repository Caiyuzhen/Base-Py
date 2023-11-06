import time
# from middlewares.log_middleware import log_middlewareFn



# 👇👇👇 在这里边进行数据库的查询 （比如 mySQL)!!!
def login():
	response_body = "⏰ 登录页面, 当前时间是: %s" % time.ctime()
	return response_body

def register():
	response_body = "✏️ 注册页面"
	return response_body

def detail():
	response_body = "🛍️ 详情页"
	return response_body

def wrong_404():
	response_body = "❌ 404 页面不存在"
	return response_body
	
 
# 👇 统一返回页面
# 👇 1. 定义字典来将【路由】【函数】一一映射起来
URL_ROUTE = { # 纯大写、全局变量
	"/login.py": login, # http://localhost:8080/login
 	"/register.py": register, # http://localhost:8080/register
	"/detail.py": detail,
	"404": wrong_404
}

# 👇 把数据返回给服务器
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
     
	func = URL_ROUTE[file_path]
 
	# 🔥 3. 调用函数的引用
	response_body =  func()
 
	# 🔥 4. 返回数据给到 web 服务器
	return response_body

