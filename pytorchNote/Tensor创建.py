# Variable定义
Variable:用于求导,对Tensor的封装(pytorch0.4.0中取消)
	data:包装的Tensor数据
	grad:data的梯度
	grad_fn:创建Tensor的Function
	requires_grad:是否需要梯度
	if_leaf:是否是叶子节点

# Tensor定义
Tensor(pytorch0.4.0之后的张量):
	data:
	dtype:张量的数据类型
		torch.float16(half)			torch.cuda.HalfTensor
		torch.float32(float)		torch.cuda.FloatTensor
		torch.float64(double)		torch.cuda.DoubleTensor
		torch.uint8					torch.cuda.ByteTensor
		torch.int8					torch.cuda.CharTensor
		torch.int16(short)			torch.cuda.ShortTensor
		torch.int32(int)			torch.cuda.IntTensor
		torch.int64(long)			torch.cuda.LongTensor
		torch.bool					torch.cuda.BoolTensor
	shape:
	device:GPU/CPU
	requires_grad:
	grad:
	grad_fn:
	is_leaf:

# Tensor的创建
torch.tensor(
	data,	# 可以是list,ndarray
	dtype=None,	# 类型为ndarray类型
	device=None,	# cuda/cpu
	requires_grad=False,
	pin_memory=False,	# 是否存于锁页内存
	)

torch.from_numpy(
	ndarray		# 创建出来的Tensor会与ndarray共享内存
	)

torch.zeros(
	size,
	out=t,	#将生成的张量赋值给t
	layout=torch.strided,	# 稀疏矩阵用torch.sparse_coo可提高读取效率
	device=None,
	requires_grad=False
	)

torch.zeros_like(
	input,	# 根据input形状创建全0张量
	dtype=None,
	layout=None,
	device=None,
	requires_grad=False
	)

torch.ones()
torch.ones_like()
torch.full(fill_value)	# 填充任意值 其他参数相同
torch.full_like(fill_value)

torch.arange(	# 创建等差数列
	start=0,	# 数列包含start
	step=1,		# 公差
	end=10,		# 数列不包含end
	)

torch.linspace(
	start=0,	# 包含start
	end=1,		# 包含end
	steps=10	# 数列元素个数
	)

torch.logspace(		# 创建对数均分的1维张量
	start=0,
	end=1,
	steps=10,	# 数列元素个数
	base=10		# 对数的底
	)

torch.eye(	# 单位对角矩阵
	n=5,	# 矩阵行数
	m=None	# 矩阵列数一般省略 创建方阵
	)

torch.normal(	# 正态分布(高斯分布)
	mean=0,	# mean为张量时可以给不同元素设置不同均值
	std=0.5,	# std为张量时可以给不同元素设置不同标准差
	size=None,
	out=None
	)

torch.randn(size)	# 标准正态分布
torch.randn_like()	# 指定形状的标准正态分布
torch.rand(size)	# [0,1)区间上的均匀分布
torch.rand_like()
torch.randint(low,high,size)	# [low,high)区间上整数的均匀分布
torch.randint_like()
torch.randperm(n)	# 生成从0到n-1的随机排列(常用做乱序索引)
torch.bernoulli(input)	# 输出概率值 生成伯努利分布
