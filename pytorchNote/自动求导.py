# 计算图
概念:用来描述运算的有向无环图
原理:loss对w的导数(w.grad)=loss到w所有路径的导数的和
组成:
	结点Node:张量
	边Edge:运算
分类:
	静态图:先搭建图,再运算
	动态图:图的搭建和运算同时进行

# 注意
每次求导之后梯度不会自动清零(每次反向传播后会与原有梯度叠加)
叶子节点的父节点requires_grad都为True(要对该节点求导得到叶子节点的梯度)
叶子节点不能进行in_place操作(会导致反向传播拿到改变后的数据)

# 自动求导
torch.autograd.backward(	# 使用loss.backward()时自动调用该函数
	tensors,	# 用于求导的张量
	grad_tensors=None,	# 多个loss时 设置梯度的权重
	retain_grad=None,	# 保存计算图
	create_graph=False	# 创建导数的计算图 用于高阶求导
	)
torch.autograd.grad(
	outputs,	# 需要求导的张量 loss
	inputs,		# 需要梯度的张量 w/x
	create_graph=False,
	retain_grad=None,
	create_graph=None,
	)

# 反向传播函数
loss.backward(
	retain_grad=True,	# 设置该参数即可进行两次反向传播求二阶导数
	gradient=weight_t	# 传入与loss相同size的权重张量 为各部分loss的梯度设置不同权重
	)

# 梯度清零
w.grad.zero_()