'''
Created on 7 May 2016

@author: Relm

Playground, mostly for testing and have fun.
'''

import numpy as np
import matplotlib.pyplot as plt
from SignalProcessing.WaveProcessing import WaveProcessing

nDataPoint = np.random.random_integers(6000,10000)
time = 10.0+np.random.random()

wav = np.add(WaveProcessing().waveGen(nDataPoint, time,  1.5,  9.0, 0, 0),
             WaveProcessing().waveGen(nDataPoint, time,  1.5,  18.0, 0, 0))

wavRef = WaveProcessing().waveGen(nDataPoint, time,  1.0,  9.0, 0, 0)   
for i in range (0,1000):
    twave =   WaveProcessing().waveGen(nDataPoint, time, np.random.random()*1.0+1.0, np.random.random()*500.0+11.0,
                                        np.random.random()*1.0, np.random.random()*360)
    wav = np.add(twave , wav)
R=[]
f = []
Re = []
wav = wav[0], WaveProcessing().fftBandpassFilter(wav[1], 0.1, 1000.0, time/nDataPoint)
plt.plot(wav[1])
plt.show()
Re.append(WaveProcessing().lockin(wav[1], wavRef[1]))
Re.append(WaveProcessing().lockin(wav[1], WaveProcessing().doubleFrequency((wavRef[1]))))

plt.subplot(411)
#plt.plot(wav[0],wav[1])
plt.plot(wav[1])
plt.subplot(412)
plt.plot(wav[0], wavRef[1])

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
#plt.plot(np.imag(coeffs))
#plt.plot(np.real(coeffs))
    