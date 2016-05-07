'''
Created on 7 May 2016

@author: Relm

lockin amp playground, generate wave, pass it through simple lockin, make use of hilbert transformation to get 90 degree phase shift.

Vout  = abs ((x**2+y**2)**0.5)*2.0
output form this toy lockin gives amplitude = Vsig*Vref

'''

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


class SignalProcessing:
    def __init__(self):
        pass
    def wave(self, nDataPoint = 10000, time = 10.0, amp = 10.5, freq = 9.0, dc = 0,phase=0):
        k = np.array(np.arange(nDataPoint))
        t = time/nDataPoint*k
        y = dc + amp*np.sin(2*np.pi*freq*t+phase*np.pi/360.)
        return t , y
    
    def hilbertTran(self,wav):
        wavefft = np.fft.fft(wav)*2.0
        wavefft[0:len(wav)/2] = 0.0
        return np.fft.ifft(wavefft)
    def lockin(self,wave,waveRef):
        x = wave*waveRef
        y = wave*np.imag(self.hilbertTran(waveRef))
        R = (np.average(x)**2+np.average(y)**2)**0.5*2.0
        phase = np.arctan(np.average(y)/np.average(x))*180.0/np.pi
        '''
        plt.subplot(211)
        plt.plot(x)
        plt.subplot(212)
        plt.plot(y)
        plt.show()
        '''
        return R, phase
    def halfFrequency(self,wav):
        y = []
        n = len(wav)
        for i in range(0,n/2):
            y.append(wav[i])
            y.append((wav[i]+wav[i+1])/2.0)
        return y
    
    def doubleFrequency(self,wav):
        y = []
        n = len(wav)
        for i in range(0,n,2):
            y.append(wav[i])
        for k in range(n-1,0,-2):
            y.append(-wav[k])
        return y    
    
wav = np.add(SignalProcessing().wave(), SignalProcessing().wave(10000, 10.0,  5.5,  18.0, 0, 0))
plt.plot(wav[1])
plt.show()
wavRef = SignalProcessing().wave(10000, 10.0,  1.0,  9.0, 0, 0)   
for i in range (0,1000):
    twave =   SignalProcessing().wave(10000, 10.0, np.random.random()*1.0+1.0, np.random.random()*500.0+11.0,
                                        np.random.random()*10.0, np.random.random()*360)
    wav = np.add(twave , wav)
R=[]
f = []
Re = []
Re.append(SignalProcessing().lockin(wav[1], wavRef[1]))
Re.append(SignalProcessing().lockin(wav[1], SignalProcessing().doubleFrequency((wavRef[1]))))

plt.subplot(411)
#plt.plot(wav[0],wav[1])
plt.plot(wav[1])
plt.subplot(412)
plt.plot(wav[0], wavRef[1])

for i in np.arange (1,500,0.1):
    f.append(i)
    R.append( SignalProcessing().lockin(wav[1],SignalProcessing().wave(10000, 10.0,  1,  i, 0, 0) [1])[0])
print Re
plt.subplot(413)
plt.plot(np.fft.rfftfreq(10000, 10.0/10000),np.abs(np.fft.rfft(wav[1]))/10000.0)
plt.yscale('log')
plt.subplot(414)
plt.plot(f,R)
plt.show()
#plt.plot(np.imag(coeffs))
#plt.plot(np.real(coeffs))
    