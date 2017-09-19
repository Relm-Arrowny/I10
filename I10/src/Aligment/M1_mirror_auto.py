'''
Created on 11 Sep 2017

@author: wvx67826
'''

from RS232.RS232 import RS232
import time
class M1_mirror_auto(object):
 
    def __init__(self, epicsIDM1,epicsIDBlade, epicsCurrentAmp):
        self.m1= RS232(epicsIDM1) #set up for driving the motors
        self.blade = RS232(epicsIDBlade)
        self.currentAmp = RS232(epicsCurrentAmp)
        self.m1Fpitch = 0.0
        self.bladePosition = [0.0, 0.0] #xsize and y size
        self.bCurrent = [0.0, 0.0, 0.0, 0.0] # x ring, x hall, y minus, y plus
        self.update_position()
        self.busy = False    
    def set_motors(self, motor, motAngle):
        self.magControl.set("AXIS" + str(motor) +".VAL", motAngle)
        
        
    def update_position(self):
        self.m1Fpitch = self.m1.get("FPITCH:DMD:AO")
        self.bladePosition[0] = self.blade.get("XSIZE.RBV")
        self.bladePosition[1] = self.blade.get("YSIZE.RBV")
        self.bCurrent[0] = self.currentAmp.get("XRING:I")
        self.bCurrent[1] = self.currentAmp.get("XHALL:I")
        self.bCurrent[2] = self.currentAmp.get("YMINUS:I")
        self.bCurrent[3] = self.currentAmp.get("YPLUS:I")

    def log(self):
        pass
test = M1_mirror_auto("BL10I-OP-COL-01:", "BL10I-AL-SLITS-02:","BL10I-AL-SLITS-02:")
print test.bCurrent, ",", test.bladePosition,",", test.m1Fpitch, "\n"
print( time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())  + "%f \t" %test.bCurrent[0] + "%f \t" %test.bCurrent[1] +
                "%f \t" %test.bCurrent[2] +"%f \t" %test.bCurrent[3] +
                "%f \t" %test.bladePosition[0] + "%f \t" %test.bladePosition[1] +
                "%f \n" %test.m1Fpitch)
f = open('S2.data', 'w+')
while True:
        test.update_position()
        f.write( time.strftime("%a, %d %b %Y %H:%M:%S\t" , time.gmtime())  + "%f \t" %test.bCurrent[0] + "%f \t" %test.bCurrent[1] +
                "%f \t" %test.bCurrent[2] +"%f \t" %test.bCurrent[3] +
                "%f \t" %test.bladePosition[0] + "%f \t" %test.bladePosition[1] +
                "%f \n" %test.m1Fpitch)
        time.sleep(20)
f.close()

