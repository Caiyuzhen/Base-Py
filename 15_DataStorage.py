# 🔥🔥🔥数据存储(把数据存储到硬盘上)

# ⛰️修改 ——————————————————————————————————————————————————————————————————
# 🔥打开文件
f = open('TheBest.txt', 'w') # 默认创建在主文件夹下、打开的模式('w' 为写入模式)
f.write('🎉Hello World!') # 操作文件, 把单个字符串写入到文件中
f.writelines(['😄The long words.'])# 把多个字符串写入到文件中, 如有需要需要自己添加换行符  \n
f.close() # ⚡️关闭文件对象后，输入才会从缓冲区写入到文件中



# 🔥重新打开文件！！重新写点内容进去（⚡️注意，文件被关闭后就无法写入了，要重新打开！）
# 🔥打开文件的方式一:
f = open('TheBest.txt', 'r+') # 重新打开文件, 写入新内容(⚡️⚡️用'r', 这样才不会重新截断！！)
f.write('👀New words~') # 操作文件, 写入新的内容s
# print(f.readable()) 



# 🔥打开文件的方式二:
from pathlib import Path
g = Path.cwd()
g = g / "TheBest2.txt"
gg = g.open('w')
gg.write('👋你好呀')
gg.flush()




# 🔥🔥🔥用 with 语句打开文件(不需要手动的关闭文件!!!)
with open('TheBest4.txt', 'w') as vv:
	vv.write('🐱这是一个新内容')  # ⚡️⚡️⚡️不需要手动的关闭文件!!!




# 🔥🔥🔥永久的把 Python 对象存(字符串、元组、序列、字典等) 储到文件中！！序列化（转为二进制的格式）
import pickle

x, y, z = 43, 44, 45
aa = 'Zen'
ll = ['Hey', 996, 3.14]
dd = {'name': 'Zen', 'age': 18}

with open('data.pkl', 'wb') as kkn: # 🔥 用 .pkl 的形式（存储为二进制文件）
	pickle.dump(x, kkn)
	pickle.dump(y, kkn)
	pickle.dump(z, kkn)
	pickle.dump(aa, kkn)
	pickle.dump(ll, kkn)
	pickle.dump(dd, kkn)
	# pickle((x, y, z, aa, ll, dd), kkn) # 更简便的写法: 打包为元组


with open('data.pkl', 'rb') as kkn: # 🔥 用 .pkl 读取二进制文件
	x = pickle.load(kkn)
	y = pickle.load(kkn)
	z = pickle.load(kkn)
	aa = pickle.load(kkn)
	ll = pickle.load(kkn)
	dd = pickle.load(kkn)
	# x, y, z, aa, ll, dd = pickle.load(kkn) # 更简便的写法: 把元组解包

print(x, y, z, aa, ll, dd, sep = '\n') # ⛰️ sep = '\n' 为换行




# 🔥文件可以被迭代、文件指针
# 迭代完毕后，【⚡️⚡️文件光标】指向文件末尾！！可以通过 f.tell() 来查看文件指针的位置
for i in f:
	print(i) # 此时 👀New words~ 还没被写入！！

print(f.tell())#⚡️ 查看【文件光标】的位置(停留在哪个字符的位置)
f.seek(0)# ⚡️重置【文件光标】的位置！




f.close() # ⚡️关闭文件对象后，输入才会从缓冲区写入到文件中




# 🔥在不关闭的情况下写入文件内容
f = open('TheBest.txt', 'r+')
f.write("🚗It's new words")
f.flush() # ⚡️刷新缓冲区，把内容写入到文件中


# 🔥截取文件内容(删除文件内容到哪一行）
# f.truncate(29) # 一:指定光标的位置来截取
# f = open('TheBest.txt', 'w') # 二: 重新用 w 模式打开（🔥就会清空之前的内容！）






# 🔥🔥路径文件(相对路径，相对于当前文件夹，绝对路径，相对于系统根目录)
from pathlib import Path
x = Path.cwd()
print(x)

# 🔥把文件加到某个路径下
y = x / "TheBest.txt"






# ⛰️新增 ——————————————————————————————————————————————————————————————————
# 🔥创建文件夹
n = x / 'NewFolder'
# n.mkdir() # ⚡️⚡️⚡️创建文件夹(⛰️⛰️如果文件夹已经存在，⚠️⚠️就会报错！)


# 🔥如果父级路径不存在，则会报错，要想不报错的话可以用 exist_ok=True
n = x / 'NewFolder/A/B/C'
n.mkdir(parents=True, exist_ok=True)





# 🔥修改文件夹名称
n.rename('TheBestNewName98')

# 🔥修改文件名称
m = Path('TheBest2.txt')
m.replace('TheBest3.txt')








# ⛰️查询 ——————————————————————————————————————————————————————————————————
# 🔥判断一个路径是否是文件夹
print(x.is_dir()) # True，是文件夹

# 🔥判断一个路径是否是文件
print(y.is_file()) # True，是文件

# 🔥判断一个路径是否存在
z = Path('C/404').exists() # False，不存在
print(z) # False

# 🔥获取路径的后缀
print('文件后缀:',y.suffix)

# 🔥获取文件的【最后一部分】
print('文件最后一部分:', y.name)

# 🔥获取文件名
print('文件名:', y.stem)

# 🔥获取文件的【父级目录】
print('父级目录:', y.parent)

# 🔥获取文件的所有父级目录
zz = y.parents
for each in zz:
	print(each) # 打印所有路径
	print(zz[2]) # 打印其中一条路径

# 🔥查询文件、文件夹的信息、可以用来查询文件尺寸
print(y.stat().st_size) # st_xxxx ... 里边有各种方法

# 🔥相对路径转化为绝对路径
print(y.resolve())

# 🔥获取当前路径下的所有子文件夹、及子文件, 将会返回一个 generator object 生成器
print(list(x.iterdir())) # 生成器对象，需要转化为 list

print('__分割线__')

# 🔥过滤出当前路径下的所有文件
res = [xx for xx in x.iterdir() if xx.is_file()]
print(res)



h = Path('.')
h.glob('%.txt') # ⚡️⚡️⚡️获取当前路径下的所有 .txt 文件
list(h.glob('*/*.py')) #获取当前路径下的所有下一级目录的 .py 文件
list(h.glob('**/*.py')) #获取当前路径下、以及所有子目录的下一级目录的 .py 文件



# ⛰️删除 ——————————————————————————————————————————————————————————————————
# 🔥删除文件夹(前提是需要先删除里边的文件！)
pp = Path('TheBest4Folder')
# pp.unlink() # 删除后就没了，所以会报错
# pp.parent.rmdir() # 删除后就没了，所以会报错

