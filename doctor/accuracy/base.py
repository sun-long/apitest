import pytest
from requests import request
from commonlib.cache_dict import CacheDict
from commonlib.log_utils import log
from defines.belt.rasmanager_service_business import RasmanagerSwaggerBusiness
from defines.belt.face_service_business import FaceSwaggerBusiness
from defines.belt.adapter_service_business import AdapterSwaggerBusiness
from defines.belt.bill_service_business import BillSwaggerBusiness
from defines.belt.auth_service_business import AuthSwaggerBusiness
from defines.belt.user_service_business import UserSwaggerBusiness
from defines.belt.botmanager_service_business import BotmanagerSwaggerBusiness
from defines.belt.identity_service_business import IdentitySwaggerBusiness
from defines.belt.ocr_service_business import OcrSwaggerBusiness
from defines.belt.notificationinternal_service_business import NotificationinternalSwaggerBusiness
from defines.belt.device_service_business import DeviceSwaggerBusiness
from defines.belt.ipsocr_service_business import IpsocrSwaggerBusiness
from defines.belt.ipsapplet_service_business import IpsappletSwaggerBusiness
from defines.belt.notification_service_business import NotificationSwaggerBusiness
from commonlib.sign_utils import encode_jwt_token
import os
import cv2

@pytest.fixture(scope='function')
def FaceApi(config_obj, ext_info,aksk_token):
    """ FaceApi API """
    host_key = config_obj.EnvInfo.Service
    host=config_obj.get(host_key)    
    ak_sk = config_obj.EnvInfo.ak_sk
    ak=config_obj.get(ak_sk).ak    
    sk=config_obj.get(ak_sk).sk    
    aksk_token=encode_jwt_token(ak,sk)
    OcrApi=FaceSwaggerBusiness(host, token=aksk_token)




@pytest.fixture(scope='function')
def OcrApi(config_obj, ext_info,aksk_token):
    """ OcrApi API """
    host_key = config_obj.EnvInfo.Service
    host=config_obj.get(host_key)
    return OcrSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info,token=aksk_token)

@pytest.fixture(scope='function')
def IdentityApi(config_obj, ext_info,aksk_token):
    """ IdentityApi API """
    host_key = config_obj.EnvInfo.Service
    host=config_obj.get(host_key)    
    return IdentitySwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info,token=aksk_token)

def get_images_of_dir(pathdir):
    """获取文件夹下所有的iamge图片
    input param:pathdir,输入文件夹露肩
    output param:images,输出该文件夹（包括文件夹内的文件夹）下所有的文件"""
    images=[]
    images_suffix=['jpg','jpeg','bmp','png']
    for root, dirs, files in os.walk(pathdir):
        print("root", root)  # 当前目录路径
        print("dirs", dirs)  # 当前路径下所有子目录
        print("files", files)  # 当前路径下所有非目录子文件
        for i in files:
            if any(i.endswith(suffix) for suffix in images_suffix):
                file_name=os.path.join(root,i)
                images.append(file_name)
    return images
def uniform_file_name(path_dir,main_file_name,index):
    """统一文件夹内的文件名称，输入文件夹，统一名称，统一初始序号"""
    # path=input('请输入文件路径(结尾加上/)：')       

    #获取该目录下所有文件，存入列表中
    fileList=os.listdir(path_dir)
    for i in fileList:
        
        #设置旧文件名（就是路径+文件名）
        oldname=os.path.join(path_dir,i)
        
        suffix=os.path.splitext(i)[-1]
        index=index+1
        new_file_name=main_file_name+"_"+str(index)+suffix
        #设置新文件名
        newname=os.path.join(path_dir,new_file_name) 
        
        os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
        print(oldname,'======>',newname)

def generate_rotate_images_of_dir_to_another_dir(srcPathdir,dstPathdir,degree):
    """将文件夹下所有的文件进行旋转后存储到另外一个文件夹"""
    images=get_images_of_dir(srcPathdir)
    img_rotate=None
    for image in images:
        filename=os.path.split(image)[-1]
        img=cv2.imread(image)
        if degree=="90":
            new_file_name=os.path.splitext(filename)[0]+"_90"+os.path.splitext(filename)[-1]
            img_rotate=cv2.rotate(img,0)
        elif degree=="180":
            new_file_name=os.path.splitext(filename)[0]+"_180"+os.path.splitext(filename)[-1]
            img_rotate=cv2.rotate(img,1)
        elif degree=="270":
            new_file_name=os.path.splitext(filename)[0]+"_270"+os.path.splitext(filename)[-1]
            img_rotate=cv2.rotate(img,2)
        if not os.path.exists(dstPathdir):
            os.makedirs(dstPathdir)
        new_path=os.path.join(dstPathdir,new_file_name)
        cv2.imwrite(new_path,img_rotate)
def save_image_according_level(accuracy_dir,image_path,level):
    """根据图片的等级存储图片至accuracy文件夹
    accuracy_dir,dst精度结果文件夹
    image_path,src图片源路径文件夹
    level,图片质量等级"""
    dir_name_1=""
    if level=="EXTREMELY_HIGH":
        dir_name_1="EXTREMELY_HIGH"
    elif level=="HIGH":
        dir_name_1="HIGH"
    elif level=="NORMAL":
        dir_name_1="NORMAL"
    elif level=="LOW":
        dir_name_1="LOW"
    new_dir=accuracy_dir+"/"+dir_name_1
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    image_name=os.path.basename(image_path)
    new_name=os.path.join(new_dir,image_name)
    img=cv2.imread(image_path)
    cv2.imwrite(new_name,img)



if __name__=='__main__':
    srcPathdir=f"/Users/weishuting/scp/viper/data/人脸"
    dstPathdir=f"/Users/weishuting/scp/viper/data/人脸_旋转"
    generate_rotate_images_of_dir_to_another_dir(srcPathdir,dstPathdir,"270")