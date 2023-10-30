#!/usr/bin/env python
# -*-coding: utf-8 -*-

import hashlib
import os
import re
import json
import time
import signal
import socket

import struct
import shutil
import uuid
from commonlib import system
from commonlib.decorator import wait
from commonlib.log_utils import log


def get_env_var(var_name):
    """
    @note: get env variable by name
    """
    cmd = "env | grep %s" % var_name
    ret, output, err = system.ci_system(cmd, output=True)
    if ret != 0 or output == "":
        return None

    return output.split(var_name + '=')[-1].strip()

def scp_dir(src_path, remote_path, host, port=22, username="root", password="root"):
    """
    :param src_path:
    :param remote_path:
    :param host:
    :param port:
    :param username:
    :param password:
    :return:
    """
    import paramiko
    from scp import SCPClient
    result, error_msg = True, ""
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(host, port, username, password)
        scpclient = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)
        scpclient.put(src_path, remote_path, recursive=True)
    except Exception as e:
        result = False
        error_msg = str(e)
    finally:
        ssh_client.close()
    return result, error_msg


def ssh_scp_get(remote_file, local_file, ip, port=22, user='root', password="root"):
    """
    :param ip:
    :param port:
    :param user:
    :param password:
    :param remote_file:
    :param local_file:
    :return:
    """
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, user, password)
    a = ssh.exec_command('date')
    stdin, stdout, stderr = a
    print(stdout.read())
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp = ssh.open_sftp()
    sftp.get(remote_file, local_file)


def RemoteScp(remote_path, local_path, host_ip, host_port=22, host_username="root", host_password="root"):
    """
    :param host_ip:
    :param host_port:
    :param host_username:
    :param host_password:
    :param remote_path:
    :param local_path:
    :return:
    """
    import paramiko
    scp = paramiko.Transport((host_ip, host_port))
    scp.connect(username=host_username, password=host_password)
    sftp = paramiko.SFTPClient.from_transport(scp)
    try:
        remote_files = sftp.listdir(remote_path)
        for file in remote_files:   # 遍历读取远程目录里的所有文件
            local_file = local_path + file
            remote_file = remote_path + file
            sftp.get(remote_file, local_file)
    except IOError:   # 如果目录不存在则抛出异常
        return "remote_path or local_path is not exist"
    finally:
        scp.close()


def exec_cmd(cmd, client_info=None):
    """ 执行cmd命令"""
    if client_info:
        # if not cmd_utils.ping_ip(self.client_info["ip"]):
        #     raise Exception("%s ping不通" % self.client_info["ip"])
        ret, output, err = ssh_cmd(cmd,
                                   client_info["ip"],
                                   port=client_info["port"],
                                   username=client_info["username"],
                                   password=client_info["password"])
    else:
        # res = os.popen(cmd)
        # output_str = res.read()
        ret, output, err = system.ci_system(cmd, logger=None, loglevel='info',
                                            prompt='cmd', output=True)
    return ret, output, err

def ssh_cmd(cmd, host, port=22, username="root", password="root"):
    """
    :param cmd:
    :param host:
    :param port:
    :param username:
    :param password:
    :return:
    """
    import paramiko
    ret, msg, err = True, "", ""
    # ssh = paramiko.SSHClient()  # 创建SSH对象
    transport = paramiko.Transport((host, int(port)))
    ssh = paramiko.SSHClient()
    try:
        # 建立连接
        transport.connect(username=username, password=password)
        # 将sshclient的对象的transport指定为以上的transport
        ssh._transport = transport
        # 执行命令，和传统方法一样
        stdin, stdout, stderr = ssh.exec_command(cmd)

        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
        # ssh.connect(hostname=host, port=port, username=username, password=password)  # 连接服务器
        # stdin, stdout, stderr = ssh.exec_command(cmd)  # 执行命令并获取命令结果
        # # stdin为输入的命令
        # # stdout为命令返回的结果
        # # stderr为命令错误时返回的结果
        res, err = stdout.read(), stderr.read()
        msg = res if res else err
    except Exception as e:
        ret, msg = False, str(e)
    finally:
        transport.close()
        ssh.close()  # 关闭连接
    return ret, msg, err

def ssh_connect_status(host, port=22, username="root", password="root"):
    """
    :param cmd:
    :param host:
    :param port:
    :param username:
    :param password:
    :return:
    """
    cmd = 'echo 123'
    import paramiko
    ret, msg, err = True, "", ""
    ssh = paramiko.SSHClient()  # 创建SSH对象
    status = False
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
        ssh.connect(hostname=host, port=port, username=username, password=password)  # 连接服务器
        stdin, stdout, stderr = ssh.exec_command(cmd)  # 执行命令并获取命令结果
        # stdin为输入的命令
        # stdout为命令返回的结果
        # stderr为命令错误时返回的结果
        res, err = stdout.read(), stderr.read()
        msg = res if res else err
        if msg and '123' in msg.decode():
            status = True
    except Exception as e:
        ret, msg = False, str(e)
    finally:
        ssh.close()  # 关闭连接

    return status


@wait(timeout=120, interval=2)
def ssh_status_until_connect(ip, port, username, password):
    """ 连接状态 ip"""
    return ssh_connect_status(ip, port, username, password)


@wait(timeout=60*5, interval=10)
def ssh_status_until_disconnect(ip, port, username, password):
    """ 连接状态 ip"""
    return not ssh_connect_status(ip, port, username, password)


def kill_pids(pid_name, host, port=22, username="root", password="root", env_cmd=None):
    """
    :param env_cmd:
    :param pid_name:
    :param host:
    :param port:
    :param username:
    :param password:
    :return:
    """
    ps_cmd = "ps -ef|grep %s |grep -v grep | awk '{print $2}'" % pid_name
    kill_cmd = "kill %s"
    if env_cmd:
        ps_cmd = "%s;%s" % (env_cmd, ps_cmd)
        kill_cmd = "%s;%s" % (env_cmd, kill_cmd)

    ret, msg = ssh_cmd(ps_cmd, host, port, username, password)
    if ret:
        pid_list = msg.split("\n")
        for pid in pid_list:
            if pid:
                ret, msg = ssh_cmd(kill_cmd % pid, host, port, username, password)
                print(ret, msg)
        return True, ""
    else:
        return ret, msg

def ping_ip(ip):
    """
    ip能ping通，返回True
    @ip ip地址
    """
    cmd = "ping -c 3 %s | grep -e '3 received' -e '3 packets received' | wc -l" % ip
    ret, output, err = system.ci_system(cmd, output=True)
    if output == "1\n":
        return True
    else:
        return False


def not_ping_ip(ip):
    """
    ip不能ping通，返回True
    @ip ip地址
    """
    cmd = "ping -c 3 %s | grep -e '3 received' -e '3 packets received' | wc -l" % ip
    ret, output, err = system.ci_system(cmd, output=True)
    if output != "1\n":
        return True
    else:
        return False


def kill_proc_by_pid(pid):
    """
    @note: kill proccess by pid
    """
    if type(pid) != int:
        pid = int(pid.strip())
    os.kill(pid, signal.SIGKILL)


def kill_proc_by_pid_file(pid_file):
    """
    @note: kill proccess by pid
    """
    if not os.path.isfile(pid_file):
        return False

    pid = None
    with open(pid_file, 'r') as f:
        pid = f.readline().strip()

    cmd = "ps -ef | grep %s | grep local-agent | grep -v grep" % pid
    ret = system.ci_system(cmd)
    if ret != 0:
        return False

    os.kill(int(pid), signal.SIGKILL)


def kill_all_proc_by_port(port):
    """
    @note: kill all proccess by port
    """
    cmd = "lsof -i:%s -t" % port
    ret, pids_str, err = system.ci_system(cmd, output=True)

    if pids_str == "":
        return True

    pids = pids_str.split('\n')
    for pid in pids:
        if pid == "":
            continue

        kill_proc_by_pid(pid)
    return True


def kill_all_proc_by_name(name):
    """
    @note: kill all proccess by port
    """
    cmd = "ps -ef | grep %s | grep -v grep | awk -F ' ' '{print $2}' | xargs kill -9" % name
    ret, pids_str, err = system.ci_system(cmd, output=True)


def telnet_ip_port(ip, port):
    """
    @note: telnet ip port成功，返回True
    @param:
        ip: ip地址
        port: port端口
    """
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect(('%s' % ip, int(port)))
        sk.close()
        return True
    except Exception:
        return False


def get_local_ip(ifname="eth0"):
    """
    获取本地ip地址
    @ifname net_if(eth0, eth1)
    """
    try:
        import fcntl
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
        ret = socket.inet_ntoa(inet[20:24])
    except IOError as IOerror:
        return None
    return ret

def checkip(ip):
    """
    @note: checking ip valid
    @param
        ip: machine ip
    @return
        True or False
    """
    ip_list = ip.split(".")
    if len(ip_list) != 4:
        return False
    for data in ip_list:
        if int(data) < 0 or int(data) > 256:
            return False
    return True


def find_str_in_file(file_path, match_re):
    """
    @note: find str in file
    """
    lines = []
    with open(file_path) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if re.search(match_re, lines[i]) is not None:
                return True
    return False

def modify_file(file_path, match_re, replace_str):
    """
    @note: modify content of file
    """
    lines = []
    with open(file_path) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = re.sub(match_re, replace_str, lines[i])

    with open(file_path, "w") as f:
        for line in lines:
            print >> f, line.replace('\n', '')


def modify_mutil_line_in_file(file_path, match_re_list, replace_str_list):
    """
    @note: modify mutilple lines of file
    @param:
        match_re_list: the length must equal replace
        replace_str_list: the length must equal match
    """
    len_match = len(match_re_list)
    len_replace = len(replace_str_list)
    if len_match != len_replace:
        return None

    lines = []
    with open(file_path) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if re.match(match_re_list[-1], lines[i]) and i >= (len_match - 1):
                if match_mutil_line(match_re_list, lines[i - len_match + 1:len_match]):
                    lines[i - len_match + 1:len_match] = modify_mutil_line(match_re_list, \
                                                                           replace_str_list, lines[
                                                                                             i - len_match + 1:len_match])

    with open(file_path, "w") as f:
        for line in lines:
            print >> f, line.replace('\n', '')


def match_mutil_line(match_re_list, lines):
    """
    @note: match mutilple lines
    @param:
        match_re_list: the length must equal lines
        lines: the length must equal match
    """
    for i in range(len(lines)):
        if re.match(match_re_list[i], lines[i]) is None:
            return False
    return True


def modify_mutil_line(match_re_list, replace_str_list, lines):
    """
    @note: match mutilple lines
    @param:
        match_re_list: the length must equal lines
        replace_str_list: the length must equal lines
        lines: the length must equal match
    """
    for i in range(len(lines)):
        lines[i] = re.sub(match_re_list[i], replace_str_list[i], lines[i])
    return lines


def insert_before_line(file_path, match_re, new_line):
    """
    @note: insert new line before one line
    """
    new_lines = []

    lines = []
    with open(file_path) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if re.search(match_re, lines[i]) is not None:
                new_lines.append(new_line)
            new_lines.append(lines[i])

    with open(file_path, "w") as f:
        for line in new_lines:
            print >> f, line.replace('\n', '')


def insert_after_line(file_path, match_re, new_line):
    """
    @note: insert new line after one line
    """
    new_lines = []

    lines = []
    with open(file_path) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            new_lines.append(lines[i])
            if re.search(match_re, lines[i]) is not None:
                new_lines.append(new_line)

    with open(file_path, "w") as f:
        for line in new_lines:
            print >> f, line.replace('\n', '')


def gen_log_name(raw_log_name):
    """
    @note: gen full log name
    """
    return "%s_%s.log" % (raw_log_name, get_cur_time_str1())


def get_cur_time_str1():
    """
    @note: get cur time , like "2017-06-21-17-15-13"
    """
    return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

def get_file_md5(file_path):
    """
    @note 返回文件的md5
    :param file_path:
    :return:


    ret = {
        "status": 0, 0成功  1失败
        "md5": "",
        "error_message": ""
    }
    """
    ret = {
        "status": 0,
        "md5": "",
        "error_message": ""
    }
    try:
        with open(file_path, "r") as f:
            md5 = hashlib.md5(f.read()).hexdigest()
        ret.update({"md5": md5, })
    except Exception as e:
        ret.update({"status": 1,
                    "error_message": str(e)})
    return ret


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


def get_file_size(file_path, change=True):
    """ 获取文件大小，单位：M
    :param change:
    :param file_path:
    :return:
    """
    # file_path = unicode(file_path, 'utf8')
    file_size = os.path.getsize(file_path)
    if change:
        file_size = file_size / float(1024 * 1024)
    return round(file_size, 2)


def init_dir(target_dir, delete=True):
    """ 删除目录并创建一个新的目录
    :param target_dir:
    :return:
    """
    if os.path.isdir(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir)


def alter_line(file_path, key_word, new_line):
    """
    替换文件中的字符串
    :param file_path:文件名
    :param key_word:就字符串
    :param new_line:新字符串
    :return:
    """
    file_data = ""
    with open(file_path, "r") as f:
        for line in f:
            if key_word in line:
                line = new_line + "\n"
            file_data += line
    with open(file_path, "w") as f:
        f.write(file_data)



if __name__ == '__main__':
    # cmd = "curl http://127.0.0.1:8889/api/1.0/tasks/all_status"
    # ret, msg, err = ssh_cmd(cmd, "10.4.10.60", username='root', password='T2mksense1!')
    # if ret:
    #     t = json.loads(msg)
    #     t = json.dumps(t, sort_keys=True, indent=2)
    #     print(t)

    scp_dir('/home/SENSETIME/wangan/test.demo', '/home/sensetime/test.demo', '10.4.10.29',
            username='root', password='T2mksense1')