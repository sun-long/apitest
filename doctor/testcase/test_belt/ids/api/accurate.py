import requests
import base64
import json
import os
import random
import xlwt
import time

mTime = time.strftime('%Y年%m月%d日')
mWorkBook = xlwt.Workbook()
mWorkSheet = mWorkBook.add_sheet(mTime)

column = 0
row = 0


def errorStyle():
    font = xlwt.Font()
    font.name = 'name Times New Roman'
    font.colour_index = 1

    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 2

    myStyle = xlwt.XFStyle()
    myStyle.font = font
    myStyle.pattern = pattern
    return myStyle

def get_file_path_by_name():
    '''
    获取指定路径下所有文件的绝对路径
    '''
    L = []
    for root, dirs, files in os.walk(r"D:/CRD/apitest/resource/images/go_image/ids_face/accuracy/liveness"):  # 获取所有文件
        for file in files:  # 遍历所有文件名
            if os.path.splitext(file)[1] == '.jpg':   # 指定尾缀 
                L.append(os.path.join(root, file))  # 拼接处绝对路径并放入列表
                L.sort()
    # print('总文件数目：', len(L))
    # print(L)
    return L

# 遍历接口

def iterateApi():
    
    for i in range(len(get_file_path_by_name())):
        url = "https://demos.visioncloudapi.com/ids-wrapper/v1/face/detect_liveness"
        with open(get_file_path_by_name()[i], 'rb') as f:
                base64_data = base64.b64encode(f.read())
                image = base64_data.decode()
                body =   {
                    "disable_defake": True,
                    "encrypt_info": {
                        "algorithm": "ENCRPT_ALGORITHM_NONE",
                        "data": "string",
                        "encrypted_fields": [
                        "string"
                        ],
                        "iv": "string",
                        "version": 0
                    },
                    "image": image,
                    "min_quality_level": "NORMAL"
                }
                data = json.dumps(body)
                r = requests.post(url= url, data=data)
                _, filename = os.path.split(str(f))
                print("filename:", filename.strip("'>"), "| liveness_score:", r.json()["liveness_score"])
                getResult(filename.strip("'>"), r.json()["liveness_score"])


# 处理返回结果
def getResult(filename,
              liveness_score
             ):
    global column
    if (column == 0):
        mWorkSheet.write(column, 0, "filename")
        mWorkSheet.write(column, 1, "liveness_score")
    column += 1
    writeSheet(filename, liveness_score)

    
# 保存到excel
def writeSheet(filename, liveness_score, error=False):
    if error is True:
        myStyle = errorStyle()
    else:
        myStyle = xlwt.XFStyle()
    mWorkSheet.write(column, 0, filename, myStyle)
    mWorkSheet.write(column, 1, liveness_score, myStyle)

if __name__ == "__main__":
    iterateApi()
    mWorkBook.save(mTime + ".xls")
