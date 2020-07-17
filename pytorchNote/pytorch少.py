# pytorch官网
https://pytorch.org/

# 导入pytorch包
import torch

# 测试cuda是否可用
torch.cuda.is_available()

# 张量的创建和初始化
# 生成随机张量
torch.rand(5,3)
# 生成空张量 (初始化的元素为内存中初始值)
torch.empty(5,3)
# 生成张量并声明类型
torch.zeros(5, 3, dtype=torch.long)
# 从现有的数据结构生成张量
torch.tensor([5.5, 3])
# 从现有的张量x创建张量 属性继承x 可覆写
torch.randn_like(x, dtype=torch.float)
# 从数据结构创建指定数据类型的tensor
torch.FloatTensor(list1)

# 张量运算
# 返回张量形状(tuple类型)
x.size()
# 增量运算简单写法 相当于有y=y+x
y.add_(x)
# 张量变形为3行5列
x.view(3,5)
# 单元素张量转化为数值
x.item()

# torch张量常用运算
# 相加并以另一个张量z作为输出
torch.add(x, y, out=z)
# 计算两个矩阵乘积
torch.mm(tensor1, tensor2)
# 绝对值 正弦 等math函数
torch.abs(tensor)
torch.sin(tensor)

# autograd包 用来计算反向传播 梯度下降
from torch.autograd import Variable
# 从torch张量创建variable 并指定是否进行梯度下降
var = Variable(tensor, requires_grad=True)
# 查看variable的值
# 使用variable进行特定运算
v_out = torch.mean(var*var)
# 根据var表达式(上式)计算v_out梯度
v_out.backward()
# 查看梯度 d(v_out)/d(var)=(1/4)*2*var
var.grad

torch.Tensor
.grad_fn
.requires_grad 设置为True
.backward()
.grad
.detach()
torch.no_grad()
Function

# torch.nn包 用来搭建神经网络
nn.Module
forward(input)

# torch张量 numpy张量相互转换
torch_tensor = torch.from_numpy(np_tensor)
np_tensor = torch_numpy.numpy()

