#!/usr/bin/env python    
#!coding=utf-8    
import os    
import time    
import sys    
import datetime    
from mymail import SendEmail    
global per_hour
per_hour = 2     
global base_time 
base_time = datetime.datetime(1970,1,1) 
whhmail = SendEmail()    
    
mysender = 'XXXXXXXXX@XX.com'    
while True:    
    timeis = datetime.datetime.now()    
        
    if base_time - datetime.datetime(1970,1,1) == datetime.timedelta(0) or (( timeis - base_time ).seconds)/3600 > per_hour:    
        try:    
            Pro_status = os.popen('netstat -antp | grep 996','r').readlines()    
            line_cnt = len(Pro_status)    
            if line_cnt > 2:    
                print "可以发送邮件了"    
                base_time = timeis    
                print "获取basetime " + base_time.strftime("%Y-%m-%d %H:%M:%S")   
                whhmail.send_email(mysender,"您的aws服务端口检测提醒","[" + base_time.strftime('%Y-%m-%d %H:%M:%S') + "]\n "+"".join(Pro_status))    
        except  Exception as e:    
            print('myerror', e)    
    else:
        print "没有执行检查睡眠5秒"
    time.sleep(5)    
