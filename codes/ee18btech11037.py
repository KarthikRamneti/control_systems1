import matplotlib.pyplot as plt
import numpy as np
import math

w = np.linspace(0,1000,100000)

#bode phase plot for pole = 0.1
y1 = []
for i in w:
	if i <= 0.01:
		y1.append(0)
	if i > 0.01 and i <1:
		y1.append(-45*(math.log10(i)+2)) #eqn of straight line
	if i >= 1:
		y1.append(-90)


#bode phase plot for pole = 1
y2 = []
for i in w:
	if i <= 1:
		y2.append(0)
	if i > 1 and i <100:
		y2.append(-45*(math.log10(i))) #eqn of straight line
	if i >= 100:
		y2.append(-90)


plt.semilogx(w,y1,label='for pole = 0.1')
plt.axvline(x=0.01,dashes=[5, 5, 5, 5], color = 'c')
plt.axvline(x=0.1,dashes=[5, 5, 5, 5], color = 'c')
plt.axvline(x=1,dashes=[5, 5, 5, 5], color = 'c')
plt.axvline(x=10,dashes=[5, 5, 5, 5], color = 'c')
plt.axvline(x=100,dashes=[5, 5, 5, 5], color = 'c')
plt.axhline(y=-45,dashes=[5, 5, 5, 5], color = 'c')
plt.semilogx(w,y2,label='for pole = 10')

plt.title("Phase Plot")
plt.legend()

#if using termux
plt.savefig('./figs/ee18btech11001/ee18btech11001_2.pdf')
plt.savefig('./figs/ee18btech11001/ee18btech11001_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_2.pdf"))
#else
#plt.show()
	
