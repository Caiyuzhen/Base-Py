# 🔥把字符串反转
a = '你好呀'
print(a[::-1])





# 🔥字符串大小写
# 首字母大写(将会生成一个新的字符串)
b = "abc"
print(b.capitalize())

# 全部变成大写
print(b.upper())

# 全部变成小写
print(b.lower())





# 🔥字符串左中右对齐
# 左对齐
c = "这是一个对齐测试"
print(c.center(20))
print(c.center(20, '-'))

# 右对齐
print(c.rjust(20))
print(c.rjust(20, '*'))

# 左对齐
print(c.ljust(20))
print(c.ljust(20, '+'))




# 🔥字符串的查找(返回数量)
d = "上海自来水来自海上"
print(d.count("海")) # 2 个海字
print(d.count("海", 0, 5)) # 从 0 到 5 个字符里面有 1 个海字




# 🔥字符串的查找(返回索引)
print(d.find("海")) # 0
print(d.find("海", 1, 5)) # 从 1 到 5 个字符里面有 1 个海字, 返回索引 4




# 🔥字符串的替换
e = "你好吗？"
print(e.replace("你", "我")) # 我好吗？





# 🔥字符串的判断
# 判断起始字符
f = "你好吗？"
print(f.startswith("我")) # False
print(f.endswith("吗？")) # True

# 判断开头是否都为大写
g = "Hello World"
print(g.istitle()) # True

# 判断是否全部都为大写
print(g.isupper()) # False

# 判断是否全部由字母组成
print("Hello".isalpha()) # True

# 判断是否全部由数字组成
print("123".isdigit()) # True
print('123'.isdecimal()) # True

# 判断是包含数字
print("Hello123".isalnum()) # True





# 🔥字符串的截取
h = "  Hello World  "
# 左侧不要留空白
print(h.lstrip())

# 右侧不要留空白
print(h.rstrip())

# 左右两侧不要留空白
print(h.strip())


# 去除左侧的指定字符(单个字符)
g = "www.google.com"
print(g.lstrip("w."))	

# 去除右侧的指定字符(单个字符)
print(g.rstrip(".m"))

# 去除左右两侧的指定字符(单个字符)
print(g.strip("w.m"))


# 去除左侧的指定字符(多个字符)
print(g.removeprefix("www."))

# 去除右侧的指定字符(多个字符)
print(g.removesuffix(".com"))





# 🔥字符串的拆分
h = "www.google.com"

# 从左到右找到 . 然后切割为三分
print(h.partition("."))

# 从右到左找到 . 然后切割为三分
print(h.rpartition("."))

# 分割为三个元素，然后转化为列表（数组）
i = "苟日新,日日新,又日新"
print(i.split(','))

# 且为两个元素
print(i.split(',', 1))

# 按换行符分割
j = "苟日新\n日日新\n又日新"
print(j.splitlines())




# 🔥字符串拼接
k = "苟日新"
l = "日日新"
m = "又日新"
print('.'.join([k, l, m]))
print(''.join([k, l, m]))




# 🔥格式化字符串 (类比模板字符串)
# 单个参数
year = 2022
print("今年是 {} 年".format(year))

# 多个参数
result = "1+2={}, 2 的平方是{}, 3 的立方是{}".format(1+2, 2**2, 3*3*3)
print(result)

# 指定参数的位置
"{1} 看到 {0} 就很开心".format("小明", "小李") # 1 = 小李, 0 = 小明

# 指定参数的名称
"我叫 {name}, 我今年 {age} 岁".format(name="小明", age=18)




# 🔥格式化字符串的对齐方式
# 左对齐
k = '{left:>10}{right:<10}'.format(left=250, right=120) #10 为显示的宽度
print(k)

# 以二进制的形式输出
print('{:b}'.format(80)) # 1010000

# 以 Unicode 形式输出
print('{:c}'.format(80)) # P

# 以百分号的形式输出（包含小数点后 6 位的精度）
print("{:%}".format(0.98))

# 以百分号的形式输出（包含小数点后 2 位的精度）
print(("{:.2%}").format(0.98))

# 自定义精度⚡️
reslut2 = "{:.{prec}f}".format(3.1415926, prec=2) # 3.14
print(reslut2)


# F 语法糖, 在字符串前面加个 F, 可省略 format, 但是只兼容 3.6 以上的版本
name = "小明"
result3 = F"Hello {name} !" # Hello 小明
print(result3)


# 自定义格式化字符串的传参
num = 3.1415926
fill = "+"
align = "^"
width = "10"
prec = "3"
ty = "g"
result4 = F"{num:{fill}{align}{width}.{prec}{ty}}"

print(result4) # 3.14


# 判断是否包含某个字符串
print("水" in "水果") # True
print("水" not in "水果") # False


# 删除指定的对象
a = [1, 2, 3, 4, 5]
del a[0]
print(a)


# 把字符串转化为列表
b = "zen"
print(list(b)) # ['z', 'e', 'n']


# 找到最靠后的字符（大写在小写之前）
print(max('zen'))


# 🔥对列表进行排序 (由字符的少到多排序), ⚡️⚡️sorted 可以对任何可迭代对象进行排序
fruit = ['apple', 'pear', 'orange', 'banana']
print(sorted(fruit, key=len)) # ['pear', 'apple', 'orange', 'banana']


# 🔥对字符进行排序(元素，由小到大)
z = sorted((1,8,9,8,6,0))
print(z)


# 🔥反转字符
k = list(reversed((3,2,5)))
print(k) # (5, 2, 3)


# 🔥🔥将一个对象转化为一个可迭代对象
season = ['spring', 'summer', 'fall', 'winter']
n = list(enumerate(season))
print(n)


# 🔥过滤出小写字符
z = list(filter(str.islower, 'Hello World')) 
print(z)