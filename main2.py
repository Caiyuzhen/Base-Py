import requests

# 请求 api
response = requests.get('http://randomuser.me/api')
response2 = requests.get('http://randomuser.me/api/?results=5')

data = response.json()
data2 = response2.json()


# 遍历获取数据
for user in data2['results']:
	print(user['name']['first'])


print(9 * 1000)


# 创建函数
def greet(greeting, name):
	# 模板字符串
	"""Return a greeting


	Arguments:
		greeting {string} -- A great world
		name {string} -- A great person name


	Returns:
		string -- A great with a name
	"""
	return f'{greeting} {name}'


print(greet('hello', 'world'))