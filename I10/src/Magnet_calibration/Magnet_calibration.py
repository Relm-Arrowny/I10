'''
Created on 16 May 2017

@author: wvx67826
'''
from scipy import arange
import numpy as np
from Halbach_array.Halbach import Halbach
from RS232.RS232 import RS232
import time

f = open('S:/Science/I10/Tools/I10_Python/I10_python/I10/src/Magnet_calibration/cal4bars_close_gap_X_Z.dat', 'w+')

hProbe = Halbach("BL10J-MO-USER-01:", "BL10I-EA-USER-01:SER5.")
hProbe.setup_prob()
mag1 = RS232("ME01D-EA-EMEC-01:")
sx = RS232("ME01D-MO-CRYO-01:")

def motion_wait():
        busy = True
        while busy:
            position = mag1.get("Y2.RBV")
            oldPosition = mag1.get("Y2.RBV")
            time.sleep(0.2)
            position = mag1.get("Y2.RBV")
            if (oldPosition == position):
                busy = False
def motion_wait1():
        busy = True
        while busy:
            position = sx.get("X.RBV")
            oldPosition = sx.get("X.RBV")
            time.sleep(0.5)
            position = sx.get("X.RBV")
            if (oldPosition == position):
                busy = False
                
for j in arange (9,15,1):
    sx.set("X.VAL", j)
    motion_wait1()
    for i in arange (20, 0,-0.25):
        #mag1.set("Y1.VAL", -i)
        mag1.set("Y2.VAL", i)
        motion_wait()
        hProbe.read_field()
        print i,hProbe.xField
        f.write("%f \t" %j +"%f \t" %i + "%f \n" %hProbe.xField)
f.close()
    
    