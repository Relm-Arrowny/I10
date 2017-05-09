'''
Created on 20 Apr 2017

@author: wvx67826
'''
from RS232.RS232 import RS232
import time
class Halbach(object):
 
    def __init__(self, epicsID, epicsIDFieldReader):
        self.magControl= RS232(epicsID) #set up for driving the motors
        self.hallProb = RS232(epicsIDFieldReader) #setup for reading hallprob
        self.magMotor = [0.0,0.0,0.0,0.0]
        self.update_position()
        self.xField = 0
        self.busy = False
        self.setup_prob() #setup the terminator and timeout wait
    
    def set_motors(self, motor, motAngle):
        self.magControl.set("AXIS" + str(motor) +".VAL", motAngle)
        
        
    def update_position(self):
        for i in range(1,5):
            self.magMotor[i-1] = float(self.magControl.get("AXIS%s.RBV" %i))

    def read_field(self):
        self.motion_wait()
        self.hallProb.set_tran_state("flush")
        self.hallProb.set_tran_state("read")
        time.sleep(2.0)
        xField = self.hallProb.get("TINP")

        self.xField = xField[:6]
        #print self.xField

    def setup_prob(self):
        """
                Set the port to make sure the right PV is being controlled
        and set the terminator'''
        '''
        """
        self.hallProb.set("OEOS", '\n')
        self.hallProb.set("IEOS", '\r\n')
        self.hallProb.set("TMOT", 2.0)
        self.hallProb.set("SCAN", 0)
        
    def set_field(self, field, angle = 0.0):
        self.set_motors(1, field+angle)
        self.set_motors(2, -1.0*field+angle)
        self.set_motors(3, field+angle)
        self.set_motors(4, -1.0*field+angle)
        self.motion_wait()
        

    def motion_wait(self):
        self.busy = True
        while self.busy:
            self.update_position()
            oldPosition = list(self.magMotor)
            time.sleep(0.2)
            self.update_position()
            if (oldPosition == self.magMotor):
                self.busy = False
    def find_field(self, field, acc):
        pass