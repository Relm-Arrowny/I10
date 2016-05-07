'''
Created on 7 May 2016

@author: Relm


Simple waveform processing include functions:

waveGen ---> generate wave
hilberTran ----> hilber transformation
lockin ----> Lockin amplifier
half/doubleFrequency ----> half or double frequency of wave


'''
import numpy as np


class WaveProcessing:
    def __init__(self):
        pass
    def waveGen(self, nDataPoint = 10000, time = 10.0, amp = 10.5, freq = 9.0, dc = 0,phase=0):
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
