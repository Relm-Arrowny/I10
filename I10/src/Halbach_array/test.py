'''
Created on 27 Apr 2017

@author: wvx67826
'''
from scipy import arange
import numpy as np
from Halbach_array.Halbach import Halbach
import time
test = Halbach("BL10J-MO-USER-01:", "BL10J-EA-USER-01:SER1.")

f = open('C:/Users/wvx67826/Desktop/Halbach/text.data', 'w+')
#test.set_field(90, 29.21)
for i in arange (0, 365, 15):
        test.set_field(i, 114.6)
        #test.set_motors(2, i)
        #test.set_motors(4, i)
        test.read_field()

        f.write("%f \t" %i + "%f \n" %test.xField)
f.close()
"""
for i in arange (0, 360,5):
    #    test.set_field(12.35,i)
    test.set_field(15.75, i)
    test.read_field()
    print i, ",", test.xField    
       
#   test.set_motors(i, i)
#        test.read_field()

"""
"""

motor = []
motor.append([])
for i in arange (0, 365, 15):
    motor[0].append(i)

for j in range (1,5):
    test.set_field(1.6, 29.21)
    motor.append([])
    for i in motor[0]:
        test.set_motors(j, i)
        test.read_field()
        motor[j].append(test.xField)    
        
f = open('C:/Users/wvx67826/Desktop/Halbach/text.data', 'w+')

f.writelines("Angle \t motor 1 \t motor 2 \t motor 3 \t motor 4 \n")
for i in range (len(motor[0])):
    f.write("%f \t" %motor[0][i] + "%f \t" %motor[1][i]+"%f \t" %motor[2][i] + "%f \t" %motor[3][i]+ "%f \t" %motor[4][i] + "\n")
f.close()
"""



"""
motor = []
motor.append([])
motor.append([])
for i in arange (0, 365, 5):
    motor[0].append(i)
    test.set_motors(1, i)
    test.read_field()
    motor[1].append(test.xField) 
        
f = open('C:/Users/wvx67826/Desktop/Halbach/text.data', 'w+')

f.writelines("Angle \t motor 1 \n")
for i in range (len(motor[0])):
    f.write("%f \t" %motor[0][i] + "%f \t" %motor[1][i] + "\n")
f.close()
"""
