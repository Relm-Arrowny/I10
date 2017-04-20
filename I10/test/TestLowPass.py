'''
Created on 7 May 2016

@author: Relm
'''
import numpy as np
import matplotlib.pyplot as plt
from SignalProcessing.WaveProcessing import WaveProcessing

wav = WaveProcessing().waveGen(9999)
for i in range (0,1000):
    twave =   WaveProcessing().waveGen(9999, 10.1, np.random.random()*1.0+1.0, np.random.random()*500.0+20.0,
                                        np.random.random()*10.1, np.random.random()*360)
    wav = np.add(twave , wav)
plt.subplot(211)
plt.plot(wav[0],wav[1])

wavLowpass = WaveProcessing().fftBandpassFilter(wav[1], 9.1,10.0, 10.1/9999.0)

plt.subplot(212)
plt.plot(wavLowpass)
print np.average(wav[1])
plt.show()
