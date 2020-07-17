# in_place操作
在原始内存中改变该数据

# 查看地址
id(t)

# 用这种方法统一设置随机种子
def set_seed(seed=1):
	random.seed(seed)
	np.random.seed(seed)
	torch.manual_seed(seed)
	torch.cuda.manual_seed(seed)

# 将data中所有元素随机排序
random.shuffle(data)

# 根据现有张量和条件创建bool类型的张量
bool_t = t.ge(5)	# 大于等于5

# 保留计算图非叶子节点的梯度
t.retain_grad()	# 在计算前调用该方法

# 设置学习率下降策略
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)


# 静态类方法 可被类和对象调用
# 方法中不能使用类的方法和属性
@staticmethod
def method_name():
	return 

# 线性回归
# 确定模型
y=w*x+b
# 损失函数
MSE: 1/m*sum(pow(y_p-y_t))
# 求解梯度并更新模型参数
w = w - LR * w.grad
b = b - LR * b.grad

# 逻辑回归
# 确定模型(线性二分类模型)
y=1/(1+torch.exp(-z))	# sigmoid/logistic函数
z = WX+b

# 机器学习模型训练步骤
数据:
	数据收集
	数据划分
	数据读取
	数据预处理
/模型/损失函数/优化器/迭代训练

# epoch/iteration/batchsize
epoch:所有训练样本都已经输入到模型中一次=1个epoch
iteration:一批样本输入到模型中一次=1个iteration
batch_size:一批样本中的样本数量