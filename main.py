import json
items = json.loads('[{"id": 1, "text": "🥗沙拉"}, {"id": 2, "text": "🍔汉堡"}, {"id": 3, "text": "🥟饺子"}]')

for item in items:
	print(item["text"])


# 变量名不能以数字开头！！
if True:
	print('吃沙拉')
else:
	print('吃饺子')

try:
	pass
except Exception as e:
	print(e)