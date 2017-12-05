'''
Created on 18 Oct 2017

@author: wvx67826
'''
import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt



f = open("S:\Science\I10\Tools\I10_Python\I10_python\I10\src\Magnet_calibration\cal4bars_slotted2.dat",'r')
data = ascii.read(f)
poly1 = np.polyfit(data["col1"],data["col2"], 18)
poly2 = np.polyfit(data["col2"],data["col1"], 18)
poly3 = [1.16037577500095521697E-15,-2.04507433061767536694E-13,1.64442582768738713139E-11,-7.98012177305311099537E-10,2.60418200105020154749E-08,-6.02290596049618574667E-07,1.01233131325416681601E-05,-1.24439882884389219552E-04,1.10418593909395032146E-03,-6.75483164298878047821E-03,2.46117863057059779730E-02,-1.48955169285745984281E-02,-3.73281063845343596963E-01,2.20632755759183174504E+00,-6.39209835092398037659E+00,1.05162348085858852187E+01,-1.02710537475533598695E+01,-1.20011732660689651730E+00,1.40298401771834505780E+02]
p1 = np.poly1d(poly1)
p2 = np.poly1d(poly2)
p3 = np.poly1d(poly3)
print poly1 - poly3
plt.plot(data["col1"],data["col2"])
plt.plot(data["col1"],p1(data["col1"]))
plt.plot(data["col1"],p3(data["col1"]))
plt.show()
f.close()

f = open("poly2mm.data",'w+')
for i in range (0, len(poly1)):
    
    f.write( "%.20E," %poly1[i])
f.write("\n")
for i in range (0, len(poly2)):
    
    f.write(  "%.20E," %poly2[i])
    
