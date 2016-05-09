'''
Created on 7 May 2016

@author: Relm

Simple waveform processing include functions:

waveGen ---> generate wave
hilbertTran ----> hilbert transformation
lockin ----> Lockin amplifier
half/doubleFrequency ----> half or double frequency of wave
lowpassFilter -----> continuous lowpass filter 
fftLowpassFilter ----> fft lowpass filter fft input -> cut off high frequency -> ifft to recover the lowpass wave

'''
import numpy as np
import matplotlib.pyplot as plt

class WaveProcessing:
    def __init__(self):
        pass
    def waveGen(self, nDataPoint = 10000, time = 10.0, amp = 1.0, freq = 10.0, dc = 0,phase=0):
        '''Generate and return time and sin wave'''
        k = np.array(np.arange(nDataPoint))
        t = time/nDataPoint*k
        y = dc + amp*np.sin(2*np.pi*freq*t+phase*np.pi/360.)
        return t , y
    def hilbertTran(self,wav):
        '''Hilber transformation for any real wave'''
        wavefft = np.fft.fft(wav)*2.0
        wavefft[0:len(wav)/2] = 0.0
        return np.fft.ifft(wavefft)
    
    def lockin(self,wave,waveRef):
        '''Lockin amplifier return R  and phase '''
        x = wave*waveRef
        y = wave*np.imag(self.hilbertTran(waveRef))
        R = (np.average(x)**2+np.average(y)**2)**0.5*2.0
        phase = np.arctan(np.average(y)/np.average(x))*180.0/np.pi
        return R, phase
    
    def halfFrequency(self,wav):
        '''half the frequency of the input wave'''
        y = []
        n = len(wav)
        for i in range(0,n/2):
            y.append(wav[i])
            y.append((wav[i]+wav[i+1])/2.0)
        return y
    
    def doubleFrequency(self,wav):
        '''double the frequency of the input wave'''
        y = []
        n = len(wav)
        for i in range(0,n,2):
            y.append(wav[i])
        for k in range(n-1,0,-2):
            y.append(-wav[k])
        return y    
    def lowpassFilter(self,x,dt,RC):
        '''Continuous lowpass filter'''
        y = x
        a = dt/(RC+dt)
        for i in range (1, len(y)):
            y[i]=a *x[i]+(1-a)*y[i-1]
        return y
    def fftBandpassFilter(self, x, frqLowCutoff, frqHighCutoff, dtime):
        '''fft Bandpass filter'''
        fftresult = np.fft.rfft(x)
        fftfrq = np.fft.rfftfreq(len(x), dtime)
        for i in range (0,len(fftfrq)):
            if fftfrq[i]<frqLowCutoff:
                fftresult [i] = 0.0
            if fftfrq[i]>frqHighCutoff:
                fftresult [i:len(fftresult)] = 0.0
        return np.fft.irfftn(fftresult)
                
        
        
        
        