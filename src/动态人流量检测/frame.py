# -*- coding:utf8 -*-
import cv2
import os
import shutil
 
 
def get_frame_from_video():
    """
    Args:
        video_name:输入视频名字
        interval: 保存图片的帧率间隔
    Returns:
    """
    path=os.path.split(os.path.realpath(__file__))[0]
    input=path+"/video"
    dirs=os.listdir(input)
    interval = 5
     # 视频文件名字
    for dir in dirs:
        suffix=os.path.splitext(dir)[1].lower()
        print(suffix)
        if(suffix!=".mp4"):
            continue
        video_name=os.path.join(input,dir)

        # 保存图片的路径
        save_path = path+"/video_out/"
#        save_path = video_name.split('.mp4')[0] + '/'
        is_exists = os.path.exists(save_path)
        if not is_exists:
            os.makedirs(save_path)
            print('path of %s is build' % save_path)
        else:
            shutil.rmtree(save_path)
            os.makedirs(save_path)
            print('path of %s already exist and rebuild' % save_path)
     
        # 开始读视频
        video_capture = cv2.VideoCapture(video_name)
        i = 0
        j = 0
     
        while True:
            success, frame = video_capture.read()
            i += 1
            if i % interval == 0:
                # 保存图片
                j += 1
                save_name = save_path + str(j) + '_' + str(i) + '.jpg'
                cv2.imwrite(save_name, frame)
                cv2.imshow('f',frame)
                c = cv2.waitKey(1)
                if c == 27:
                    break
                print('image of %s is saved' % save_name)
            if not success:
                print('video is all read')
                break
 
 
#if __name__ == '__main__':
#    path=os.path.split(os.path.realpath(__file__))[0]
#    input=path+"/video"
#    dirs=os.listdir(input)
#    # 视频文件名字
#    for dir in dirs:
#        suffix=os.path.splitext(dir)[1].lower()
#        print(suffix)
#        if(suffix!=".mp4"):
#            continue
#        filepath=os.path.join(input,dir)
#        interval = 5
#        get_frame_from_video(filepath, interval)
