import numpy as np
import matplotlib.pyplot as plt
import time

try:
    '''
    x=np.arange(1,5)
    print(len(x))
    y=np.arange(6,10)
    print(len(y))
    print(x,y)
    fig=plt.figure()
    plt.plot(x,y,linewidth=1, color = 'red',marker='o')
    plt.plot(x,y/2,linestyle='dashed')
    plt.grid(True)
#fig2
    fig2=plt.figure()
    x=np.randon.normal(50,10,1000)
    plt.hist(x,rwidth =0.3, color='orange')
# fig 3
    x=np.arange(1,5)
    print(len(x))
    y=np.arange(6,10)
    fig3=plt.figure()
    ax=fig3.add_subplot(1,1,1)
    ax.scatter(x,y,c='orange')
    #plt.close()
    plt.show()
    #fig2.savefig("hist.png")
    #fig.savefig("figure.png")
    #plt.close()
    #plt.close()
    '''
    x=np.arange(1,5)
    y=np.arange(6,10)

    x1=np.random.rand(30)
    y1=np.random.rand(30)
    x2=np.random.rand(30)
    y2=np.random.rand(30)

    fig4=plt.figure()
    ax=fig4.add_subplot(1,1,1)
    ax.scatter(x1,y1,alpha=0.2,c='orange')
    ax.scatter(x2,y2,alpha=0.4,c='red')
    plt.show()
#    while 1:
#        a=1
except KeyboardInterrupt:
    print("end")