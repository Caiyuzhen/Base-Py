import logging

# 配置日志记录
logging.basicConfig(filename='user_request_log.txt', level=logging.INFO)

def log_middlewareFn(env, start_response = None): # env 为传入的请求信息，start_response 为传出的响应信息
    # 记录请求信息
    remote_addr = env.get('REMOTE_ADDR', '-')
    request_method = env.get('REQUEST_METHOD', '-')
    request_uri = env.get('REQUEST_URI', '-')
    logging.info(f"Request from {remote_addr}: {request_method} {request_uri}")

    # 调用下一个应用（或中间件）或直接返回响应
    # response = your_application(env, start_response)
    # return response