import re
import time
from contextlib import contextmanager # 🔥 上下文管理器装饰器（可以用来补充路径）
import pymysql # 🔥操作数据库的包 pip3 install pymysql  ｜ 🔥记得安装 pip install cryptography 包用来认证并连接数据库 => 国内可以用清华镜像 pip install cryptography -i https://pypi.tuna.tsinghua.edu.cn/simple
# from middlewares.log_middleware import log_middlewareFn 




# 👇定义用来存储 URL 以及 func() 对应关系的字典 ————————————————————————————————————————————————————————————————————————
URL_ROUTE = dict()


# 👇打开文件更好的方式, 让下方 with open 时不用传入 views/template 这一串路径 ————————————————————————————————————————————————————————————————————————
TEMPLATES_PATH = "views/templates" # 🚀 用来存储模板文件的路径, 以便后续使用
@contextmanager
def mini_open_static(file_path, model): # 传入上下文管理器的装饰器, 补充 views/templates 这个路径
    f = open(TEMPLATES_PATH + file_path, model)
    yield f # 🔥🔥 yield 执行到这里回西安暂停一下, 然后下去执行  content = f.read() # 读取文件内容, 然后再回来执行 f.close()
    f.close()




# 🚀 装饰器, 用来把 【url】 跟 【函数】的映射关系对应上
def route(url):  # url => "/login.html"
	def set_func(func): # func => 函数名
		URL_ROUTE[url] = func # 将 url 与 func 映射起来 => # 🌟 比如在这一步把 URL_ROUTE['/index.py'] 对应为 login() 函数 🌟
		def call_func(*args, **kwargs): # 收集 func 函数的所有参数, 并返回 func 函数!
			return func(*args, **kwargs)
			return call_func
	return set_func # 此时 login(x) = setfunc(x), 因为 return setfunc(x) 出来了




# 👇👇👇 在这里边进行数据库的查询 （比如 mySQL)!!! ————————————————————————————————————————————————————————————————————————
@route("/index.html")
def index():
	# 👇不使用上下文管理器
	# with open("views/templates/index.html", "r") as f: # 从打开路径 => server.js 这个位置开始找 index.html
		# content = f.read() # 读取文件内容
  
	# 1. 获取 html 模板 View
	with mini_open_static("/index.html", "r") as f: # 👈 使用 mini_open_static 上下文管理器
		content = f.read() # 读取文件内容
  
	# 2. 查询数据库
	db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='stock_db', charset='utf8') # 一: 连接数据库服务器
	cursor = db.cursor() # 二: 获取游标(用来操作数据库, 执行 sql 语句, 获取结果)
	cursor.execute("select * from info;") # 三: 执行 sql 语句, 🔥可以进行分页 => select * from info; 相当于查询出 info 表格的所有数据
	data_from_database = cursor.fetchall() # 四: 获取结果
	cursor.close() # 五: 关闭游标
	db.close() # 六: 关闭数据库服务器连接
	# print("\n\n")
	# print(data_from_database) # 七: 打印出来的是元组的数据列表
 
	# 八: 把数据填入 html 模板内
	html_template = """
			<tr>
				<td>{0[0]}</td>
				<td>{0[1]}</td>
				<td>{0[2]}</td>
    			<td>{0[3]}%</td>
				<td>{0[3]}%</td>
				<td>{0[4]}</td>
				<td>{0[5]}</td>
				<td>{0[7]}</td>
				<td>
    				<input type="button" value="添加" id="add" name="add" systemId="{0[1]}">
        		</td>
        	</tr>
 			"""
	html = "" # 定义个变量, 用来存储查询出来的数据最终要组成的 list html
	for i_stock in data_from_database:
		html += html_template.format(i_stock) # 有多少个数据就会产生多撒后行
     
	# data_from_database = "模拟从数据库查询出来的数据"
	# content = re.sub(r"\{% content %\}", html, content) # 🚀🚀 导入正则表达式模块, 用来替换 index.html 内的 content 这个占位符字符串位置的内容
	content = re.sub(r"\{% content %\}", str(html), content) # 🚀🚀 导入正则表达式模块, 用来替换 index.html 内的 content 这个占位符字符串位置的内容
	return content


@route("/login.html")
def login():
	response_body = "⏰ 登录页面, 当前时间是: %s" % time.ctime()
	return response_body

@route("/register.html")
def register():
	response_body = "✏️ 注册页面"
	return response_body

@route("/detail.html")
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
	# if env['PATH_INFO'] == '/login.py':
	# 	return login()
	# elif env['PATH_INFO'] == "/detail.py":
	# 	return detail()
	# elif env['PATH_INFO'] == "/register.py":
	# 	return register()
	# else:
	# 	return wrong_404()



	# 🔥 2. 根据字典定义的路由, 来调用不同的函数
	file_path = env['PATH_INFO'] # 获取请求的 path  => "/login.html"
	# if file_path.endswith('.py'):
	# 	file_path = file_path[:-3]  # 去掉 '.py' 后缀
     
	# 🔥 根据路由匹配函数
	# func = URL_ROUTE[file_path] # [🔥字典中自带了 get 方法, 使用 get 方法更加保险, 不会让程序崩溃！]
	func = URL_ROUTE.get(file_path, None) # [🔥字典中自带了 get 方法, 使用 get 方法更加保险, 不会让程序崩溃！]
 
 
	if not func: # 🔥如果没有找到 url => 在字典中没有找到对应的映射
		# 🔥回调(🚀返回页面), 执行 http_server.py 内的 set_status_headers 函数 !! 并且将状态码传递过去
		call_func("404 Not Found", [("Content-Type", "text/html; charset=utf-8"), ("Framework", "mini-web")])
		func = URL_ROUTE.get("404", lambda: "❌ Not found page 404") # 表示如果没有 404 页面, 则用 lambda 进行兜底, 以免有些地方没有写 404 page
	else:
		# 🔥回调(🚀返回页面), 执行 http_server.py 内的 set_status_headers 函数 !! 并且将状态码传递过去
		call_func("200 OK", [("Content-Type", "text/html; charset=utf-8"), ("Framework", "mini-web")]) # 🚀列表套元组(元组是不可变的, 一旦创建其元素便不能被修改), Content-Type 表示键, text/html; charset=utf-8 表示值
		
 
 
	# 🔥 3. 调用函数的引用
	response_body = func()
 
 
	# 🔥 4. 返回数据给到 web 服务器
	return response_body

