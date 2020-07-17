# 用来调整学习率的类
class _LRScheduler(object):
	def __init__(self, optimizer, last_epoch=-1):
		self.optimizer = None	# 关联的优化器
		self.last_epoch = None	# 记录epoch数
		self.base_lrs = None	# 记录初始学习率
	
# 自定义类继承_LRScheduler类
class MyScheduler(_LRScheduler):
	def __init__(self):
	
	# 调用即可更新学习率
	def step():
		return
		
	# 计算并返回学习率 该函数被step调用
	# 重写父类方法
	def get_lr():
		return
		
# 常用学习率调整方法
# 有序调整
# 每过step_size次epoch将lr减小为gamma倍
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1, last_epoch=-1)
# 按照给定的间隔milestones调整学习率 milestones为list
scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones, gamma=0.1, last_epoch=-1)
# 按指数衰减调整学习率 gamma为指数的底
scheduler = torch.optim.lr_scherduler.ExponentialLR(optimizer, gamma, last_epoch=-1)
# 余弦周期调整学习率 T_max为1/2周期 eta_min为学习率下限
scheduler = torch.optim.lr_scherduler.CosineAnnealingLR(optimizer, T_max, eta_min=0, last_epoch=-1)

# 自适应调整
scheduler = torch.optim.lr_scherduler.ReduceLROnPlateau(
	optimizer, 
	mode='min',	# min为监控指标是否下降 max相反
	factor='0.1'，	# 调整系数(gamma)
	patience=10， # 监控指标连续10次不变化则调整学习率
	verbose=False,	# 是否打印日志
	threshold=0.0001,
	threshold_mode='rel',
	cooldown=0,	# lr变换后 下次进行监控的cd
	min_lr=0,	# 学习率下限
	eps=1e-08,	# 学习率衰减最小值
	last_epoch=-1)

# 自定义调整 
# lr_lambda为function或list
scheduler = torch.optim.lr_scherduler.lambdaLR(optimizer, lr_lambda, last_epoch=-1)

# 更新学习率
scheduler.step()
		
