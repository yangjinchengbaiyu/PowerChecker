# _*_ coding:UTF-8 _*_
from time import sleep
from psutil import sensors_battery
from messageboxs import *


b = sensors_battery()[0]
e_t = (10, 20, 30, 40, 50, b)
index = sorted(e_t).index(b)

if index:
    low = False
    
else:
    low = True

e_t = (10, 20, 30, 40, 50)
e = index * 10

while True:
    battery = sensors_battery()[0]  # 获取电池电量

    if not low:

        if battery <= e:
            if e in (30, 40, 50):
                lower(battery)
            else:
                very_low(battery)

            try:
                e = e_t[e_t.index(e) - 1]
            except IndexError:
                low = True

    elif battery >= 10:
        low = False

    sleep(1)  # 等待1秒
