# 🔥列表类比篮子，可以放入不同种类的数据
rhyme = [1, 2, 3, '你好']
print(rhyme[3])

for each in rhyme:
	print(each)


# 访问最后一个元素(方法一)
length = len(rhyme)
print(rhyme[length - 1]) #你好


# 访问最后一个元素(方法二)
print(rhyme[-1]) #你好




# 🔥列表切片(获取多个数据）
# 一个区间
print(rhyme[0:2]) # [1, 2]

# XXX 之前的数据
print(rhyme[:3]) # [1, 2, 3]

# XXX 之后的数据
print(rhyme[2:]) # [3, '你好']

# 可以加多一个参数，表示跨度（跨多少个元素选择）
print(rhyme[0:4:2]) # [1, 3]

# 更简洁的语法，忽略开始跟结束的位置，直接写跨度
print(rhyme[::2]) # [1, 3]

# 逆序数处
print(rhyme[::-2]) # ['你好', 2]



# 🔥列表的方法(增)
heros = ['钢铁侠', '蜘蛛侠', '绿巨人']
heros.append('蝙蝠侠') # append 每次只能添加一个元素
heros.extend(['美国队长', '雷神']) # extend 可以添加多个元素, 参数必须是一个可迭代对象
heros[len(heros):] = ['奇异博士'] # 在末尾加上一个元素
heros[len(heros):] = ['绿灯侠', '鹰眼'] # 在末尾加上多个元素
heros.insert(3, '海王') # 在指定位置插入一个元素


# 🔥列表的方法(删)
heros.remove('海王') # 删除指定元素
heros.pop(0) # 删除指定位置的元素
# heros.clear() # clear 清空全部列表


# 🔥列表的方法(改)


# 🔥列表的方法(查)