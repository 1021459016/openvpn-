#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/4/20
import sys
import pyperclip   
import os

print('！！！----------使用前请复制口令----------！！！')

def file_pass():    
    f_name = "C:\\Program Files\\OpenVPN\\config\\pass.txt"    #密码信息文件存放路径
    if os.path.exists(f_name):
        f = open(f_name, mode='r+')
    else:
        f = open(f_name, mode='w+')
    if os.path.getsize(f_name) == 0:
        username = input('请输入账号：')
        password = input('请输入PIN码：')
        new_password = password + dtm()
        f.write(username+'\n')
        f.write(new_password)
        f.close()
    else:
        old_str = f.read()[-6:]
        new_str = dtm()
        f.close()
        alter(f_name,old_str,new_str)

def dtm():        #获取动态码信息
    import re
    dtm = pyperclip.paste()
    pattern = re.compile(r'\d+')
    re = pattern.findall(dtm)
    new_dtm = str(re[0])
    return new_dtm


def alter(file,old_str,new_str):                                   #负责更新文件密钥
    f_new_name = '%s.new' % file
    with open(file, "r") as f1,open(f_new_name, "w") as f2:
        for line in f1:
            if old_str in line:
                new_line = line.replace(old_str, new_str)
            else:
                new_line = line
            f2.write(new_line)
    os.remove(file)
    os.replace(f_new_name,file)


def openvpn():
    cmd = 'openvpn-gui.exe --connect client-218.205.195.94.ovpn'   #这里放要连接的VPN文件信息，本质是通过cmd窗口调用此命令连接openvpn
    os.system(cmd)
    
if __name__ == '__main__':
    file_pass()
    openvpn()
