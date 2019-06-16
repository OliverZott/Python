''' 
proj_plot:      - plot from file with measured values
                - 

TODO:           - WTF... plot size fucked up beyond believe 
                - besser plot_names als funktion an proj_plot uebergeben?
                - ongoing plot

@Date 04.06.2019
@author: Oliver Zott

https://matplotlib.org/3.1.0/tutorials/text/text_intro.html

'''

import matplotlib.pyplot as plt
import numpy as np
import os


def proj_plot(file_name):
    
    path = r'C:\Users\Dura\eclipse-workspace\Python\Projekt_1\Messwerte' 
    
    f = open(os.path.join(path, file_name), "r") 
    #f = open(file_name, "r")
    lines = f.readlines()[1:]               # ignore first line (header)
    
    D = np.loadtxt(lines,delimiter=";",usecols=[0],dtype="str")
    T = np.loadtxt(lines,delimiter=";",usecols=range(1,2))
    H = np.loadtxt(lines,delimiter=";",usecols=range(2,3))
    L = np.loadtxt(lines,delimiter=";",usecols=range(3,4))

    # define time array from numpy-ndarray 
    time_arr = np.array([])
    for time_str in D:
        x = time_str[11:16]
        time_arr = np.append(time_arr, x)

    date = D[1][0:11]
 
 
    # fig with sub plots
    plt.close('all')

    fig = plt.figure(figsize=(20, 10))
    ax1 = fig.add_subplot(2, 1, 1) 
    ax2 = fig.add_subplot(2, 1, 2) 
    
    #fig, (ax1, ax2) = plt.subplots(2, 1, sharey=False)
    ax1.grid()
    ax1.plot(time_arr, T, label='Temperature')
    ax1.plot(time_arr, H, label='Humidity')
    ax1.legend(loc='upper right', shadow=False, fontsize='x-large')
    ax1.set_title('Messwerte - ' + date)
    
    ax1.set_xticks((np.linspace(0,len(time_arr)+3, 17)))

    ax2.grid()
    ax2.plot(time_arr, L, label="Illuminance")
    ax2.legend(loc="upper right",fontsize='x-large')
    ax2.set_xticks((np.linspace(0,len(time_arr)+1, 17)))

    
    plt.savefig(path+"/" + date + ".svg", dpi=600, bbox_inches='tight')
    #plt.show()
    plt.close('all')
    

# test
#proj_plot('Messwerte_2019-06-07.txt')