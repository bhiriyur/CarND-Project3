import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from random import randint



def balanced():
    A = pd.read_csv('driving_log.csv')
    n = 11
    bins = np.linspace(-0.6,0.6,n)
    plt.hist(A['steering'],bins=bins)


    plt.figure()
    B = []
    for i in range(n-1):
        start, end = bins[i], bins[i+1]
        Bi = A[(A['steering']>start) & (A['steering']<=end)]
        B.append(Bi.sample(17))
        print(i,start,end,len(B[-1]))
        plt.hist(B[-1]['steering'])

    #print(B)
    B = pd.concat(B).reset_index(drop=True)
    plt.figure()
    plt.hist(B['steering'], bins=bins,color='r')

    plt.show()

balanced()


def plot_hists():
    print(os.getcwd())
    for k in range(20):
        i = randint(0,A.shape[0])
        cfile = A['center'][i].strip()
        lfile = A['left'][i].strip()
        rfile = A['right'][i].strip()
        steer = A['steering'][i]
        throttle = A['throttle'][i]
        brake= A['brake'][i]
        speed= A['speed'][i]
        #print("File {:3}, | Steering = {} Throttle = {} Brake = {} Speed = {}".format(i,steer,throttle,brake,speed))
        plt.figure()
        plt.subplot(3,1,1)
        plt.plot(A['steering'],'b')
        plt.plot(i,A['steering'][i],'mo')
        plt.title('Steering')
        plt.subplot(3,1,2)
        plt.plot(A['speed'], 'r')
        plt.plot(i, A['speed'][i], 'mo')
        plt.title('Speed')
        plt.subplot(3,1,3)
        plt.plot(A['throttle'], 'g')
        plt.plot(i, A['throttle'][i], 'mo')
        plt.title('Throttle')

        plt.figure(figsize=(5,9))
        plt.subplot(3,1,1)
        plt.imshow(plt.imread(cfile))
        plt.title("{:3}, | steer:{:4.2f} throttle:{:4.2f} speed:{:4.2f}".format(i,steer,throttle,speed))
        plt.axis('off')
        plt.subplot(3,1,2)
        plt.imshow(plt.imread(lfile))
        plt.axis('off')
        plt.subplot(3,1,3)
        plt.imshow(plt.imread(rfile))
        plt.axis('off')
        plt.show()