# torch.nn
nn.Parameter	# 张量子类 表示可学习参数
nn.Module	# 网络层基类 管理网络属性
nn.functional	# 卷积 池化 激活等函数具体实现
nn.init	# 参数初始化方法

# containers
nn.Sequetial	# 按顺序包装多个网络层
nn.ModuleList	# 将多个网络层打包为list 常用于大量重复网络的构建
nn.ModuleDict	# 将多个网络层打包为dict 选择特定网络层进行前向传播
