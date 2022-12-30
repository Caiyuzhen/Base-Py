# 集合
# 🔥集合也具备推导式
a = {res for res in "World"} #会随机推导出来，无序的
print(a)

# 🔥集合是无序的，所以不能够用索引来取值！！

# 🔥可以使用 in 跟 not 来判断是否存在
print("W" in a) # True
print("W" not in a) # False


# 🔥可以使用迭代的方式来遍历集合
for i in a:
	print(i)


# 🔥集合具备唯一性(可以用来去重！), 用 set() 方法！！
result = set([1,1,2,3,3,4,5,6,7,7,8,8,8,8,9])
print(result)


# 🔥创建一个不可变的集合(只读)
frozenset({"a","b","c"})


# 🔥往集合内添加某个数据
b = {'1', '2', '3'}
b.add('4')
print(b) # 1, 2, 3, 4



# 🔥删除集合内的某个数据
b.remove('4') # remove 不存在的数据会报错
b.discard('8') # discard 不存在的数据不会报错



# 🔥【字典】的【键】【集合】的数据必修是【可哈希】的！
#获取哈希值(不可变的对象才能具备哈希值)
print(hash(1.0002))