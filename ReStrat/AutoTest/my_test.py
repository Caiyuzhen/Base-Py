# unittest 测试框架（内置的） => 🚀 使用 【-m unittest my_test.py】 来运行, 会自动运行所有以 test 开头的函数!!
"""
	assertEqual 方法用于断言两个值是否相等
 	assertNotEqual 方法用于断言两个值是否不等
   	assertTrue 方法用于断言一个值为 True
	assertFalse 方法用于断言一个值为 False
 	assertIsNone 方法用于断言一个值为 None
   	assertIn 方法用于断言一个序列中包含某个值
	assertNotIn 方法用于断言一个序列中不包含某个值
		比如 assertNotIn(2 not in[1,3 -1])
"""
import unittest 

from product import my_adder # 被测试的函数

class TestMyAdder(unittest.TestCase): # 使用继承自 unittest.TestCase 的类来编写测试用例
	def test_positive_with_positive(self): # 要测试的代码需要用 test 开头
		self.assertEqual(my_adder(5, 3), 8) # assertEqual 为 unittest 内的方法
  
	def test_negative_with_positive(self): # 要测试的代码需要用 test 开头
		self.assertEqual(my_adder(5, -3), 2) # assertEqual 为 unittest 内的方法
    
    
    
    
    
    
from product import ShoppingList

class TestShoppingList(unittest.TestCase): # 🔥记得以 Test 开头！
	def setUp(self):
		self.shopping_list = ShoppingList({"纸巾": 8, "牙刷": 5, "电池": 10})
	
	def test_get_item_count(self):
		self.assertEqual(self.shopping_list.get_item_count(), 3)
  
	def test_get_total_price(self):
		self.assertEqual(self.shopping_list.get_total_price(), 23)

