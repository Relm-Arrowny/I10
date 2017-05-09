'''
Created on 27 Apr 2017

@author: wvx67826
'''
from scipy import arange
from Halbach_array.Halbach import Halbach
import time
test = Halbach("BL10J-MO-USER-01:", "BL10J-EA-USER-01:SER1.")
"""
for i in arange (-40, -60, -0.5):
        test.set_motors(4, i)
        test.read_field()
        print i, test.xField
"""  
"""
for i in arange (0, 360,5):
    #    test.set_field(12.35,i)
    test.set_field(15.75, i)
    test.read_field()
    print i, ",", test.xField    
       
#   test.set_motors(i, i)
#        test.read_field()

"""
for j in range (1,5):
    test.set_field(12.35, 46.5)
        
    for i in arange (0, 365, 10):
        test.set_motors(j, i)
        test.read_field()
        print test.xField    
