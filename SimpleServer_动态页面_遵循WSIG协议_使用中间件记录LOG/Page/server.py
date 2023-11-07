import re
import socket
import sys
import os
import time
from mini_web import application, login, register, detail, wrong_404 # 导入 login.py, register.py 里的函数
from middlewares.log_middleware import log_middlewareFn
import multiprocessing # 🔥 【进程】模块, 一个进程只能用一个端口!! 【线程（Thread）和进程（Process）】, 一个进程中可以同时存在多个线程, 各个线程之间可以并发执行, 各个线程之间可以共享地址空间和文件等资源, 当进程中的一个线程奔溃时，会导致其所属进程的所有线程奔溃

# 🌟WSGI 协议服务器类
class WSGIServer():
	""" 初始化服务器 """
	def __init__(self, port, documents_root):
     
		global application

		self.documents_root = documents_root #  🔥 服务器根路径
		self.port = port # 🔥 存放端口号

		# 1. 创建套接字  ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# 2. 绑定本地信息(绑定端口) ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
		self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 🚀🚀 在绑定端口前, 允许端口在没有释放干净前就可以复用 !! 防止端口被占用
		self.server_socket.bind(("localhost", self.port)) #server_socket.bind(("localhost", 8080)) # 绑定【域名】跟【端口】


		# 3. 监听套接字 ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
		self.server_socket.listen(128) # 128 表示同一时刻最多可以链接多少个 (128 个) 客户端
  
		# 定义两个属性用来存储 web 框架传输过来的 status 状态码以及 header 响应头
		self.status = "" # 存储字符串
		self.headers = [] # 存储列表
	
 
	""" 运行服务器 """
	def run_forever(self):
		# 4. 开始监听, 等待新客户端的链接 ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
		while True:
			print(f"Server is listening on port {self.port}...")
			self.new_socket, new_addr = self.server_socket.accept() # 🔥 用 self 来让整个类共享数据!! self.new_socket 为新的套接字, new_addr 为新的地址
			# self.deal_with_request() # 调用下一个方法
   			# 4-1. 🚀🚀🚀 (子进程) 进行多进程得处理请求 ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
			new_process = multiprocessing.Process(target = self.deal_with_request) # deal_with_request 不写括号, 表示传递函数, 而不是调用函数
			new_process.start() # 🔥🔥🔥 开启进程, 多份代码之间共享数据 (比如这份代码), COW 当数据被修改时, 才会进行复制, 否则就是共享数据
			self.new_socket.close() # 🔥🔥🔥 (进程的 self.new_socket 要关闭两次!!) 因为【子进程】会复制一份主进程的数据, 因此主进程也得关闭, 避免资源浪费, 如果内存存了个超大的文件, 内存资源就会用尽!!


	""" WSGI 从 Web 框架中接收 header 的设置"""
	def set_status_headers(self, status, headers):
		self.status = status # 🔥 保存状态码 "200 OK"
		self.headers = headers # 🔥 保存 header 响应头, [("Content-Type", "text/html; charset=utf-8")]
	

	""" 处理请求 """
	def deal_with_request(self):
		# 5. 接收 web 发送过来的 tcp 请求数据 ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
		request = self.new_socket.recv(1024).decode('utf-8') # 1024 表示本次接收的最大字节数
  
  
		if request: # 如果有数据
  
			# print(request)
			req_lines = request.splitlines() # 🚀 把请求数据按行分割成列表
   
   			# 👇用来传输给中间件的数据 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
			userReq_data = {
				'REMOTE_ADDR': self.new_socket.getpeername()[0],
				'REQUEST_METHOD': req_lines[0].split(" ")[0],  # 提取出请求的方法
				'REQUEST_URI': req_lines[0],
				# 'HTTP_USER_AGENT': user_agent  # 用户信息
			}
   
			# 提取 User-Agent 头信息 => 用来传递给中间件的数据 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
			for line in req_lines:
				if line.startswith("User-Agent:"):
					userReq_data['HTTP_USER_AGENT'] = line.split(":", 1)[1].strip()
					break
 
			log_middlewareFn(userReq_data) # 将中间件添加到应用程序 %%%%%%%%%%%%%%%%%%%%%%%%%%%%
   
   
			for i, line in enumerate(req_lines): # 🔥🔥 enumerate 表示枚举, i 表示索引, line 表示元素
				pass
				# print(i, line)

			# 6. 提取请求的文件（比如 index.html）——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
			print(req_lines[0]) # GET /index.html HTTP/1.1 => 完整的请求文件
			ret = re.match(r"([^/]*)([^ ]+)", req_lines[0]) # [^/]*[^ ] 表示从取出路径 => /a/b/c/index.html
			if ret: # 如果正则匹配成功, 表示提取到了请求的文件名
				print("——————————")
				print("正则提取出的数据:", ret.group(1)) 
				print("正则提取出的数据:", ret.group(2)) 
				file_name = ret.group(2) # 🔥保存请求的文件名

				if file_name == "/":
					file_name = "/index.html"

				# 👇如果不是 .py 结尾的请求, 就是获取静态资源 ************************************************************************
				if not file_name.endswith(".py"):
					# 7. 打开文件, 读取文件数据 ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
					has_error = False  # 标志, 用于指示是否发生异常
					f = None  # 初始化 f 变量, 用于判断文件是否存在

					try: # 尝试打开文件
						file_path = self.documents_root + file_name
						if os.path.exists(file_path):
							f = open(file_path, "rb") # 🔥 rb 用来打开【二进制】文件
							content = f.read() # 🔥 存储读取出来的文件数据
							# ... 其余文件处理代码
						else:
							raise Exception("❌ 文件不存在～")
					except: # 👇 如果有异常, 把异常数据返回给浏览器
						has_error = True
						not_found_header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain; charset=utf-8\r\n" # 🚀 访问的地址不存在时的处理
						not_found_header += "\r\n" # 空格
						not_found_body = "❌ Url is not found, 请输入正确的 url 地址"
						self.new_socket.send(not_found_header.encode('utf-8'))
						self.new_socket.send(not_found_body.encode('utf-8'))
						self.new_socket.close()
					finally: # 如果没异常, 把拿到的文件返回给浏览器
						if not has_error: # 只有在没有异常的情况下才发送正常的响应
							# 8. 把数据返回给浏览器 (🔥 如果需要发送响应头跟二进制数据, 则需要分开发送!! 因为字符串跟二进制的数据无法同时发送!!) ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
							response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n"  # \r\n 表示回车换行, 为了兼容 linux, macosx, windows
							response_header += "\r\n" # 表示一个空行, 作为换行符
							response_body = content

							# 8-1.分开发送给浏览器 - 发送 header
							self.new_socket.send(response_header.encode('utf-8')) # 🚀 发送 header 数据给浏览器

							# 8-1.分开发送给浏览器 - 发送 body (html 页面数据)
							self.new_socket.send(response_body) # 🚀 发送 html 二进制数据给浏览器

						# 9. 关闭这个新套接字 (🔥 self.new_socket!!) ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
						self.new_socket.close() # 🔗 关闭的话, 就是短链接, 图片那些得重新请求 (又得重新进行三次握手四次挥手)

						if f is not None: # 如果文件存在
							f.close()
				# 👇如果是 .py 结尾的请求, 就生成动态页面 ************************************************************************
				else:
					# 👇更健壮, 避免只能返回 200 OK, 而是能在 web 框架中设置 header 响应头
					env = dict() # 🔥🔥定义字典, 用来封装数据传递给 application => Reference WSGI 协议约定的能传入的字典参数 : https://doc.itprojects.cn/0001.zhishi/python.0023.miniweb/index.html#/01
					env['PATH_INFO'] = file_name # 🔥🔥 传入请求的文件名
     
					response_body = application(env, self.set_status_headers) # env 为请求的文件名、self.set_status_headers 为传入状态码跟返回 headerv 的函数 👈👈 不写括号, 不是调用函数, 而是把函数【传入 application（外部处理 web 页面的函数） 内】, 在 application 内去调用并传入 header 的状态码等 header 响应 !!! 🔥🔥 response_body 就是 application 的 return !!! 因此 header 不能写在 body 前面, 否则拿不到 header 的值
					response_header = "HTTP/1.1 %s\r\n" % {self.status}  # 👈👈 合并 header 的状态码跟响应	
					for headerContent in self.headers:
						response_header += "%s: %s\r\n" % (headerContent[0], headerContent[1]) # 👈👈 合并 header 的响应头
					response_header += "\r\n"
					response = response_header + response_body # 🚀 储存返回给浏览器的数据
					self.new_socket.send(response.encode('utf-8'))  # encode('utf-8') 用来转为二进制数据传给浏览器
					self.new_socket.close()
     

def main():
	http_server = WSGIServer(8080, './html') # 🔥传入端口 + 文件夹的根路径
	http_server.run_forever() # 🔥 一直运行程序


if __name__ == "__main__": # 当这个脚本被直接运行时（而不是被其他脚本导入），调用 main() 函数，执行主要功能
	main()
