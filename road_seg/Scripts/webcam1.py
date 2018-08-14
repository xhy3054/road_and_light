#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import os.path
import scipy
import argparse
import math
import cv2
import sys
import time

# 为Python添加默认模块搜索路径
sys.path.append('/usr/local/lib/python2.7/site-packages')       
# Make sure that caffe is on the python path:
# caffe模块要在Python的路径下;
# 这里我们将把caffe 模块添加到Python路径下.
caffe_root = '/home/yzhou79/SegNet/caffe-segnet-cudnn5/'
sys.path.insert(0, caffe_root + 'python')
import caffe

# Import arguments
#创建一个解析对象
parser = argparse.ArgumentParser()
#向该对象中添加你要关注的命令行参数和选项
parser.add_argument('--model', type=str, required=True)
parser.add_argument('--weights', type=str, required=True)
parser.add_argument('--colours', type=str, required=True)
args = parser.parse_args()


net = caffe.Net(args.model,     # 定义模型结构
                args.weights,   # 包含了模型的训练权值
               caffe.TEST)     # 使用测试模式(不执行dropout)

caffe.set_mode_gpu()

input_shape = net.blobs['data'].data.shape
output_shape = net.blobs['argmax'].data.shape

label_colours = cv2.imread(args.colours).astype(np.uint8)


'''视频
#cap = cv2.VideoCapture('/home/inin-h7-blackhole/SegNet/Example_Models/myvideo.mp4')
#cap = cv2.VideoCapture(0) 
# Change this to your webcam ID, or file name for your video file

rval = True

while rval:
	start = time.time()
	rval, frame = cap.read()

        if rval == False:
            break

	end = time.time()
'''


'''图片  
inputPath = '/home/inin-h7-blackhole/Stein_private/image_2/'  
outputPath = '/home/inin-h7-blackhole/Stein_private/image_2_rgb/'  
  
for i in range(695):  
    start = time.time()  
    frame = cv2.imread(inputPath+"%06d"%i+'.png')  
  
    end = time.time()  

'''
start = time.time()  
frame = cv2.imread('/home/yzhou79/picture/test.jpg')  
  
end = time.time()  
print '%30s' % 'Grabbed  frame in ', str((end - start)*1000), 'ms'

start = time.time()
frame = cv2.resize(frame, (input_shape[3],input_shape[2]))
input_image = frame.transpose((2,0,1))
# input_image = input_image[(2,1,0),:,:] # May be required, if you do not open your data with opencv
input_image = np.asarray([input_image])
end = time.time()
print '%30s' % 'Resized image in ', str((end - start)*1000), 'ms'

start = time.time()
out = net.forward_all(data=input_image)
end = time.time()
print '%30s' % 'Executed SegNet in ', str((end - start)*1000), 'ms'

start = time.time()
segmentation_ind = np.squeeze(net.blobs['argmax'].data)
segmentation_ind_3ch = np.resize(segmentation_ind,(3,input_shape[2],input_shape[3]))
segmentation_ind_3ch = segmentation_ind_3ch.transpose(1,2,0).astype(np.uint8)
segmentation_rgb = np.zeros(segmentation_ind_3ch.shape, dtype=np.uint8)

cv2.LUT(segmentation_ind_3ch,label_colours,segmentation_rgb)
segmentation_rgb = segmentation_rgb.astype(float)/255

end = time.time()
print '%30s' % 'Processed results in ', str((end - start)*1000), 'ms\n'

#cv2.imshow("Input", frame)
#cv2.imshow("SegNet", segmentation_rgb)
cv2.imwrite('/home/yzhou79/picture/'+'1.png',segmentation_rgb*255)  
key = cv2.waitKey(1)


