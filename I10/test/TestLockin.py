'''
Created on 7 May 2016

@author: Relm

Playground, mostly for testing and have fun.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from SignalProcessing.WaveProcessing import WaveProcessing
Raverage= 0
Ra= 0
for n in range (0,100):
    print n
    nDataPoint =np.random.random_integers(6000,10000)
    time = 50.0+np.random.random()

    wav = np.add(WaveProcessing().squreWaveGen(nDataPoint, time,  1.0,  9.0, np.random.random()*5.0, np.random.random()*360.0),
                 WaveProcessing().waveGen(nDataPoint, time,  1.0,  18.0, np.random.random()*5.0, np.random.random()*360.0))
    wavRef =WaveProcessing().squreWaveGen(nDataPoint, time,  1.0,  9.0, np.random.random()*5.0, np.random.random()*360.0)
#    wavRef = WaveProcessing().waveGen(nDataPoint, time,  1.0,  9.0, np.random.random()*5.0, np.random.random()*360.0)   
    for i in range (0,1000):
        twave = WaveProcessing().waveGen(nDataPoint, time, np.random.random()*0.9+0.0, np.random.random()*60.0+19.2,
                                            np.random.random()*5.0, np.random.random()*360)
        twave = np.add(twave,WaveProcessing().waveGen(nDataPoint, time, np.random.random()*0.9+0.0, np.random.random()*5.8,
                                            np.random.random()*5.0, np.random.random()*360))
        
        wav = np.add(twave , wav)
    R=[]
    f = []
    Re = []
    '''
    plt.plot(wav[1])
    plt.show()
    '''
    wav = wav[0], WaveProcessing().fftBandpassFilter(wav[1], 1.0, 1000, time/nDataPoint)
    wavRef = wavRef[0], WaveProcessing().fftBandpassFilter(wavRef[1], 2.0, 17.0, time/nDataPoint)
    Re.append(WaveProcessing().lockin(wav[1], wavRef[1]))
    Re.append(WaveProcessing().lockin(wav[1][len(wav[1])/2:], WaveProcessing().doubleFrequency((wavRef[1]))))
    
    plt.subplot(411)
    plt.plot(wav[0],wav[1])
    plt.plot(wav[1])
    plt.subplot(412)
    plt.plot(WaveProcessing().doubleFrequency((wavRef[1])))
    
    
    for i in np.arange (1,50,0.1):
        f.append(i)
        R.append( WaveProcessing().lockin(wav[1],WaveProcessing().waveGen(nDataPoint, time,  1.0,  i, 0, 0) [1])[0])
    
    
    print Re,nDataPoint, time
    plt.subplot(413)
    plt.plot(np.fft.rfftfreq(nDataPoint, time/nDataPoint),np.abs(np.fft.rfft(wav[1]))*2.0/nDataPoint)
    plt.yscale('log')
    plt.subplot(414)
    plt.plot(f,R)
    plt.show()
    Raverage = Raverage+Re[0][0]
    Ra = Ra+Re[1][0]
print Raverage/1, Ra/1.

#plt.plot(np.imag(coeffs))
#plt.plot(np.real(coeffs))
    