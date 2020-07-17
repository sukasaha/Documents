# Sampler:生成索引
# Dataset:根据索引找到数据和标签

# 构建可迭代的数据装载器
torch.utils.data.DataLoader(
	dataset,	# Dataset对象,数据来源
	batch_size=1,
	num_works=0,	# 是否多进程读取数据
	shuffle=False,	# 每个epoch是否乱序
	drop_last=False	# 样本数不能被batch_size整除时 是否舍弃最后一批数据
	)

# torch.utils.data.Dataset类
# 继承Dataset类时必须重写__getitem__函数
class Dataset(object):
	# 接收索引 返回样本
	def __getitem__(self, index):
		raise NotImplementedError

	def __add__(self, other):
		return ConcatDataset([self, other])

# 创建自己的Dataset类
# 具体看例子my_dataset.py
class MyDataset(torch.utils.data.Dataset):
	def __init__(self, data_dir, transform=None):
		self.label=		# 记录所有分类的标签
		self.data_info=		# 该数据集
		self.transform = transform

	# 此函数必须被重写
	def __getitem__(self, index):
		# 根据索引得到图片 标签 并返回
		return img, label

# 构建MyDataset实例
train_data = MyDataset(data_dir=train_dir, transform=train_transform)
valid_data = MyDataset(data_dir=valid_dir, transform=valid_transform)

# 通过传入MyDataset实例 构建DataLoder
train_loader = DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)
valid_loader = DataLoader(dataset=valid_data, batch_size=BATCH_SIZE)

# 遍历DataLoader进行训练等操作
# enumerate迭代器可以同时去到索引i和数据data
for i,data in enumerate(train_loader):
	pass

	