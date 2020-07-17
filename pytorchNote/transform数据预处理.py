# 常用图像预处理方法
torchvision.transform
# 常用数据集的dataset实现 MNIST/CIFAR-10/ImageNet等
torchvision.datasets
# 常用的模型预训练 AlexNet/VGG/ResNet/GoogLeNet等
torchvision.model

# 将多个图像预处理/数据增强操作打包
train_transform = transforms.Compose([
	# 从图像中心将图像裁剪为32*32 若尺寸变大填充黑色
	transforms.CenterCrop((32,32))
	# 随机裁减
	transforms.RandomCrop(
		size=(32,32),
		padding=None,	#a:上下左右; (a,b):上下/左右; (a,b,c,d):左/上/右/下
		pad_if_need=False,	# 若图像小于设定的size 进行填充
		padding_mode='constant',	# 单一像素填充
					# edge:根据边缘像素填充
					# reflect:镜像填充(不包含边缘像素)
					# symmetric:镜像填充(包含边缘像素)
		fill=(0,0,0)	# constant时填充的像素值
		)
	# 随即整形裁减
	transforms.RandomResizedCrop(
		size=(),
		scale=(0.08,1.0),	# 随即裁剪的面积比例
		ratio=(3/4,4/3),	# 随机裁剪长宽比
		interpolation	# 插值方法
					# PIL.Image.NEAREST
					# PIL.Image.BILINEAR
					# PIL.Image.BICUBIC
		)
	# 从图像四个角点和中心点裁减出尺寸为size的五张照图像
	transforms.FiveCrop(size)
	# 将五张照片反转得到十张图像
	transforms.TenCrop(
		size，
		vertical_filp=False	# false时水平反转 true时垂直反转
	)
	# 根据概率随机水平反转
	transforms.RandomHorizontalFlip(p=0.5)
	# 根据概率随机垂直反转
	transforms.RandomVerticalFlip(p=0.5)
	# 随机旋转图片
	transforms.RandomRotation(
		degrees,# a时，在(-a,a)之间选择角度随机旋转
			# (a,b)时，在(a,b)之间选择角度随机旋转
		resample=False,	# 重采样方法
		expand=False,	# 是否扩大图像保证旋转后不丢失角点信息
		center=None）	# 选择则旋转点 默中心
	# 对图像边缘进行填充
	transforms.Pad(	# 参数使用与RandomCrop类似
		padding,
		fill=0,
		padding_mode='constant')
	# 调整亮度/对比度/饱和度/色相
	transforms.ColorJitter(
		brightness=0,	# 为a时 从[max(0, 1-a),1+a]中随机选择
				# 为(a,b)时 从[a,b]中随机选择
		contrast=0,	# 同上
		saturation=0,	# 同上
		hue=0)	# 为a时 从[-a, a]中随机选择	
			# 为(a,b)时 从[a, b]中随机选择
			# 0<=a<=b<=0.5
	# 根据概率将图像转换为灰度图
	transforms.RandomGrayscale(
		num_output_channels,	# 输出通道数只能为1或3
		p=0.1	# 概率值
		)
	# 图像转换为灰度图
	transforms.Grayscale(num_output_channels)
	# 对图像进行仿射变换
	transforms.RandomAffine(
		degrees,	# 旋转角度随机区间
		translate=None,	# 平移区间(width, height) 取值(0,1)
		scale=None,	# 缩放比例随机区间(面积为单位)
		shear=None,	# a:x轴斜切(-a,a)区间中随机角度
				# (a,b):x斜切(-a,a) y斜切(-b,b)
				# (a,b,c,d):x斜切(-a,b) y斜切(-c,d)
		resample=False,	# 重采样方式 NEAREST/BILINEAR/BICUBIC
		fillcolor=0	# 填充的颜色数值
		)
	# 对图像进行随机遮挡
	transforms.RandomErasing(
		p=0.5,	# 执行遮挡操作的概率
		scale=(0.02, 0.33)，	# 遮挡区域的面积比
		ratio=(0.3,3,3),	# 遮挡区域的长宽比
		value=0,	# 遮挡区域的RGB像素值/255(或'random')
		inplace=False
	)
	transforms.Resize((32,32))	# 图像整形为32*32
	transforms.ToTensor()	# 图像转换为Tensor 并归一化
	# 数据标准化 传入每个通道的mean和std 得到0均值1方差的标准化数据
	transforms.Normalize(mean=[0.41,0.42,0.43], std=[0.3,0.32,0.31],)
	transforms.Lamba()	# 匿名函数
	])

# 将预处理操作求逆
# 传入预处理后的图像张量 和 transform对象
img = transform_invert(img_tensor, train_transform)

# 对transforms操作
# 从几个transforms中随机挑一个
transforms.RandomChoice([transforms1, transforms2, transform3])
# 随机执行一组transforms
transforms.RandomApply([transforms1, transforms2, transform3], p=0.5)
# 对一组transforms打乱顺序
transforms.RandomOrder([transforms1, transforms2, transform3])
