import re
import socket
import sys
import os


# 全局变量, 记录要打开的文件路径
g_document_root = "./html" # 服务器根路径



def main():
	# 1. 创建套接字
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# 2. 绑定本地信息
	server_socket.bind(("localhost", 8080)) # 绑定【域名】跟【端口】

	# 3. 监听套接字
	server_socket.listen(128) # 128 表示同一时刻最多可以链接多少个 (128 个) 客户端
 
	# 4. 开始监听, 等待新客户端的链接
	while True:
		print("Server is listening on port 8080...")
		new_socket, new_addr = server_socket.accept() # 🔥 new_socket 为新的套接字, new_addr 为新的地址

		# 5. 接收请求的数据
		request = new_socket.recv(1024).decode('utf-8') # 1024 表示本次接收的最大字节数
		# print(request)
		req_lines = request.splitlines() # 🚀 把请求数据按行分割成列表
		for i, line in enumerate(req_lines): # 🔥🔥 enumerate 表示枚举, i 表示索引, line 表示元素
			pass
			# print(i, line)

		# 6. 提取请求的文件（比如 index.html）
		print(req_lines[0]) # GET /index.html HTTP/1.1 => 完整的请求文件
		ret = re.match(r"([^/]*)([^ ]+)", req_lines[0]) # [^/]*[^ ] 表示从取出路径 => /a/b/c/index.html
		if ret:
			print("——————————")
			print("正则提取出的数据:", ret.group(1)) 
			print("正则提取出的数据:", ret.group(2)) 
			file_name = ret.group(2) # 🔥保存请求的文件名

		# 7. 打开文件, 读取文件数据
		file_path = g_document_root + file_name
		if os.path.exists(file_path):
			f = open(file_path, "rb") # 🔥 rb 用来打开【二进制】文件
			content = f.read() # 🔥 存储读取出来的文件数据
			# ... 其余文件处理代码
		else:
			return # 文件不存在时的处理


		# 8. 把数据返回给浏览器 (🔥 如果需要发送响应头跟二进制数据, 则需要分开发送!! 因为字符串跟二进制的数据无法同时发送!!)
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
  
		f.close()



if __name__ == "__main__":
	main()
