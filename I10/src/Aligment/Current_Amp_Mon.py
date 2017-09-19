'''
Created on 13 Sep 2017

@author: wvx67826
'''

from RS232.RS232 import RS232
import time
class Current_Amp_Mon(object):
 
    def __init__(self, epicsCurrentAmp):
        #set up for driving the motors
        self.currentAmp = RS232(epicsCurrentAmp)
        self.bCurrent = [0.0, 0.0, 0.0, 0.0] # x ring, x hall, y minus, y plus
        self.update_position()
        self.busy = False    
    def set_motors(self, motor, motAngle):
        self.magControl.set("AXIS" + str(motor) +".VAL", motAngle)
        
        
    def update_position(self):
        self.bCurrent[0] = self.currentAmp.get("SIG1")
        self.bCurrent[1] = self.currentAmp.get("SIG2")
        self.bCurrent[2] = self.currentAmp.get("SIG3")
        self.bCurrent[3] = self.currentAmp.get("SIG4")

    def log(self):
        pass
    
test = Current_Amp_Mon("BL10I-DI-IAMP-01:")
test1 = Current_Amp_Mon("BL10I-DI-IAMP-01:")
print test.bCurrent, ",", test1.bCurrent, "\n"
f = open('13_9_test.data', 'a+')
while True:
        test.update_position()
        f.write( time.strftime("%a, %d %b %Y %H:%M:%S\t" , time.gmtime())  + "%f \t" %test.bCurrent[0] + "%f \t" %test.bCurrent[1] +
                "%f \t" %test.bCurrent[2] +"%f \t" %test.bCurrent[3] +"%f \t" %test1.bCurrent[0] + "%f \t" %test1.bCurrent[1] +
                "%f \t" %test1.bCurrent[2] +"%f \t" %test1.bCurrent[3] )
        print ( time.strftime("%a, %d %b %Y %H:%M:%S\t" , time.gmtime())  + "%f \t" %test.bCurrent[0] + "%f \t" %test.bCurrent[1] +
                "%f \t" %test.bCurrent[2] +"%f \t" %test.bCurrent[3] +"%f \t" %test1.bCurrent[0] + "%f \t" %test1.bCurrent[1] +
                "%f \t" %test1.bCurrent[2] +"%f \t" %test1.bCurrent[3] )
        time.sleep(20)
f.close()

