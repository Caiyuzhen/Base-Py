""" 
	捕获异常错误
		捕获异常错误的目的是为了让程序继续运行下去, 如果不捕获异常错误，程序就会停止运行
		捕获错误后可以进一步的做一些处理
  
	捕获异常错误的语法:
		1.万能异常错误: Exception => 能捕捉所有错误, 但不具体, 一般【🔥用在捕获异常的最后！】
			try:
				your code
		
			except Exception: 
				error code #出错才会执行
    
		2.缺少输入值
			NameError
    
		3.捕获输入的值不合法
			ValueError
   
		4.试图访问一个没有的属性
			AttributeError
  
		5.访问了字典中不存在的键
			KeyError
	
		...
  
	主动触发异常
		比如应用层面的异常 => 如自己写的插件, 登录 QQ 错误等
	
	自定义异常 -> 自己写个类去继承 BaseException :
		比如说第三方插件的错误



  
"""	
import sys # 当try块中的代码引发异常时，sys.exit(1)会结束程序的执行，返回一个非零的退出代码（通常用1表示错误），表示任务已经结束


# 自定义异常
class YoutubeConnentError(BaseException):
	def __init__(self, msg):
		self.message = msg  # 把错误消息放入构造函数

	def __str__(self):
		return self.message  # 返回异常文案


# try:
# 	raise YoutubeConnentError("这是一个异常消息")

# except YoutubeConnentError as e:
# 	print(f"❌ 触发了自定义异常 {e}")
 
 

print("try except Exception 捕捉错误 ——————————————————————————————————————————————")
while True:
	# num1 = input('输入第 1 个数字:')
	# num2 = input('输入第 2 个数字:')
	
	try:
		# num1 = int(num1)
		# num2 = int(num2)
		# result = num1 + num2
		# print(name.check)
		# open("./filetest.py")
		# print(result)
		# print(result, name)
		raise YoutubeConnentError("这是一个异常消息")
		# raise IndexError # 主动触发异常 (比如应用层面的异常 => 如自己写的插件)

	except NameError as n:
		print(f"❌ 缺少输入值, 错误信息如下: {n}")
		sys.exit(1)
  
	except ValueError as v:
		print(f"❌ 输入的值不合法, 错误信息如下: {v}")
		sys.exit(1)

	except AttributeError as a:
		print(f"❌ 缺少对应的属性, 错误信息如下: {a}")
		sys.exit(1)

	except IOError as i:
		print(f"❌ 打开文件错误, 错误信息如下: {i}")
		sys.exit(1)
  
	except KeyError as k:
		print(f"❌ 访问了字典中不存在的键: {k}")
		sys.exit(1)
  
	except Exception as e:
		print(f"❌ 发生了错误: {e}")
		sys.exit(1)
  
	except YoutubeConnentError as y:
		print(f"❌ 触发了自定义异常 {y}")
		sys.exit(1)
  
	else:
		print("无异常的逻辑...")
  		#...
    
	finally: # 🚀 不管有没有异常都走这里
		print("不管有没有异常都走这里")
  
  
  
  

