# 查看gpu信息
# cuda是否可用
torch.cuda.is_available()
# 查看gpu个数
torch.cuda.device_count()
# 查看当前设备索引
torch.cuda.current_device()
# 查看gpu型号
torch.cuda.get_device_name(0)	# param:设备索引号 默认为0
# 为当前gpu设置随机种子
torch.cuda.manual_seed()
# 为当前所有gpu设置随机种子
torch.cuda.manual_seed_all()
# 生成一个设备的引用
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# 设置当前使用的GPU设备名称为'/gpu:0'
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
# 设定特定gpu为逻辑gpu 其中逻辑gpu0为主cpu 进行计算的分发/回收
os.environ.setdefault('CUDA_VISIBLE_DEVICES', '2,3')	# 将物理gpu2 gpu3设置为逻辑gpu0 gpu1


# 查看张量/模型信息
# 使用to函数转换数据类型/设备
t = torch.ones((3,3))
L = nn.Linear(2,2)
# 查看张量属性
t.device	# 查看张量所在设备'cpu'/'cuda:0'
t.is_cuda	# true/false
id(t)		# 查看内存地址
# 转换张量的数据类型
t = t.to(torch.float64)
# 转换张量的设备
t = t.to('cuda')
# 查看模型属性
id(L)	# 查看模型地址
next(L.parameters()).is_cuda()	# next()可以返回模型参数的张量
# 转换模型中可训练参数的数据类型
L.to(torch.float64)
# 模型迁移到gpu上
L.to(torch.device('cuda'))


# 多cpu分发并行
torch.nn.DataParallel(
	module,		# 需要并行分发的模型 该函数被调用后该模型可被并行分发计算
	device_ids=None,	# 要分发的设备 默认分发到所有逻辑gpu
	output_device=None,	# 结果输出设备
	dim=0
	)

