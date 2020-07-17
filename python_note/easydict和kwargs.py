# EasyDict
from easydict import EasyDict
# 创建easydict
ed = EasyDict()
# 用现有dict创建easydict
d = {'num1':10, 'num2':20}
ed = edict(d)
# 访问/创建easydict元素
ed.num1
ed.num2

# 位置参数/关键字参数
# 注意三种参数的顺序
def fun(x, *args, **kwargs):
	print(x)
	print(args)
	print(kwargs)
# 调用时传入多参数
fun(1,2,3,4,a=10,b=20)
# 输出
1
(2,3,4)	# 把没名字的参数打包成tuple
{'a':10, 'b':20}	# 把带名字的参数打包成dict
# 也可以使用**运算符直接传入dict
fun(1,2,3,4,**ed)

