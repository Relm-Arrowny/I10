'''
Created on 16 May 2017

@author: wvx67826
'''

from RS232.RS232 import RS232
import time
class EggCups(object):
 
    def __init__(self, epicsID):
        self.magl= RS232(epicsID) #set up for driving the motors
        self.magMotor = [0.0,0.0,0.0]
        self.update_position()
        self.xField = 0
        self.busy = False
        self.setup_prob() #setup the terminator and timeout wait
    
    def set_motors(self, motor, motAngle):
        self.magControl.set("AXIS" + str(motor) +".VAL", motAngle)
        
        
    def update_position(self):
        for i in range(1,5):
            self.magMotor[i-1] = float(self.magControl.get("AXIS%s.RBV" %i))
