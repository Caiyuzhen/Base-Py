import requests

# 请求 api
response = requests.get('http://randomuser.me/api')
response2 = requests.get('http://randomuser.me/api/?results=20')

data = response.json()
data2 = response2.json()


# 遍历获取数据
for user in data2['results']:
	print(user['name']['first'])


print(9 * 1000)