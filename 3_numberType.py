import decimal # 十进制模块, 能让浮点数更精准
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
print(a + b) 



# 整数、小数、浮点数
print(6 / 2) # 3.0


# 浮点数，会有精度的误差，比如 0.1 + 0.2 != 0.3
print(0.1 + 0.2) # 0.30000000000000004


#复数
x = 1 + 2j
print(x.real) # 实部
print(x.imag) # 虚部


# 🔥特殊的除法（地板除 比如 3 / 2 = 1），确保两个数相除的结果一定是整数，不是则向【下】取整！！比目标结果小！！
print(3 // 2) # 1
print(-3 // 2) # -2


# 🔥求余数
print(3 % 2) # 1
print(6 % 2) # 0, 因为能够整除，所以余数为 0
print(8 % 5) # 3


# 🔥同时求出地板除跟余数
print(divmod(3, 2)) # (1, 1)


# 🔥求绝对值
xx = -520
print(abs(xx)) # 520


# 🔥截取小数取整
print(int(3.1415926)) # 3


# 🔥转化成浮点数
print(float(520)) # 520.0


# 🔥计算 x 的 y 次方 (有两种方法)
print(pow(2, 3)) # 8
print(2 ** 3) # 8

