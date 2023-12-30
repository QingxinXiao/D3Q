# coding=utf-8
import re

# 这里以读取video_reqtest.txt中后一个括号内的数字0.079，存到train.txt为例，video_reqtest.txt文件中的内容如下
# video 1/1 (1/902) /content/drive/MyDrive/yolov5-5.0/mydata/barbecue.mp4: 384x640 1 fire, Done. (0.079s)
# video 1/1 (2/902) /content/drive/MyDrive/yolov5-5.0/mydata/barbecue.mp4: 384x640 1 fire, Done. (0.015s)
# video 1/1 (3/902) /content/drive/MyDrive/yolov5-5.0/mydata/barbecue.mp4: 384x640 1 fire, Done. (0.015s)
# 读取文件的每一行
read_txt = open("log200.txt", "r")
# 定义一个空列表用于接收提取出来的内容
temp = []

for line in read_txt:
    a = re.findall(r'[[](.*?)[,]', line)  # 读出一行中（）内的值，用到是python的正则表达式，不懂。。。如  abbc(0.1s)   ,读出为 0.1s

    # b = re.findall(r'[[](.*?)', a[1])  # 按上面的方法把s去掉

    temp.append((a[0]))  # 添加到临时列表中

# 写入到文件
with open("new.txt", "w") as file:
    j = 1
    for i in temp:
        file.write('"' + str(j) + '"' + ':' + ' ')
        file.write(i + ', ')
        j = j+1
    file.close()

