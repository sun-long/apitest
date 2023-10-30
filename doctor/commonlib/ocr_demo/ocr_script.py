#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ocr_script.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/26 下午12:18   wangan      1.0         None
'''
import json
import os

import easyocr


class EasyOcr(object):
    def __init__(self):
        # 设置识别中英文两种语言
        self._reader = easyocr.Reader([
            # 'ch_sim',
            'en'
        ], gpu=False)  # need to run only once to load model into memory

    def readImage(self, image_path):
        """ 读取图片,返回识别结果"""
        result = self._reader.readtext(image_path, detail=0)
        return result



def traversal_files(path):
    file_list = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            file_list.append(name)

    print("file num:%s" % len(file_list))
    return file_list


def gen_json(file_list, ff_dir, save_path):
    res = {}
    eo = EasyOcr()
    for file in file_list:
        name = file.split(".")[0]
        ocr_res = eo.readImage(os.path.join(ff_dir, file))
        ocr_time = None
        for r in ocr_res:
            if ":" in r:
                ocr_time = r
                break
        # res[name] = {
        #     "all": ocr_res,
        #     "time": ocr_time
        # }
        res[name] = ocr_time
        print("[%s][%s]:%s" % (name, ocr_time, ocr_res))
    save_json(res, save_path)


def save_json(data, save_path):
    data = json.dumps(data, sort_keys=True, indent=2)
    with open(save_path, 'w') as f:
        f.write(data)
    print("文件写入成功.path:%s" % save_path)


if __name__ == '__main__':
    ff_dir = "/home/SENSETIME/wangan/belt/ff"
    save_path =  "/home/SENSETIME/wangan/belt/ff.json"
    file_list = traversal_files(ff_dir)
    gen_json(file_list, ff_dir, save_path)