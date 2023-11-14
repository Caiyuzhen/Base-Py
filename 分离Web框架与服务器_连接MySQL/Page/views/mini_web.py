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
    yield f # 🔥🔥 yield 执行到这里会去暂停一下, 然后下去执行  content = f.read() # 读取文件内容, 然后再回来执行 f.close()
    f.close()




# 🚀 装饰器函数, 用来把 【url】 跟 【函数】的映射关系对应上 ——————————————————————————————————————————————————————————————————————————————
def route(url):  # url => "/login.html"
	def set_func(func): # func => 函数名
		URL_ROUTE[url] = func # 将 url 与 func 映射起来 => # 🌟 比如在这一步把 URL_ROUTE['/index.py'] 对应为 login() 函数 🌟
		def call_func(*args, **kwargs): # 收集 func 函数的所有参数, 并返回 func 函数!
			return func(*args, **kwargs)
			return call_func
	return set_func # 此时 login(x) = setfunc(x), 因为 return setfunc(x) 出来了






# 👇👇👇 在这里边进行数据库的查询 （比如 mySQL)!!! ————————————————————————————————————————————————————————————————————————
@route(r"/index\.html") # 因为是 r 正则表达式, 所以 . 需要转译一下
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
	sql = """select * from info;""" # 三: 执行 sql 语句, 🔥可以进行分页 => select * from info; 相当于查询出 info 表格的所有数据
	cursor.execute(sql)
	data_from_database = cursor.fetchall() # 四: 获取结果
	cursor.close() # 五: 关闭游标
	db.close() # 六: 关闭数据库服务器连接
	# print("\n\n")
	# print(data_from_database) # 七: 打印出来的是元组的数据列表
 
	# 八: 定义 html 模板
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
    				<input type="button" value="添加" id={0[0]} name="add">
        		</td>
        	</tr>
 			"""
	html = "" # 定义个变量, 用来存储查询出来的数据最终要组成的 list html
	for i_stock in data_from_database:
		html += html_template.format(i_stock) # 有多少个数据就会产生多少行, format 表示格式化, 用来格式化字符串
     
    # 3.把数据塞入 html 模板内
	# data_from_database = "模拟从数据库查询出来的数据"
	# content = re.sub(r"\{% content %\}", html, content) # 🚀🚀 导入正则表达式模块, 用来替换 index.html 内的 content 这个占位符字符串位置的内容
	content = re.sub(r"\{% content %\}", str(html), content) # 🚀🚀 导入正则表达式模块, 用来替换 index.html 内的 content 这个占位符字符串位置的内容
	return content



@route(r"/login\.html") # 因为是 r 正则表达式, 所以 . 需要转译一下
def login():
	response_body = "⏰ 登录页面, 当前时间是: %s" % time.ctime()
	return response_body


@route(r"/register\.html") # 因为是 r 正则表达式, 所以 . 需要转译一下
def register():
	response_body = "✏️ 注册页面"
	return response_body



@route(r"/focus\.html") # 因为是 r 正则表达式, 所以 . 需要转译一下
def focus():
    # 1. 获取 html 模板 View
    with mini_open_static("/focus.html", "r") as f:
        content = f.read()
        
	# 2. 查询数据库
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='stock_db', charset='utf8') # 一: 连接数据库服务器
    cursor = db.cursor() # 二: 获取游标(用来操作数据库, 执行 sql 语句, 获取结果)
    # 三: 执行 sql 语句, 🔥i.id=j.info_id 跟 reference 进行连接         
    sql = """SELECT i.stock_code, i.short_info, i.chg, i.turnover, i.price, i.highs, f.note_info
    		 FROM info AS i
     		 INNER JOIN focus AS f ON i.id = f.info_id;"""

    cursor.execute(sql)
    data_from_database = cursor.fetchall() # 四: 获取结果 , fetchone 表示提取所有数据
    print(data_from_database)
    cursor.close() # 五: 关闭游标
    db.close() # 六: 关闭数据库服务器连接
	# 七: 定义 html 模板
    html_template = """
			<tr>
				<td>{0[0]}</td>
				<td>{0[1]}</td>
				<td>{0[2]}</td>
    			<td>{0[3]}%</td>
				<td>{0[4]}%</td>
				<td>{0[5]}</td>
    			<td>{0[6]}</td>
    			<td>
    				<a class="btn btn-primary" id={0[0]} name="changeNote" href="/update/{0[0]}.html">修改备注</a>
        		</td>
				<td>
					<input type="button" value="删除备注" id={0[0]}  name="delete" systemIDvalue="{0[0]}">
        		</td>
        	</tr>
 			"""
    html = "" # 定义个变量, 用来存储查询出来的数据最终要组成的 list html
    for i_stock in data_from_database:
        html += html_template.format(i_stock) # 有多少个数据就会产生多撒后行
    # 3.把数据塞入 html 模板内
    content = re.sub(r"\{% content %\}", str(html), content) # 🚀🚀 导入正则表达式模块, 用来替换 index.html 内的 content 这个占位符字符串位置的内容
    return content



@route(r"/update/(\d+)\.html") # 每支股票的详情页, # 因为是 r 正则表达式, 所以 . 需要转译一下
def updatePage(stock_code):
    
    # 1. 打开 html 模板
    with mini_open_static("/update.html", "r") as f:
        content = f.read()
        
    # 2. 查询数据库
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='stock_db', charset='utf8') # 一: 连接数据库服务器
    cursor = db.cursor() # 二: 获取游标(用来操作数据库, 执行 sql 语句, 获取结果)
    
    # 三: 执行 sql 语句, 🔥i.id=j.info_id 跟 reference 进行连接         
    sql = """SELECT focus.note_info from focus inner join info on focus.info_id=info.id where info.stock_code=%s;""" #当 focus 的 id 跟 info 的 id 一样时候 => on focus.focus_info_id=info.id  |  要找哪知股票 => where info.stock_code=%s; ｜ 👈两个表的内连接
    cursor.execute(sql, [stock_code]) # 👈 为了避免 sql 注入, 使用 MYSQL 自带的功能参数化
    data_from_database = cursor.fetchone() # 四: 获取结果 , fetchone 表示提取一条数据

	# 五: 关闭游标
    cursor.close() 
    
    # 六: 关闭数据库服务器连接
    db.close() 
    
    content = re.sub(r"\{% stock_code %\}", stock_code, content) # 通过正则替换掉 html 模板内的 {% stock_code %} 这个占位符
    content = re.sub(r"\{% note_info %\}", str(data_from_database[0]), content) # 通过正则替换掉 html 模板内的 {% note_info %} 这个占位符
    # 3.返回数据
    return content



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
	#     file_path = file_path[:-3]  # 去掉 '.py' 后缀
 
 
	# 2-1 提取从路由中获取出来的 path 里边的文件名 比如 update/000037.html
	func = URL_ROUTE.get(file_path, None) # [🔥字典中自带了 get 方法, 使用 get 方法更加保险, 不会让程序崩溃！] 👈会把用户请求的 /index.html 放入到字典中, 然后去👆 URL_ROUTE 中让 index 跟 index() 进行对应！
 
	for url, func in URL_ROUTE.items(): # 一种情况是可以映射到函数的, 另一种情况是不能映射到函数的 => 比如 update/000037.html
		ret = re.match(url, file_path) # 相当于 match 匹配 re.match(r"/update/\d+\.html", "/update/000037.html")
		if ret: # 如果匹配到了
			# 如果匹配到了字典中有映射的函数
			call_func("200 OK", [("Content-Type", "text/html; charset=utf-8"), ("Framework", "mini-web")]) # 🚀列表套元组(元组是不可变的, 一旦创建其元素便不能被修改), Content-Type 表示键, text/html; charset=utf-8 表示值
   
			# func.__name__
			# func.__code__.co_argcount
			paraments = [] #从正则中提取出来的数据
			for i in range(func.__code__.co_argcount): # 🌟func.__code__.co_argcount 表示函数的【参数个数】=> 这样就能根据 http://localhost:8080/update/000037.html 的查询参数来匹配到对应的函数了！！有参数就会 group[X] 来获得参数, 没有参数则不会 group[X] 来获得参数
				paraments.append(ret.group(i+1)) # 从正则中提取出来的数据, 从 1 开始, 因为 0 是整个正则匹配到的数据
				

			# 👇👇从路由中拿到路径
			# stock_code = ret.group(1)
   
			# 👇👇把路径传入到函数内, 以便函数内部使用
			response_body = func(*paraments)  # * 表示拆包
   
			break
	else:
		# 如果字典中没有匹配到影射的函数
		call_func("404 Not Found", [("Content-Type", "text/html; charset=utf-8"), ("Framework", "mini-web")])
		func = URL_ROUTE.get("404", lambda: "❌ Not found page 404") # 表示如果没有 404 页面, 则用 lambda 进行兜底, 以免有些地方没有写 404 page
		response_body = func()
 
 
     
	# 🔥 根据路由匹配函数 (👇旧) ————————————————————————————————————————
	# func = URL_ROUTE[file_path] # [🔥字典中自带了 get 方法, 使用 get 方法更加保险, 不会让程序崩溃！] (更旧)
	# func = URL_ROUTE.get(file_path, None) # [🔥字典中自带了 get 方法, 使用 get 方法更加保险, 不会让程序崩溃！] 👈会把用户请求的 /index.html 放入到字典中, 然后去👆 URL_ROUTE 中让 index 跟 index() 进行对应！
 
 
	# if not func: # 🔥如果没有找到 url => 在字典中没有找到对应的映射
	# 	# 🔥回调(🚀返回页面), 执行 http_server.py 内的 set_status_headers 函数 !! 并且将状态码传递过去
	# 	call_func("404 Not Found", [("Content-Type", "text/html; charset=utf-8"), ("Framework", "mini-web")])
	# 	func = URL_ROUTE.get("404", lambda: "❌ Not found page 404") # 表示如果没有 404 页面, 则用 lambda 进行兜底, 以免有些地方没有写 404 page
	# 	# 🔥 3. 调用函数的引用
	# 	response_body = func(file_path)
	# else:
	# 	# 🔥回调(🚀返回页面), 执行 http_server.py 内的 set_status_headers 函数 !! 并且将状态码传递过去
	# 	call_func("200 OK", [("Content-Type", "text/html; charset=utf-8"), ("Framework", "mini-web")]) # 🚀列表套元组(元组是不可变的, 一旦创建其元素便不能被修改), Content-Type 表示键, text/html; charset=utf-8 表示值
	# 	# 🔥 3. 调用函数的引用
	# 	response_body = func(file_path)
 
 
 
	# 🔥 4. 返回数据给到 web 服务器
	return response_body

