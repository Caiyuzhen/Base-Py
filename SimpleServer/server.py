import re
import socket
import sys
import os
import time


# 全局变量, 记录要打开的文件路径
g_document_root = "./html" # 服务器根路径



# 🔥启动服务器主程序
def main():
	# 1. 创建套接字 = 绑定端口 ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# 2. 绑定本地信息 (调用等待函数绑定端口) ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
	def wait_for_port_release(port, timeout=60): # 等待函数, 等待直到端口被释放
		start_time = time.time()
		while True:
			try:
				server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 🚀🚀 在绑定端口前, 允许端口在没有释放干净前就可以复用 !! 防止端口被占用
				server_socket.bind(("localhost", port)) # server_socket.bind(("localhost", 3999)) # 绑定【域名】跟【端口】
				break
			except OSError as e:
				if "Address already in use" in str(e) and time.time() - start_time < timeout:
					time.sleep(1)  # 每秒检查一次
				else:
					raise # raise 表示抛出异常
	wait_for_port_release(8080)  # 此处使用您希望等待的端口号

	# 3. 监听套接字 ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
	server_socket.listen(128) # 128 表示同一时刻最多可以链接多少个 (128 个) 客户端
 
	# 4. 开始监听, 等待新客户端的链接 ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
	while True:
		print("Server is listening on port 8080...")
		new_socket, new_addr = server_socket.accept() # 🔥 new_socket 为新的套接字, new_addr 为新的地址

		# 5. 接收请求的数据 ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
		request = new_socket.recv(1024).decode('utf-8') # 1024 表示本次接收的最大字节数
		# print(request)
		req_lines = request.splitlines() # 🚀 把请求数据按行分割成列表
		for i, line in enumerate(req_lines): # 🔥🔥 enumerate 表示枚举, i 表示索引, line 表示元素
			pass
			# print(i, line)

		# 6. 提取请求的文件（比如 index.html）——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
		print(req_lines[0]) # GET /index.html HTTP/1.1 => 完整的请求文件
		ret = re.match(r"([^/]*)([^ ]+)", req_lines[0]) # [^/]*[^ ] 表示从取出路径 => /a/b/c/index.html
		if ret:
			print("——————————")
			print("正则提取出的数据:", ret.group(1)) 
			print("正则提取出的数据:", ret.group(2)) 
			file_name = ret.group(2) # 🔥保存请求的文件名
   
			if file_name == "/":
				file_name = "/index.html"

			# 7. 打开文件, 读取文件数据 ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
			has_error = False  # 标志, 用于指示是否发生异常
			f = None  # 初始化 f 变量, 用于判断文件是否存在
   
			try:
				file_path = g_document_root + file_name
				if os.path.exists(file_path):
					f = open(file_path, "rb") # 🔥 rb 用来打开【二进制】文件
					content = f.read() # 🔥 存储读取出来的文件数据
					# ... 其余文件处理代码
				else:
					raise Exception("❌ 文件不存在～")
			except: # 如果有异常
				has_error = True
				not_found_header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain; charset=utf-8\r\n" # 🚀 访问的地址不存在时的处理
				not_found_header += "\r\n" # 空格
				not_found_body = "❌ Url is not found, 请输入正确的 url 地址"
				new_socket.send(not_found_header.encode('utf-8'))
				new_socket.send(not_found_body.encode('utf-8'))
				new_socket.close()
				# pass
			# 8. 把数据返回给浏览器 (🔥 如果需要发送响应头跟二进制数据, 则需要分开发送!! 因为字符串跟二进制的数据无法同时发送!!) ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
			finally: # 如果没异常
				if not has_error: # 只有在没有异常的情况下才发送正常的响应
					response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n"  # \r\n 表示回车换行, 为了兼容 linux, macosx, windows
					response_header += "\r\n" # 表示一个空行, 作为换行符
					response_body = content
					# response_body = "👋 你好 Hello!"
					# response = response_header + response_body # 🚀 储存返回给浏览器的数据

					# 8-1.分开发送给浏览器 - 发送 header
					new_socket.send(response_header.encode('utf-8')) # 🚀 发送 header 数据给浏览器

					# 8-1.分开发送给浏览器 - 发送 body (html 页面数据)
					new_socket.send(response_body) # 🚀 发送 html 二进制数据给浏览器

				# 9. 关闭这个新套接字 (🔥 new_socket!!)
				new_socket.close()

				if f is not None: # 如果文件存在
					f.close()


if __name__ == "__main__":
	main()
