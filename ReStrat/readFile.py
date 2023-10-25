"""
	读取
		read 返回全部文件内容的字符串
		readline 返回一行文件内容的字符串
		readlines 返回全部文件内容组成的【列表】 (然后再用 for 循环读出来)
  
	写入

"""
# 读取 ————————————————————————————————————————————————————————
# 方法一（需要手动关闭）
f = open('./files/data1.txt', "r", encoding="utf-8") # r 为读取, w 为覆盖写入, a 为追加, 🌟 r+ 为打开并追加
print(f.read()) # 读取文件
f.close()


# 方法二（会自动关闭）
with open('./files/data2.txt', "r", encoding="utf-8") as file:
    print(file.read())
    
with open('./files/data2.txt', "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        print(line)
        
        
        
# 写入 ————————————————————————————————————————————————————————
with open('./files/data3.txt', "r+", encoding="utf-8") as file: # r 为读取, w 为覆盖写入, a 为追加, 🌟 r+ 为打开并追加
	print(f"第一次读取: {file.read()}")
	file.write("Hey!!, \n 你好!!")
	file.seek(0)  # 🔥 将文件指针重新定位到文件开头 !! 否则会读为空文件 !!
	print(f"第二次读取: {file.read()}")
        
        