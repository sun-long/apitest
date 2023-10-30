import ast
import os

dir_list = []



# 遍历目录
def walkDirectory(file):
    for root, dirs, files in os.walk(file):
        # root 表示当前访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历所有的文件夹
        i = 1
        for d in dirs:
            dir_list.append(os.path.join(root, d))
    for dir in dir_list:
        # 将文件中的receive_time写入到txt文件中
        walkFile(dir)


def walkFile(file):
    assginment = file.split("/")[7]
    file_list = []
    for root, dirs, files in os.walk(file):
        # root 表示当前访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for f in files:
            file_list.append(os.path.join(root, f))
    receive_time = []
    for alarm in file_list:
        with open(alarm) as f:
            data = f.read()
            # 将字符串转化成字典
            transdata = ast.literal_eval(data)
            receive_time.append(transdata['receive_time'])
            # 排序
            receive_time.sort()
    with open("{}.txt".format(assginment), "w") as fo:
        fo.write(str(receive_time))
        fo.close()
    jisuan(receive_time, assginment)


def jisuan(receive_time, assginment):
    flag = 1
    count = 0
    for i in receive_time:
        if count <= len(receive_time) - 2:
            if receive_time[count] + 60 > receive_time[count + 1]:
                flag = 1
                count = count + 1
                continue
            else:
                print(receive_time[count], receive_time[count + 1], "两次告警时间之差大于60秒")
                flag = 0
                count = count + 1
                continue
        else:
            break
    if flag == 1:
        print("{}告警时间差小于60秒".format(assginment))
    else:
        print("请检查，{}有部分告警时间差大于60秒".format(assginment))

#测试前，修改此目录即可
def main():
    walkDirectory("/home/SENSETIME/liangchen.vendor/liangchen/belt/msg_bak")


if __name__ == '__main__':
    main()
    print("打印目录个数", len(dir_list))
    # print("打印assginment个数")
