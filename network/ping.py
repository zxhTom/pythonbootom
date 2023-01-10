# -*- coding: utf-8 -*-

import os
import socket
import sys
def pingtelnet(url):
    domain=None
    port=None
    if url==None:
        domain = sys.argv[1]  # domain为IP地址或域名都可以
        if len(sys.argv)>2:
            port=int(sys.argv[2])
    else:
        ipport=url.split(':')
        domain=ipport[0]
        if len(ipport)>1:
            try:
                port=int(ipport[1])
            except Exception:
                port=None
    flag = os.system('ping -c 1 -w 1 %s' % domain)  # 实现pingIP地址的功能，-c1指发送报文一次，-w1指等待1秒；flag为0则为成功，其他均为失败
    if flag:
        print("error")
        return False
    else:
        # check remote port
        if(port!=None):
            sk=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.settimeout(2)
            try:
                sk.connect((domain, port))
                print('port ok')
            except Exception as e:
                print(e)
                print('port not connect')
                return False
        print("success")
        return True
