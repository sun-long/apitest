#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rtsp_check.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/21 下午2:09   wangan      1.0         None
'''

# pip install opencv-python
# import cv2

rtsp_list = [
    "rtsp://10.198.21.115:8554/175236_new.264",
    "rtsp://10.211.41.108:8554/175236_new.264",
    "rtsp://10.53.4.12:8554/175236_new.264",
    "rtsp://10.53.4.176:8554/175236_new.264",
    "rtsp://10.53.5.22:8554/175236_new.264",
    "rtsp://10.53.6.118:8554/175236_new.264",
    "rtsp://10.53.7.217:8554/175236_new.264",
]


def get_img_from_camera_net(rtsp, name):
    cap = cv2.VideoCapture(rtsp)
    i = 1
    while i < 2:
        ret, frame = cap.read()
        _path = name + "_" + str(i) + '.jpg'
        cv2.imwrite(_path, frame)  # 存储为图像
        i += 1
    cap.release()

def get_img_from_camera_net_1(rtsp, name):
    cap = cv2.VideoCapture(rtsp)
    i = 1
    while i < 200:
        ret, frame = cap.read()
        if frame is None:
            continue
        else:
            cv2.imwrite(name, frame)  # 存储为图像
            break
        i += 1
    cap.release()

def check():
    failed_list = []
    for rtsp in rtsp_list:
        try:
            name = rtsp.split("/")[-1].split(".")[0]
            get_img_from_camera_net(rtsp, name)
            print("%s ok!" % rtsp)
        except:
            failed_list.append(rtsp)
            print("%s failed!" % rtsp)
    print("-----------------------------")
    print("Failed List:")
    for x in failed_list:
        print(x)

if __name__ == '__main__':
    check()
