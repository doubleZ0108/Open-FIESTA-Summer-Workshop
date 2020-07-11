import requests
import time
import hashlib
import base64
import json
import os
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

def image():
    #获取一张图片的宽高作为视频的宽高
    path=os.path.split(os.path.realpath(__file__))[0]
    input=path+"/output"
    dirs=os.listdir(input)
    print(dirs)
    dirs.remove('.DS_Store')
    dirs.sort(key=lambda x:int(x.split('.')[0]))
    print(dirs)

    # 视频文件名字
    filepath=os.path.join(input,dirs[0])
    image=cv2.imread(filepath)
    cv2.imshow("new window", image)   #显示图片
    image_info=image.shape
    height=image_info[0]
    width=image_info[1]
    size=(height,width)
    print(size)
    fps=5
    fourcc=cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter('ss.mp4', cv2.VideoWriter_fourcc(*"mp4v"), fps, (width,height)) #创建视频流对象-格式一

    #video = cv2.VideoWriter('ss.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width,height)) #创建视频流对象-格式二

    """
    参数1 即将保存的文件路径
    参数2 VideoWriter_fourcc为视频编解码器
        fourcc意为四字符代码（Four-Character Codes），顾名思义，该编码由四个字符组成,下面是VideoWriter_fourcc对象一些常用的参数,注意：字符顺序不能弄混
        cv2.VideoWriter_fourcc('I', '4', '2', '0'),该参数是YUV编码类型，文件名后缀为.avi
        cv2.VideoWriter_fourcc('P', 'I', 'M', 'I'),该参数是MPEG-1编码类型，文件名后缀为.avi
        cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),该参数是MPEG-4编码类型，文件名后缀为.avi
        cv2.VideoWriter_fourcc('T', 'H', 'E', 'O'),该参数是Ogg Vorbis,文件名后缀为.ogv
        cv2.VideoWriter_fourcc('F', 'L', 'V', '1'),该参数是Flash视频，文件名后缀为.flv
        cv2.VideoWriter_fourcc('m', 'p', '4', 'v')    文件名后缀为.mp4
    参数3 为帧播放速率
    参数4 (width,height)为视频帧大小

    """
    for dir in dirs:
        filepath=os.path.join(input,dir)
        image=cv2.imread(filepath)
        video.write(image)  # 向视频文件写入一帧--只有图像，没有声音
    cv2.waitKey()
