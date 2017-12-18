#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import re
from std_msgs.msg import String
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def callback(data):
    #待匹配目标列表
    target = ["杯子","铅笔","鼠标","餐巾纸","书"]
    #准备语音输出状态
    pub = rospy.Publisher('speak_string', String, queue_size=1)
    #rospy.init_node('talker', anonymous=True)
    response = ""
    # 将正则表达式编译成Pattern对象
    for item in target:
        pattern = re.compile(ur''+item+'')
        match = pattern.search(data.data.decode('utf8'))# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        if match:
            response = "好的，我这就给您去拿" +  match.group() 
            break
    if response == "":
        response = "抱歉，我没有听清楚您需要什么。"
    rospy.loginfo(response) 
    pub.publish(response)   
    
def listener():

    rospy.init_node('translator', anonymous=True)

    rospy.Subscriber("heard_string", String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()