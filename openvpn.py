#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/4/20

import pyperclip
import re
import os


dtm = pyperclip.paste()
pattern = re.compile(r'\d+')
re = pattern.findall(dtm)
new_dtm = str(re[0])
username = '账号'
password = '密码'+new_dtm

def file_pass():
    f_name = "C:\\Program Files (x86)\\OpenVPN\\config\\pass.txt"
    f = open(f_name, mode='r+')
    f.write(username+'\n')
    f.write(password)
    f.close()

def openvpn():
    cmd = 'openvpn-gui.exe --connect client-211.101.48.117.ovpn'
    os.system(cmd)
    os.close()

file_pass()
openvpn()



