'''
Created on 16 May 2017

@author: wvx67826
'''
from scipy import arange
from Devices.HallProb import HallProb
from RS232.RS232 import RS232

f = open('cal4bars_slotted2.dat', 'w+')

hProbe = HallProb("BL10J-MO-USER-01:", "BL10I-EA-USER-01:SER4.")
hProbe.setup_prob()
mag1 = RS232("ME01D-EA-EMEC-01:")
sx = RS232("ME01D-MO-CRYO-01:")


for j in arange (9,15,1):
    sx.set("X.VAL", j)
    sx.motion_wait("X.RBV")
    
for i in arange (0, 20,0.25):
    #mag1.set("Y1.VAL", -i)
    mag1.set("Y2.VAL", i)
    mag1.motion_wait("Y2.RBV")
    hProbe.read_field()
    print i,hProbe.xField
    f.write("%f \t" %i + "%f \n" %hProbe.xField)
for i in arange (20, 0,-0.25):
    #mag1.set("Y1.VAL", -i)
    mag1.set("Y2.VAL", i)
    mag1.motion_wait("Y2.RBV")
    hProbe.read_field()
    print i,hProbe.xField
    f.write("%f \t" %i + "%f \n" %hProbe.xField)
    
f.close()
    
    