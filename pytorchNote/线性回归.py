# 确定模型
y=w*x+b
# 损失函数
MSE: 1/m*sum(pow(y_p-y_t))
# 求解梯度并更新模型参数
w = w - LR * w.grad
b = b - LR * b.grad