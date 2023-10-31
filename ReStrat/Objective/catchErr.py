""" 
	捕获异常错误
		捕获异常错误的目的是为了让程序继续运行下去, 如果不捕获异常错误，程序就会停止运行
  
	捕获异常错误的语法:
		1.万能异常错误: Exception => 能捕捉所有错误, 但不具体, 一般不用, 不然不知道哪里错了
			try:
				your code
		
			except Exception: 
				error code #出错才会执行
    
		2.缺少输入值
			NameError
    
		3.捕获输入的值不合法
			ValueError
  
"""	



print("try except Exception 捕捉错误 ——————————————————————————————————————————————")
while True:
	num1 = input('输入第 1 个数字:')
	num2 = input('输入第 2 个数字:')
	
	try:
		num1 = int(num1)
		num2 = int(num2)
		result = num1 + num2
		print(result)
		# print(result, name)

	except NameError as n:
		print(f"❌ 缺少输入值, 错误信息如下: {n}")

	except ValueError as v:
		print(f"❌ 输入的值不合法, 错误信息如下: {v}")
