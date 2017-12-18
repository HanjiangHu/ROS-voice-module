# ROS_voice
this package is python package for ROS speech, which use online baidu speech to do TTS and speech recognition.

this code is run well in ubuntu 14.04, thinkpad T44s.

you can visit the baidu speech home page at here: http://yuyin.baidu.com/

the key and id is show below, feel free to change it in simple_speaker.launch and simple_voice.launch.

App ID: 8168466
API Key: pmUzrWcsA3Ce7RB5rSqsvQt2
Secret Key: d39ec848d016a8474c7c25e308b310c3
subscribe topic

speak_string #type string
How to run:

Speech Recognition:　roslaunch simple_voice simple_voice.launch
Text To Speech: roslaunch simple_voice simple_speaker.launch
wiki

http://wiki.ros.org/baidu_speech
#关于毕设 现在可以实现对特定关键词（"杯子","铅笔","鼠标","餐巾纸","书"）进行识别以及简单的辅助人机对话，测试前电脑最好连接好网络，有时有bug，测试方法：
终端1：roscore 
终端2：roslaunch simple_voice simple_voice.launch 
终端3：rosrun simple_voice recognition.py 
终端4：roslaunch simple_voice simple_speaker.launch 以上基本就可以运行了，如果电脑说不出话可以用下面指令让他说：大家好！ 之后再在终端2按enter重新说需要什么 
终端5：rostopic pub /speak_string std_msgs/String -- '大家好！'
