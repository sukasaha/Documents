# 序列化:将内存中的模型对象编码保存到硬盘中
# 保存整个对象 速度慢/占用空间大
torch.save(
	obj,	# 要保存的对象
	f		# 输出路径
)
# 只保存参数和权重
state_dict = net.state_dict()
torch.save(state_dict, path)

# 反序列化L:将硬盘中的模型解码为内存中的模型对象
# 加载整个模型
torch.load(
	f,				# 路径
	map_location	# 指定存放位置 cpu/gpu
)
# 加载参数和权重
# path为保存的state_dict文件的路径
s_d = torch.load(path, map_location=torch.device('cuda'))
net.load_state_dict(s_d)

# 断点续训练
# 保存当前训练信息
check_point = {
	'model_state_dict':net.state_dict(),	# 保存当前权重
	'optimizer_state_dict':optimizer.state_dict(),	# 保存当前优化器参数
	'epoch':epoch	# 保存当前迭代次数
}
torch.save(check_point, path)
# 断点恢复
check_point = torch.load(path)
net.load_state_dict(check_point['model_state_dict'])
optimizer.load_state_point(check_point['optimizer_state_dict'])
start_epoch = check_point['epoch']
scheduler.last_epoch = check_point['epoch']	# 为学习率更新提供当前迭代次数
