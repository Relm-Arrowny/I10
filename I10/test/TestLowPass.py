'''
Created on 7 May 2016

@author: Relm
'''
import numpy as np
import matplotlib.pyplot as plt
from SignalProcessing.WaveProcessing import WaveProcessing

wav = wav = WaveProcessing().waveGen()
for i in range (0,1000):
    twave =   WaveProcessing().waveGen(10000, 10.0, np.random.random()*1.0+1.0, np.random.random()*500.0+20.0,
                                        np.random.random()*10.0, np.random.random()*360)
    wav = np.add(twave , wav)
plt.subplot(211)
plt.plot(wav[0],wav[1])

wavLowpass = WaveProcessing().fftBandpassFilter(wav[1], 1.0,20.0, 10.0/10000.0)

plt.subplot(212)
plt.plot(wavLowpass)
print np.average(wav[1])
plt.show()
