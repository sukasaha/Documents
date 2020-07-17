import os

# 路径拼接 自动补全/
path = os.path.join('data')

# 返回path目录下的文件/文件夹列表
listdir(path)

# 在代码中直接创建目录
makedir(dir_name)	# tql

# 路径中文件的遍历
# 会按照树结构依次遍历当前目录和所有子目录
for (root, dirs, files) in os.walk(path):
	print(root)	# 当前遍历目录的路径
	print(dirs)	# 当前目录中子目录列表
	print(files)	# 当前目录中文件列表

# 设置当前使用的GPU设备名称为'/gpu:0'
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
