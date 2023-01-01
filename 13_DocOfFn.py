# 🔥函数的文档、描述
def Exchange(dollar, rate=6.32):
	"""
		功能: 汇率转换(美元兑人民币)
		参数: dollar: 美元
			  rate: 汇率, 默认值为 6.32
	"""
	return dollar * rate

print(Exchange(100))

# 通过 help 来查看函数的文档
help(Exchange) 

# 通过 .__doc__ 来查看函数文档
print(Exchange.__doc__)




# 🔥函数的类型注释
# Python 具有四种原始数据类型：整数类型（int）、浮点数类型（float）、布尔类型（bool）和字符串类型（str）。
def Times(s:str = '默认参数', n:int = '2') -> str: # 字符串、整数
	return s * n

print(Times('Zen', 3))




# 注释为列表类型
def Times2(s:list, n:int) -> list: # 列表、整数
	return s * n # 返回一个大列表

print(Times2([1,2,3], 2))


# 注释为字典类型（键、值）
def Times3(s:dict[str, int], n:int) -> dict: # 字典、整数
	return list(s.keys()) * n # ⚡️返回字典中的键，组成一个列表，然后再在 * n

print(Times3({"A":1, "B":2, "C":3}, 2))


