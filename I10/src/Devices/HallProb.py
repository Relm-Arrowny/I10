'''
Created on 5 Dec 2017

@author: wvx67826
'''

'''
Created on 20 Apr 2017

@author: wvx67826
'''
from RS232.RS232 import RS232
import time
class HallProb(object):
 
    def __init__(self, epicsID, epicsIDFieldReader):
        self.magControl= RS232(epicsID) #set up for driving the motors
        self.hallProb = RS232(epicsIDFieldReader) #setup for reading hallprob
        self.xField = 0
        self.busy = False
        self.setup_prob() #setup the terminator and timeout wait
        self.read_field()
    def read_field(self):
        self.clearMemeory()
        xField = self.hallProb.get("TINP")
        while len(xField)<6:
            self.clearMemeory()
            xField = self.hallProb.get("TINP")
                        
        self.xField = float(xField[:6])

    def clearMemeory(self):
        self.hallProb.set_tran_state("flush")
        self.hallProb.set_tran_state("read")
        time.sleep(2.0)
        
        
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
