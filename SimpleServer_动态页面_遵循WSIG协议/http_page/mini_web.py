import time

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
def application(env, call_func):
	# 🔥回调(🚀返回页面), 执行 http_server,py 内的 set_status_headers 函数 !! 并且将状态码传递过去
	call_func("200 OK", [("Content-Type", "text/html; charset=utf-8"), ("Framework", "mini-web")]) # 🚀列表套元组(元组是不可变的, 一旦创建其元素便不能被修改), Content-Type 表示键, text/html; charset=utf-8 表示值
	if env['PATH_INFO'] == '/login.py':
		return login()
	elif env['PATH_INFO'] == "/detail.py":
		return detail()
	elif env['PATH_INFO'] == "/register.py":
		return register()
	else:
		return wrong_404()
    
	# if file_name == '/login.py':
	# 	return login()
	# elif file_name == "/detail.py":
	# 	return detail()
	# elif file_name == "/register.py":
	# 	return register()
	# else:
	# 	return wrong_404()