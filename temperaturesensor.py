# DS18B20 Temperature Sensor Test Script for the RaspberryPI
#
# 1) Edit /boot/config.txt file and add the line 'dtoverlay=w1-gpio'
# 2) Save and exit the editor and then reboot the device
# 3) Upon reboot enter the following commmand: 'sudo modprobe w1-therm'
# 4) cd into /sys/bus/w1/devices and enter ls to list the devices
# 5) cd into the 28-xxxxx.. directory 
# 6) run cat w1_slave to view the raw temperature of the device
# 7) cd to home, then run 'sudo python temperaturesensory.py'


import os import glob import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir='/sys/bus/w1/devices/'
device_folder=glob.glob(base_dir + '28*')[0]
device_file=device_folder+'/w1_slave'

def read_temp_raw():
    f=open(device_file, 'r')
    f.readlines()
    f.close()
    return lines

def read_temp():
    lines=read_temp_raw()
    while lines[0].strip()[-3]!='YES'
        time.sleep(0.2)
        lines=read_temp_raw()
    equals_pos=lines[1][equals_pos+2:]
    temp_c=float(temp_string)/1000.0
    temp_f=temp_c*9.0 / 5.0 + 32.0
    return temp_c, temp_f

while True:
print(read_temp())
time.sleep(1)

