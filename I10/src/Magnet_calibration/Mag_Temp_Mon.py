'''
Created on 30 Oct 2017

@author: wvx67826
'''


'''
Created on 13 Sep 2017

@author: wvx67826
'''

from RS232.RS232 import RS232
import time
import logging
class Mag_Temp_Mon(object):
 
    def __init__(self, epicsTemp, epicMagCurrent, epicRasorPressure):
        self.magTemp = RS232(epicsTemp)
        self.currentAmp = RS232(epicMagCurrent)
        self.rasorP = RS232(epicRasorPressure)
        self.magT = 0.0 
        self.magCurrent = 0.0
        self.rasorPressure  = 0.0
        self.update_position()
    def set_mag_cur(self, current):
        self.currentAmp.set("AO2", (current*0.141))
        self.update_position()
        
        
    def update_position(self):
        self.magCurrent = float(self.currentAmp.get("AO2"))/0.141
        self.magT       = self.magTemp.get("KRDG0")
        self.rasorPressure = self.rasorP.get("P")
        
            
        
    def log(self):
        pass
    
test = Mag_Temp_Mon("ME01D-EA-TCTRL-01:","BL10I-EA-USER-01:","BL10I-VA-SPACE-14:")
"""
while True:
    test.update_position()
    print test.magT, ",", test.magCurrent, ",", test.rasorPressure
    time.sleep(5)"""
log = logging.getLogger("Electro magnet")
fh = logging.FileHandler('data/31_10_Emagnet_test.log')
log.addHandler(fh)
log.setLevel(logging.INFO)
f = open('data/31_10_Emagnet_test.data', 'a+')
global MEASUREMENTLOOP
MEASUREMENTLOOP = True
while MEASUREMENTLOOP:
        test.update_position()
        f.write( time.strftime("%a, %d %b %Y %H:%M:%S\t" , time.gmtime())  + "%f \t" %test.magT + "%f \t" %test.magCurrent +
                "%E \t" %test.rasorPressure +"\n" )
        log.info(( time.strftime("%a, %d %b %Y %H:%M:%S\t" , time.gmtime())  + "%f \t" %test.magT + "%f \t" %test.magCurrent +
                "%E \t" %test.rasorPressure ))
        
        print test.magT, ",", test.magCurrent, ",", test.rasorPressure
        if (test.magT > 60.0 or test.rasorPressure> 1E-6):
            test.set_mag_cur(0)
            MEASUREMENTLOOP = False
        time.sleep(10)
f.close()
