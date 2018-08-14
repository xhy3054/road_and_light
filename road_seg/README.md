## 简介
  本文档记载用segnet网络对玉泉公园的人行道进行分割的方法。（二分类）

## 具体步骤

### 安装caffe-segnet
首先需要配置Segnet版本的caffe，Segnet作者提供两个版本的支持segnet架构的caffe，分别是[caffe_v1](https://github.com/alexgkendall/caffe-segnet)与[caffe_v2](https://github.com/TimoSaemann/caffe-segnet-cudnn5)，经过测试，推荐使用第二个版本，无代码错误，只需配置好路径与本机环境即可正常编译。然后caffe的安装可以参考网上诸多的教程，根据自己电脑cudnn的版本等选择合适教程。此步骤请确保caffe的python接口可以正常使用。

### segnet目录结构
作者设计的segnet的目录结构如下

	/SegNet/
		image/
			test/
			testannot/
			train/
			trainannot/
			test.txt
			train.txt
		Models/
			# SegNet and SegNet-Basic model files for training and testing
		Scripts/
			compute_bn_statistics.py
		caffe-segnet/
			# caffe implementation
  
其中，`image/train.txt`与`image/test.txt`指定图像数据存放的位置，`Models`文件夹中放置一些网络参数文件。

### 快速开始
1. 将caffe-segnet安装好;
2. 将目录结构设置成指定格式;
3. 利用提供好数据、网络文件、参数文件直接进行最后一步验证环节进行效果测试;

### 数据准备
1. 首先去玉泉公园拍摄照片;
2. 将原照片都裁剪成指定大小，并指定命名;
3. 使用[labelme](https://github.com/wkentaro/labelme)对照片进行标注;
4. 生成指定格式`.txt`文件;

注：labelme标注的图片需要人工将图片改成`unsigned char`格式。

### 训练
在修改好配置文件中的路径信息后，即可进行训练。（还需要新建一个文件夹用来存储训练产生的权重文件 `mkdir /Segnet/Models/Training`）

	./SegNet/caffe-segnet/build/tools/caffe train -gpu 0 -solver /SegNet/Models/segnet_solver.prototxt  # This will begin training SegNet on GPU 0
	./SegNet/caffe-segnet/build/tools/caffe train -gpu 0 -solver /SegNet/Models/segnet_solver.prototxt -weights /SegNet/Models/VGG_ILSVRC_16_layers.caffemodel  # This will begin training SegNet on GPU 0 with a pretrained encode

如上，训练时需要`caffe`是caffe成功编译安装后产生的，`/SegNet/Models/segnet_solver.prototxt`是配置文件，其中指定了使用的网络文件，训练的迭代次数，每次载入的数据量等等。其中指定了训练的网络配置文件`segnet_train.prototxt`，此文件中除了网络参数的设置之外，还指明了训练数据位置文件。

运行`Scripts/compute_bn_statistics.py`将生成的权重文件转换成可用的格式`/SegNet/Models/Inference/test_weights.caffemodel`：

	python compute_bn_statistics.py ~/SegNet/Models/segnet_train.prototxt ~/SegNet/Models/Training/segnet_iter_5000.caffemodel ~/SegNet/Models/Inference/

### 验证
使用训练好的模型对现有图片进行分割测试（路径自行修改）：	

	python ~/SegNet/Scripts/test_segmentation_camvid.py --model ~/SegNet/Models/segnet_inference.prototxt --weights ~/SegNet/Models/Inference/test_weights.caffemodel --iter 59

其中59是本次测试的图片数量。segnet的分割结果我放在了`p_show`文件夹下。
