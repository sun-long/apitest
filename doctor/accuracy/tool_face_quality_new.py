import os
import json
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
        
  
def generate_ground_truth(path_dir,ground_truth_file_name,quality_level):
    """生成初始ground_truth文件，将文件夹内数据导入"""
    fileList=os.listdir(path_dir)
    ground_truth_data={}
    for i in fileList:
        ground_truth_data[i]={"face_quality_level":quality_level}
    with open(ground_truth_file_name,"a") as f:
        json.dump(ground_truth_data,f)

def generate_test_image(path_dir,test_image_file_name):
    """生成test_image文件，将文件夹内的数据导入"""

    fileList=os.listdir(path_dir)
    test_image_data={
        "image_path_t":[],
        "image_path_f":[]
    }
    images_suffix=['jpg','jpeg','bmp','png']
    for root, dirs, files in os.walk(path_dir):
        print("root", root)  # 当前目录路径
        print("dirs", dirs)  # 当前路径下所有子目录
        print("files", files)  # 当前路径下所有非目录子文件
        for i in files:
            if any(i.endswith(suffix) for suffix in images_suffix):
                file_name=os.path.join(root,i)
                test_image_data["image_path_t"].append(file_name)
    # with open(test_image_file_name,"w") as f:
    #     json.dump(test_image_data,f)
    import codecs
    with codecs.open(test_image_file_name, 'w', encoding="utf-8") as f:
        json.dump(test_image_data, f, indent=4, ensure_ascii=False)




if __name__=="__main__":

    ##统一文件夹名称
    # path_dir=f"/Users/weishuting/Downloads/2023-3-21-人脸质量等级数据集/NORMAL"
    # main_file_name=f"face_normal"
    # index=0
    # uniform_file_name(path_dir=path_dir,main_file_name=main_file_name,index=index)

    #生成初始ground_truth
    # path_dir=f"/Users/weishuting/Downloads/2023-3-21-人脸质量等级数据集/NORMAL"
    # ground_truth_file_name=f"/Users/weishuting/Downloads/2023-3-21-人脸质量等级数据集/ground_truth.json"
    # generate_ground_truth(path_dir=path_dir,ground_truth_file_name=ground_truth_file_name,quality_level="NORMAL")


    # path_dir=f"/Users/weishuting/Downloads/2023-3-21-人脸质量等级数据集/HIGH"
    # ground_truth_file_name=f"/Users/weishuting/Downloads/2023-3-21-人脸质量等级数据集/ground_truth.json"
    # generate_ground_truth(path_dir=path_dir,ground_truth_file_name=ground_truth_file_name,quality_level="HIGH")


    # path_dir=f"/Users/weishuting/Downloads/2023-3-21-人脸质量等级数据集/LOW"
    # ground_truth_file_name=f"/Users/weishuting/Downloads/2023-3-21-人脸质量等级数据集/ground_truth.json"
    # generate_ground_truth(path_dir=path_dir,ground_truth_file_name=ground_truth_file_name,quality_level="LOW")


    path_dir=f"/Users/weishuting/scp/清晰度/wangxinyan"
    ground_truth_file_name=f"/Users/weishuting/scp/清晰度/ground_truth.json"
    generate_ground_truth(path_dir=path_dir,ground_truth_file_name=ground_truth_file_name,quality_level="EXTREMELY_HIGH")

    # ##生成test_image文件
    # path_dir=f"/Users/weishuting/scp/清晰度"
    # test_image_file_name=f"/Users/weishuting/scp/清晰度/test_image.json"
    # generate_test_image(path_dir=path_dir,test_image_file_name=test_image_file_name)



 
    