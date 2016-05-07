'''
Created on 7 May 2016

@author: Relm

Playground, mostly for testing and have fun.
'''

import numpy as np
from I10.src.SignalProcesiing import WaveProcessing
 

'''
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
'''
    