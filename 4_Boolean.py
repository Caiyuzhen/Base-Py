# 🔥布尔类型, 为 false 的情况有：空字符串、 0、 None、Decimal(0)、Fraction(0, 1)、[]、()、{}、set()、range(0)
import decimal # 十进制模块, 能让浮点数更精准
print(bool(250)) # True
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(0j)) # False
print(bool(decimal.Decimal(0)))
print(bool('A')) # True
print(bool('')) # False
print(bool({})) # False
print(bool([])) # False
print(bool(set())) # False
print(bool(range(0))) # False
print(1 == True) # True
print(0 == False) # True



# 🔥布尔运算（逻辑运算, 都遵循短路运算逻辑）
# and 与, 左右同时为 True 才为 True
# or 或, 左右有一个为 True 就为 True
# not 非, 取反
print(3 < 4 and 5 < 6) # True
print(3 < 4 or 5 > 6) # True
print(not True) # False
print(not 0) # True


# 🔥短路运算, 从左往右, 当第一个值无法确定逻辑结果时,才对第二个数进行求值
print(0 and 1) # 0, 因为 0 为 False, 所以不用再判断 1 了, 因为都是数字所以会抛出数字
print(0 or 1) # 1, 因为 0 为 False, 还要再判断 1 , 因为都是数字所以会抛出数字


# 🔥运算符的优先级, lambda > if-else > or > and > not > (>= != == < ) > | > ^ > & ......