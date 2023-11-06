import os
import logging

# 获取【当前中间件脚本】的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 拼接【日志文件】的绝对路径
log_file_path = os.path.join(current_dir, 'user_request_log.txt')

# 配置日志记录
logging.basicConfig(filename=log_file_path, level=logging.DEBUG)

def log_middlewareFn(env, start_response = None): # env 为传入的请求信息，start_response 为传出的响应信息
    # 打印
    print("记录用户数据")
    
	# 获取用户的 IP 地址
    remote_addr = env.get('REMOTE_ADDR', '-')

	# 获取用户的 User-Agent
    user_agent = env.get('HTTP_USER_AGENT', '-')

	# 判断是否有用户访问
    if remote_addr != '-':
		# 记录请求信息，包括 IP 地址和 User-Agent
        request_method = env.get('REQUEST_METHOD', '-')
        request_uri = env.get('REQUEST_URI', '-')
		
        logging.info(f"Request from {remote_addr} (User-Agent: {user_agent}): {request_method} {request_uri}")
        print(f"Request from {remote_addr} (User-Agent: {user_agent}): {request_method} {request_uri}")
        logging.shutdown()

    # 调用下一个应用（或中间件）或直接返回响应
    # response = your_application(env, start_response)
    # return response