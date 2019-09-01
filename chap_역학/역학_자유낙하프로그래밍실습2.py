import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)

x1=range(0,100)
y1=[i/2 for i in x1]

x2=range(0,10)
y2=[i/2 for i in x2]

x3=range(0,4)
y3=[i/2 for i in x3]

ax1.plot(x1,y1)
ax2.bar(x2,y2)
ax3.bar(x3,y3)

plt.show()
