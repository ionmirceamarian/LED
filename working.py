import paramiko
from datetime import datetime
import json
import mss
import numpy as np


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("XXX.XXX.XXX.XXX", username='username', password="password")
# closing any existing old python black* processes
ssh.exec_command("sudo ps -ef |grep 'python black' |grep -v 'grep' |awk '{print$2}' | xargs  -I {} kill -9 {}")
times = 0
while times < 10 :
   
    a = {}
    now = datetime.now()
    # mss.mss is faster than ImageGrab , did not try opencv
    image = mss.mss().grab(mss.mss().monitors[2])    
    img_array = np.array(image)
        
    a = {}
    L = img_array.shape[1]
    H = img_array.shape[0]
    # setting an effect area (158 px from bottom to the center of the screen)
    step = 158
    count = 0
    # adding offset (4 pixels will be skipped as they are slack in the back of the tv)
    offset = 4
    for i in range(0, offset):
        a[i+1] = '0,0,0'
    count = offset
    midle = int(L/2)
    # we are goiong to create an average for each 158x158 array from the middle bottom clockwise 
    # i bet there is a better way to do this but this is what worked at the time
    # going from bottom middle to the left
    for i in range(L-1, 0, - step):
        if i  > step:
            px = img_array[int(H-step):int(H),int(i-step):int(i)]
            a[count+1] = str(int(np.mean(np.mean(px,axis=0),axis=0)[2]))+","+str(int(np.mean(np.mean(px,axis=0),axis=0)[0]))+","+str(int(np.mean(np.mean(px,axis=0),axis=0)[1]))
            count += 1 
    # going from bottom left to upper left
    for i in range(H,0, - step):
        if i > step:
            px = img_array[int(i-step):int(i),0:step]
            a[count+1] = str(int(np.mean(np.mean(px,axis=0),axis=0)[2]))+","+str(int(np.mean(np.mean(px,axis=0),axis=0)[0]))+","+str(int(np.mean(np.mean(px,axis=0),axis=0)[1]))
            count += 1 
    # going from upper left to upper right
    for i in range(0 ,L, step):
        if i < L - step:
            px = img_array[0:step,int(i):int(i+step)]
            a[count+1] = str(int(np.mean(np.mean(px,axis=0),axis=0)[2]))+","+str(int(np.mean(np.mean(px,axis=0),axis=0)[0]))+","+str(int(np.mean(np.mean(px,axis=0),axis=0)[1]))
            count += 1
    # going from upper right to bottom right
    for i in range(0,H, step):
        if i < H - step:
            px = img_array[int(i):int(i+step),int(L-step):int(L)]
            a[count+1] = str(int(np.mean(np.mean(px,axis=0),axis=0)[2]))+","+str(int(np.mean(np.mean(px,axis=0),axis=0)[0]))+","+str(int(np.mean(np.mean(px,axis=0),axis=0)[1]))
            count += 1
    # going back to from bottom right to bottom left
    for i in range(L, 0, - step):
        if i  > step:
            px = img_array[int(H-step):int(H),int(i-step):int(i)]
            a[count+1] = str(int(np.mean(np.mean(px,axis=0),axis=0)[2]))+","+str(int(np.mean(np.mean(px,axis=0),axis=0)[0]))+","+str(int(np.mean(np.mean(px,axis=0),axis=0)[1]))
            count += 1 

    #  print(a)
    # sending the RGB to our pi machine
    ssh.exec_command("sudo python black_1.py  \""+json.dumps(a).replace("\"","'")+"\"")

# exiting
ssh.exec_command("sudo python black_1.py  \"{'1':'0,0,0','2':'0,0,0'}\"")
ssh.close()