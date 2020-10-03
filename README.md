# ros voice module
This module is for simple Chinese speech extraction and recognition based on online [baidu speech](http://wiki.ros.org/baidu_speech)

### Environment
Ubuntu 16.04, ROS Kinetic

### Preparation
`sudo apt-get install python-pyaudio`

`sudo apt-get install python-requests`

`sudo apt-get install vlc`

###How to run
Recognize the specific Chinese keywords like ("杯子"(cup),"铅笔"(pencil),"鼠标"(mouse),"餐巾纸"(tissue),"书"(book)), and make sure the network is well connected.

Open four terminal and input the following four commands

`roscore`

`roslaunch simple_voice simple_voice.launch` 

`rosrun simple_voice recognition.py` 

`roslaunch simple_voice simple_speaker.launch`and say "请给我一个杯子" （Please give me a cup）

If it doesn't work, input the follow command in a new terminal to let it say "大家好！" (Hey guys!) and then speak to it again.

`rostopic pub /speak_string std_msgs/String -- '大家好！'`
