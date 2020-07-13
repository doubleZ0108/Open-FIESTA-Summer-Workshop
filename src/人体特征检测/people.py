import requests
import time
import hashlib
import base64
import json
import os
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
# 二进制方式打开图片文件
path=os.path.split(os.path.realpath(__file__))[0]
input=path+"/input"
dirs=os.listdir(input)



mbSize=1024*1024
##调整物理大小到4M以下
#for dir in dirs:
#    suffix=os.path.splitext(dir)[1].lower()
#    if(suffix!=".jpeg" and suffix!=".png" and suffix!=".BMP"):
#        continue
#    filepath=os.path.join(input,dir)
#    print(filepath)
#    image=Image.open(filepath)
#    size=os.path.getsize(filepath)/(mbSize)
#    width,height=image.size
#    while True:
#        if size>=4: #把大小变到25KB以下
#            width,height=round(width*0.9),round(height*0.9)
#            image=image.resize((width,height),Image.ANTIALIAS)
#         #   resizepath=input+"/"+str(width)+"*"+str(height)+suffix
#            image.save(filepath)
#            size=os.path.getsize(filepath)/(mbSize)
#        else:
#            break
#
#预处理完后开始ocr识别
for dir in dirs:
    suffix=os.path.splitext(dir)[1].lower()
    print(suffix)
    if(suffix!=".jpeg" and suffix!=".png" and suffix!=".BMP"):
        continue
    filepath=os.path.join(input,dir)
    print(filepath)
    f = open(filepath, 'rb')
    img = base64.b64encode(f.read())
    params = {"image":img}
    access_token = '24.30ecb7603c608cbf2174baaa674fd3b7.2592000.1596853127.282335-21205296'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    #result = str(response, 'utf-8')
    #print(result)
    if response:
        print (response.json())
    #json已经是字典了
    
    data=response.json()
    #从字典中获取数据
    top_lefts=[]
    right_bottoms=[]
    face_mask=[]
    gender=[]
    upper_color=[]
    glasses=[]
    for word in data['person_info']:
        top_lefts.append((word['location']['left'],word['location']['top']))
        right_bottoms.append((word['location']['left']+word['location']['width'],word['location']['top']+word['location']['height']))
        face_mask.append(word['attributes']['face_mask'])
        gender.append(word['attributes']['gender'])
        upper_color.append(word['attributes']['upper_color'])
        glasses.append(word['attributes']['glasses'])
     #加载图片
    img=cv2.imread(filepath)
     #加载字体
    fontpath=path+"/font.ttc"
    size=22 #字体大小
    # print(fontpath)
    font = ImageFont.truetype(fontpath, size)
    #设置参数
    color=[(0,156,0),(255,0,0),(0,0,255)] #字体和边框的颜色
    wide=2  #边框的粗细

    #cv2不能显示中文，故用pil
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    
    true_num=0;
    false_num=0;
    notsure = 0;

    color_now=color[0];
    #显示字体
    for index in range(len(top_lefts)):
        print(type(face_mask[index]['score']))
        if face_mask[index]['name']=='戴口罩':
            true_num=true_num+1
        if face_mask[index]['name']=='无口罩':
            false_num=false_num+1
            color_now=color[1]
        if face_mask[index]['name']=='不确定':
            notsure=notsure+1
            color_now=color[2]
        color_now=(255,255,255)
        draw.text((top_lefts[index][0],top_lefts[index][1]+10),face_mask[index]['name']+" "+str(round(face_mask[index]['score'],2)),font = font, fill = color_now)
        draw.text((top_lefts[index][0],top_lefts[index][1]+30),gender[index]['name']+" "+str(round(gender[index]['score'],2)),font = font, fill = color_now)
        draw.text((top_lefts[index][0],top_lefts[index][1]+50),upper_color[index]['name']+" "+str(round(upper_color[index]['score'],2)),font = font, fill = color_now)
        draw.text((top_lefts[index][0],top_lefts[index][1]+70),glasses[index]['name']+" "+str(round(glasses[index]['score'],2)),font = font, fill = color_now)

     #   print(index)
        
    #添加人数
    print(img.shape[0],img.shape[1])
    draw.text((img.shape[1]-300,0),"总人数: "+str(data['person_num']),font =ImageFont.truetype(fontpath, 42),fill =(225,128,64))
    draw.text((img.shape[1]-300,45),"戴口罩: "+str(true_num),font =ImageFont.truetype(fontpath, 42),fill =color[0])
    draw.text((img.shape[1]-300,90),"无口罩: "+str(false_num),font =ImageFont.truetype(fontpath, 42),fill =color[1])
    draw.text((img.shape[1]-300,135),"不确定: "+str(notsure),font =ImageFont.truetype(fontpath, 42),fill =color[2])


    

    img=np.array(img_pil)
    #显示边框
    for index in range(len(top_lefts)):
        if face_mask[index]['name']=="戴口罩":
            cv2.rectangle(img,top_lefts[index],right_bottoms[index],color[0],wide)
        elif face_mask[index]['name']=="无口罩":
            cv2.rectangle(img,top_lefts[index],right_bottoms[index],color[1],wide)
        elif face_mask[index]['name']=="不确定":
            cv2.rectangle(img,top_lefts[index],right_bottoms[index],color[2],wide)

    #保存
    outputPath=path+"/image/"+dir
    cv2.imwrite(outputPath, img)

