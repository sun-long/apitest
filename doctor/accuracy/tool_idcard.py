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
        
  
def generate_ground_truth(path_dir,ground_truth_file_name):
    """生成初始ground_truth文件，将文件夹内数据导入"""
    fileList=os.listdir(path_dir)
    ground_truth_data={}
    for i in fileList:
        ground_truth_data[i]={"name":"",
                              "number":""}
    with open(ground_truth_file_name,"w") as f:
        json.dump(ground_truth_data,f)

def generate_test_image(path_dir,test_image_file_name):
    """生成test_image文件，将文件夹内的数据导入"""

    fileList=os.listdir(path_dir)
    test_image_data={
        "image_path_t":[],
        "image_path_f":[]
    }
    for i in fileList:
        file_name=os.path.join(path_dir,i)
        test_image_data["image_path_t"].append(file_name)
    # with open(test_image_file_name,"w") as f:
    #     json.dump(test_image_data,f)
    import codecs
    with codecs.open(test_image_file_name, 'w', encoding="utf-8") as f:
        json.dump(test_image_data, f, indent=4, ensure_ascii=False)




if __name__=="__main__":

    #统一文件夹名称
    # path_dir=f"/Users/weishuting/scp/viper/data/身份证/2022-12-28-送标文件"
    # main_file_name=f"idcard"
    # index=0
    # uniform_file_name(path_dir=path_dir,main_file_name=main_file_name,index=index)

    #生成初始ground_truth
    # path_dir=f"/Users/weishuting/scp/viper/data/身份证/2022-12-28-送标文件"
    # ground_truth_file_name=f"/Users/weishuting/scp/viper/data/身份证/2022-12-28-送标文件/ground_truth.json"
    # generate_ground_truth(path_dir=path_dir,ground_truth_file_name=ground_truth_file_name)

    #生成test_image文件
    path_dir=f"/Users/weishuting/scp/2023-1-11-质量精度"
    test_image_file_name=f"/Users/weishuting/scp/2023-1-11-质量精度/test_image.json"
    generate_test_image(path_dir=path_dir,test_image_file_name=test_image_file_name)



 
    