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
heros[0] = '灭霸'
heros[0:2] = ['武松', '鲁智深', '林冲']

result = [7,2,5,8,3,1,6,4]
result.sort() # 从小到大排序
result.reverse() # 从大到小排序


# 🔥列表的方法(查)
nums = [3,7,3,8,4,0,3,1,6,2,4,3]
print(nums.count(3)) # 查询数组中有多少个 3
print(nums.index(3)) # 查询 3 第一次出现的位置, index（x,start,end)
print(nums.index(3, 1,5)) # 从位置 1 到 5 查询 3 第一次出现的位置

nums2 = nums.copy() # 复制数组 (浅拷贝)
nums3 = nums[:] # 用切片的方式复制数组 (浅拷贝)


# 🔥列表的方法(相加)
s = [1,2,3]
t = [4,5,6]
c = s + t
print(c) # [1, 2, 3, 4, 5, 6]
print(c * 3) # 重复 3 次


# 🔥 嵌套列表
matrix = [[999,2], [3,4,5]] # 写法一
matrix2 = [[999,2], 
		  [3,4,5]] # 写法二
print(matrix, matrix2)


# 🔥访问嵌套列表
for i in matrix:
	for k in i:
		print(k, end=' ') # 999 2 3 4 5, ⚡️ end=' ' 表示加个空格, 让结果更直观

print(matrix[0][0])



# 🔥检测两个对象是否是同一个内存索引的对象
x = [1,2]
y = [1,2]
print(x is y) # false


# 🔥深拷贝
import copy
zz = [1,2]
yy = copy.deepcopy(zz) # 深拷贝
print(zz is yy) # False



# 🔥列表推导式 (比如每个元素都 X 2)
# 简陋的方案
List = [8,9]
for i in range(len(List)):#⚡️⚡️分配每个元素的索引值, 比如这里就是获得了索引值为 0、1, 然后 i = 0, i = 1!!
	List[i] = List[i] * 2
print(List)

# 列表推导式的方法 (👍从程序上速度更快！)
List2 = [8,9]
List2 = [i * 2 for i in List2]
print(List2)
