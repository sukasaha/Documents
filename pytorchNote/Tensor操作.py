# 拼接
torch.cat(	# 在已有维度dim上进行拼接
	tensors=[t1,t2,t3],
	dim=0,
	out=None
	)

torch.stack(	# 将dim作为新的维度进行拼接
	tensors=[t1,t2,t3],
	dim=0,
	out=None
	)

# 切分
torch.chunk(	# 平均切分
	input,	# 要切分的张量
	chunks=10,	# 要切分的份数
	dim=0,	# 要切分的维度
	)

torch.split(
	tensor,	# 要切分的张量
	split_size_or_sections,	# int时表示每一份的长度 list时按照list切分
	dim=0
	)

# 抽取并拼接
torch.index_select(
	input,	# 要操作的张量
	dim,	# 要索引的维度
	index，	# 要从dim中抽取并拼接的索引，必须为1维tensor
	out=None
	)
torch.masked_select(	# 将input中所有符合mask的元素拼接成1维的张量并返回
	input,
	mask,	# 与input同形状的bool类型的张量
	out=None
	)

# 变形
torch.reshape(	# 张量在内存中连续，新旧张量共享内存
	input,
	shape	# 使用-1可以自动计算该维度的size
	)

# 交换维度
torch.transpose(
	input,
	dim=1,
	dim=0
	)

# 压缩/扩展张量维度
torch.squeeze(	# 去掉长度为1的维度
	input,
	dim=None,	# 若指定dim,仅当dim维度长度为1时,将dim维度移除
	out=None
	)

torch.unsqueeze(	# 根据dim扩展维度
	input,
	dim=1,
	out=None
	)