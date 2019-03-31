
import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as pltal
import matplotlib.pyplot as pltg
import matplotlib.pyplot as pltc
import matplotlib.pyplot as pltrv1
import matplotlib.pyplot as pltrv
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
import matplotlib.patches as patches
import os.path
from os import path

import numpy as np
import pandas as pd
import pandas as pdal
import pandas as pdg









#=------------------------------------------------------------
def Gyroscope():


    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

    dataG = pdg.read_csv("Gyroscope.csv")
    listMG = dataG['Milliseconds']
    listXG = dataG['X']
    listYG= dataG['Y']
    listZG= dataG['Z']


    fig=pltg.figure(figsize=(30,5) ,facecolor='w', edgecolor='k')
    pltg.xticks(np.arange(5000,30000,5000))
    pltg.grid()

    fig.suptitle('Gyroscope', fontdict=font)
    plt.xlabel('Time(ms)', fontdict=font)
    fig.suptitle('Accelerometer', fontdict=font)

    pltg.plot(listMG[251:1350],listXG[251:1350], linewidth=2.0)
    # pltg.legend()
    # pltg.savefig('Graph/GyroXt.png', dpi = 300)
    # pltg.legend()
    pltg.plot(listMG[251:1350],listYG[251:1350], linewidth=2.0)
    # pltg.savefig('Graph/GyroXYt.png', dpi = 300)
    pltg.plot(listMG[251:1350],listZG[251:1350], linewidth=2.0)
    pltg.legend()
    pltg.savefig('Graph/GyroXYZt.png', dpi = 300,bbox_inches='tight')




#-------------------------------------------------
def Accelerometer():
    data = pd.read_csv("Accelerometer.csv")
    listM = data['Milliseconds']
    listX = data['X']
    listY= data['Y']
    listZ= data['Z']


    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }


    fig=plt.figure(figsize=(30,5) ,facecolor='w', edgecolor='k')
    plt.xticks(np.arange(5000,30000,5000))
    plt.grid()
    fig.suptitle('Accelerometer', fontdict=font)
    plt.xlabel('Time(ms)', fontdict=font)
    plt.ylabel('Sensor Reading(m/s^2)', fontdict=font)

    plt.plot(listM[251:1350],listX[251:1350], linewidth=2.0)
    # plt.legend()
    # plt.savefig('Graph/AccXt.png', dpi = 300,bbox_inches='tight')

    plt.plot(listM[251:1350],listY[251:1350], linewidth=2.0)
    # plt.legend()
    # plt.savefig('Graph/AccXYt.png', dpi = 300)

    plt.plot(listM[251:1350],listZ[251:1350], linewidth=2.0)
    plt.legend()


    # ax2 = fig.add_subplot(111, aspect='equal')
    # ax2.fill(listM, listX, zorder=0)
    # ax2.grid(True, zorder=0)
    #
    # ax2.add_patch(
    #      patches.Rectangle(
    #         (0.1, 0.1),
    #         10,5,
    #         fill=False      # remove background
    #      ) )
    # fig.savefig('rect2.png', dpi=90, bbox_inches='tight')


    # fig, ax = plt.subplots(1)
    # n=len(listM)
    # # Dummy errors (above and below)
    # xerr = np.random.rand(2, n) + 0.1
    # yerr = np.random.rand(2, n) + 0.2
    # errorboxes = []
    # rect = Rectangle((5000, 0),5000, 5)
    # errorboxes.append(rect)
    # pc = PatchCollection(errorboxes, facecolor='r', alpha=0.5,edgecolor='None')
    #
    # # Add collection to axes
    # ax.add_collection(pc)
    #
    # # Plot errorbars
    # artists = ax.errorbar(listM, listY, xerr=xerr, yerr=yerr,fmt='None', ecolor='k')
    plt.savefig('Graph/AccXYZt.png', dpi = 200,bbox_inches='tight')



    # plt.figure(figsize=(30,5) ,facecolor='w', edgecolor='k')
    # plt.xticks(np.arange(5000,30000,5000))
    # plt.grid()
    # plt.plot(listM,listX, linewidth=2.0)
    # plt.savefig('Graph/AccX.png', dpi = 300)


def AccelerometerLinear():
    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
    dataAL = pdal.read_csv("AccelerometerLinear.csv")
    listML = dataAL['Milliseconds']
    listXL = dataAL['X']
    listYL= dataAL['Y']
    listZL= dataAL['Z']


    fig=pltal.figure(figsize=(30,5) ,facecolor='w', edgecolor='k')
    pltal.xticks(np.arange(5000,30000,5000))
    pltal.grid()

    fig.suptitle('AccelerometerLinear', fontdict=font)
    plt.xlabel('Time(ms)', fontdict=font)
    plt.ylabel('Sensor Reading(m/s^2)', fontdict=font)

    pltal.plot(listML[251:1350],listXL[251:1350], linewidth=2.0)
    # pltal.legend()
    # pltal.savefig('Graph/AccLXt.png', dpi = 300)


    pltal.plot(listML[251:1350],listYL[251:1350], linewidth=2.0)
    # pltal.legend()
    # pltal.savefig('Graph/AccLXYt.png', dpi = 300)


    pltal.plot(listML[251:1350],listZL[251:1350], linewidth=2.0)
    pltal.legend()
    pltal.savefig('Graph/AccLXYZt.png', dpi = 300,bbox_inches='tight')



#----------------------------------------------------------
def Compass():
    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
    dataCm = pd.read_csv("Compass.csv")
    listMC = dataCm['Milliseconds']
    listXC = dataCm['X']
    listYC= dataCm['Y']
    listZC= dataCm['Z']


    fig=pltc.figure(figsize=(30,5) ,facecolor='w', edgecolor='k')
    pltc.xticks(np.arange(5000,30000,5000))
    pltc.grid()

    fig.suptitle('Compass', fontdict=font)
    plt.xlabel('Time(ms)', fontdict=font)
    plt.ylabel('Sensor Reading(m/s^2)', fontdict=font)

    pltc.plot(listMC[251:1350],listXC[251:1350], linewidth=2.0)
    # pltc.legend()
    # pltc.savefig('Graph/CompXt.png', dpi = 300)


    pltc.plot(listMC[251:1350],listYC[251:1350], linewidth=2.0)
    # pltc.legend()
    # pltc.savefig('Graph/CompXYt.png', dpi = 300)

    pltc.plot(listMC[251:1350],listZC[251:1350], linewidth=2.0)
    pltc.legend()
    pltc.savefig('Graph/CompXYZt.png', dpi = 300,bbox_inches='tight')


#----------------------------------------------------------
def RotationVector():
    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
    datarv = pd.read_csv("RotationVector.csv")
    listMRV = datarv['Milliseconds']
    listXRV = datarv['X']
    listYRV= datarv['Y']
    listZRV= datarv['Z']
    listCosRV= datarv['cos']

    fig=pltrv1.figure(figsize=(15,5) ,facecolor='w', edgecolor='k')
    pltrv1.xticks(np.arange(5000,30000,5000))
    pltrv1.grid()

    pltrv1.plot(listMRV[251:1350],listCosRV[251:1350], linewidth=2.0)
    pltrv1.legend()
    pltrv1.savefig('Graph/RotVecCost.png', dpi = 300,bbox_inches='tight')



    fig=pltrv.figure(figsize=(30,5) ,facecolor='w', edgecolor='k')
    pltrv.xticks(np.arange(5000,30000,5000))
    pltrv.grid()

    fig.suptitle('RotationVector', fontdict=font)
    plt.xlabel('Time(ms)', fontdict=font)
    plt.ylabel('Sensor Reading(m/s^2)', fontdict=font)

    pltrv.plot(listMRV[251:1350],listXRV[251:1350], linewidth=2.0)
    # pltrv.legend()
    # pltrv.savefig('Graph/RotVecXt.png', dpi = 300)


    pltrv.plot(listMRV[251:1350],listYRV[251:1350], linewidth=2.0)
    # pltrv.legend()
    # pltrv.savefig('Graph/RotVecXYt.png', dpi = 300)

    pltrv.plot(listMRV[251:1350],listZRV[251:1350], linewidth=2.0)
    pltrv.legend()
    pltrv.savefig('Graph/RotVecXYZt.png', dpi = 300,bbox_inches='tight')

def main():

    pa=os.getcwd()
    print(pa)
    print("---------HELLO -----------------------------")

    if path.exists('Accelerometer.csv'):
         Accelerometer()
    if path.exists('Gyroscope.csv'):
        Gyroscope()
    if path.exists('AccelerometerLinear.csv'):
        AccelerometerLinear()
    if path.exists('Compass.csv'):
        Compass()
    if path.exists('RotationVector.csv'):
        RotationVector()

if __name__ == '__main__':
    main()
