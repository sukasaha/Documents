# 参数解析器
import argparse

# 创建解析器
parser = argparse.ArgumentParser(
	# 对输入参数的描述
	description='how to give parameters using argparse',
	# 指定一个格式化类来定制帮助信息的格式
	formatter_class=argparse.ArgumentDefaultsHelpFormatter
	)
	
# 添加参数
parser.add_argument(
	'-l',
	'--learning-rate',
	type=float,
	metavar='LR',
	default=0.001，
	help='Learning rate',
	dest='learning_rate'	
	)
	
# 传参方法
python3 test.py -l 0.1
python3 test.py --learning-rate 0.1

# 使用传入的参数
args = parser.parse_args()
args.learning_rate	# 使用的是dest参数

# 将传入的参数转换为dict
args_dict = vars(parser.parse_args())
args_dict.keys()	# key为dest参数
args_dict.values()	# value为传入的参数值

