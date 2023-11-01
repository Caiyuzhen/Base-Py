""" 
	assert 
 		用于判断代码的执行逻辑是否符合预期
   
	场景
		1.单元测试 => 测试接口返回的数据
  		2.接口测试 => 判断别人传进来的参数是否符合我这个接口的预期
"""


assert type(1) is int
assert 1+1 == 2

arr = [1,2,3]
assert len(arr) > 3 # 会报错



def aInterface(name, age, score):
    assert type(name) is str
    assert type(age) is int
    assert type(socre) is float

aInterface("Jimmy", 26, 99.8)
    