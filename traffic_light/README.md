## 简介
本文档记载使用ssd网络对交通红绿灯进行识别的方法。

## 具体步骤

### 安装ssd-caffe
ssd的作者使用caffe框架进行ssd的开发。并在github上提供了ssd版本的[caffe](https://github.com/weiliu89/caffe/tree/ssd)。第一步便是安装 ssd-caffe 。这与 segnet-caffe 的安装方式基本一致，重新来一遍即可。

### 目录结构
`ssd`作者有些不修边幅，提供的代码比较杂乱，所以不建议照搬。建议此处使用与`segnet`相似的目录结构:

	/SSD/
		data/
			# .lmdb 
		Models/
			# ssd model files for training and testing
		Scripts/
			train_ssd_lisa.py
			ssd_trafficlight.py
		caffe-ssd/
			# caffe implementation


### 数据准备
由于数据采集的困难，所以此次使用了[LISA](http://cvrr.ucsd.edu/vivachallenge/index.php/traffic-light/traffic-light-detection/)提供的交通灯检测官方数据集。

训练自己的数据集，数据处理需要首先采集图片数据，然后用标注软件进行标注。标注结果如下：

	class_index x_min y_min x_max y_max

将其中图像全都放到一个`Images`的文件夹里，图像的标注信息全部放入`Labels`的文件夹里。然后在此同级目录下运行`creat_list.sh`来生成`trainval.txt`, `test.txt`和`test_name_size.txt`等文件。这些文件中内容形式如下：

	Images/0001.jpg Labels/0001.txt

然后：

	bash ./data/create_data.sh

便可以生成`trainval.lmdb`与`test.lmdb`了。

### 训练SSD

	python train_ssd_lisa.py

注意:设置好路径和数据集名称等。

### 使用SSD模型进行检测

	python ssd_trafficlight.py

注意：此处检测代码我是放到caffe根目录下运行的，所以运行时注意路径。

