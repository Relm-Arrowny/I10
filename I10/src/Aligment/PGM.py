'''
Created on 6 Dec 2016

@author: wvx67826

Fit Cff against change in wavelength to work out d theta and d beta
Nuclear Instruments and Methods in Physics Research A 467–468 (2001) 482–484

'''
import numpy as dnp
from epics import caget
import matplotlib.pyplot as plt
import scipy
from scipy import optimize
import csv

#from Test import RS232

class PGM(object):
    '''
    classdocs
    '''   
    def __init__(self):
       pass 
        
    def cal_alpha(self, cff, lamda, lineDensity, diffOrder = 1):
        return dnp.arcsin((lamda*lineDensity*diffOrder)/(dnp.power(cff,2.0)-1.0)*
                (dnp.sqrt(dnp.square(cff)+dnp.square(dnp.square(cff)-1.0)/
                             dnp.square(lamda*lineDensity*diffOrder))-1))

    def cal_beta(self, cff, lamda, lineDensity, diffOrder = 1):
        return -dnp.arccos(cff*dnp.cos(self.cal_alpha(cff, lamda, lineDensity, diffOrder)))
    
    def cal_dlamda(self, cff, lamda, lineDensity, dTheta,dbeta, diffOrder = 1):
        beta = self.cal_beta(cff, lamda, lineDensity, diffOrder)
        alpha = self.cal_alpha(cff, lamda, lineDensity, diffOrder)
        tempTheta = (-beta + alpha) /2.0
        return 2.0*dnp.cos(tempTheta + dTheta)*dnp.sin(tempTheta+dTheta+beta+dbeta)/(lineDensity*diffOrder)

def func(params, cff, energy, err):
    dTheta = params[0]
    dbeta = params [1]
    chi2 = 0.0
    pgm = PGM()
    for n in range(len(cff)):
        x = cff[n]
        y = pgm.cal_dlamda(x, lamda, nLine, dTheta, dbeta)
        chi2 = chi2 +(energy[n]-y)*(energy[n]-y)/(err[n]*err[n])
    return chi2



nLine = 300./1e7
lamda = 12.4/0.50096    

f = open("C:/Users/wvx67826/Desktop/I10/PGM/test.txt",'w')
for cff in scipy.arange(1.1,13.5,0.15):
    test = PGM()
    dlamda = test.cal_dlamda(cff, lamda, nLine, 1.23e-3, 0.224e-5) 
    temp =str(cff) + ","+str(dlamda)
    f.write(temp)
    f.write("\n")
f.close()


with  open("C:/Users/wvx67826/Desktop/I10/PGM/test.txt",'r') as f:
    reader = csv.reader(f)
    data = list(reader)
x = []
y = []
y_err = []
for i in range (len(data)):
    x.append(float(data[i][0]))
    y.append(float(data[i][1]))
    y_err.append(float(data[i][1])*0.01)
f.close()
plt.plot(x,y,'ro')

x0 = [1.0e-2,1.0e-1]
result = optimize.fmin(func,x0,args = (x,y,y_err),full_output= 0)

y1 = []
for i in range (len(x)):
    y1.append(test.cal_dlamda(x[i], lamda, nLine, result[0], result[1]))
plt.plot(x,y1)
plt.show()    

print result



