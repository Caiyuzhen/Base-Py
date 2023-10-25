def my_adder(x, y):
    return x + y




class ShoppingList:
	"""初始化购物清单, shopping_list 是字典类型, 包含商品名和对应价格, 例如 {"牙刷": 5, "电池": 10}"""
	def __init__(self, shopping_list):
		self.shopping_list = shopping_list
		self.total_price = 0 # 初始化总价为 0
  
	"""返回购物车上有多少商品"""
	def get_item_count(self):
		return len(self.shopping_list) # len 为内置函数, 返回列表的长度

	"""返回购物清单商品价格总额"""
	def get_total_price(self):
		total_price = 0
		for price in self.shopping_list.values(): # values() 为字典内的方法, 返回字典的值
			total_price += price
		return total_price
        