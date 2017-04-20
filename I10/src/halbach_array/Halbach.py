'''
Created on 20 Apr 2017

@author: wvx67826
'''
import numpy as dnp
from epics import caget
import matplotlib.pyplot as plt
import scipy
from scipy import optimize
import csv

class Halbach(object):
 
    def __init__(self, epicsID):
        self.epicsID = epicsID
        self.mag1 = caget(epicsID + "AXIS1.RBV")
        self.mag2 = caget(epicsID + "AXIS2.RBV")
        self.mag3 = caget(epicsID + "AXIS3.RBV")
        self.mag4 = caget(epicsID + "AXIS4.RBV")
        self.xField = 0
    def set_field(self, field, angle = 0.0):
        pass 
        

test = Halbach("BL10J-MO-USER-01:")
print (test.mag1)