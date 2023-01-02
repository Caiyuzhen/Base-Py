# 🔥无论是否正确，文件执行完后都能被关闭

try: # 检测范围
	f = open('123.text', 'w')
	f.write('123')
except: # 异常时处理的代码
	print('出错了')
else: # 没有异常时执行的代码
	print('没有出错')
finally: # 收尾工作执行的代码
	f.close()




# 🔥直接抛出异常
# raise ValueError("值不正确")




# 🔥利用异常一把跳过所有嵌套
try:
	while True:
		while True:
			while True:
				for i in range(10):
					if( i > 3):
						raise
					print(i)
				print('被跳过~')
			print('被跳过~')
		print('被跳过~')
except:
	print('跳到这里了')
