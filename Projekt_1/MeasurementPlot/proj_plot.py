''' 
proj_plot:      - plot from file with measured values
                - 

TODO:           - WTF... plot size fucked up beyond believe 
                - besser plot_names als funktion an proj_plot uebergeben?

@Date 04.06.2019
@author: Oliver Zott

https://matplotlib.org/3.1.0/tutorials/text/text_intro.html

'''

import matplotlib.pyplot as plt
import numpy as np



def proj_plot(file_name):
    
    path = r'C:\Users\Dura\eclipse-workspace\Python\Projekt_1\Messwerte' 
    
    D = np.loadtxt(file_name,delimiter=";",usecols=[0],dtype="str")
    TH = np.loadtxt(file_name,delimiter=";",usecols=range(1,3))
    L = np.loadtxt(file_name,delimiter=";",usecols=range(3,4))

    
    # Open current file 
    f = open(file_name, "r")

    date = f.readline(10)
    time_arr = np.array([])
    
    #print(date)

    for lines in f:
        x= lines[11:19]
        time_arr = np.append(time_arr, x)
    
    
    plt.close('all')

    axes = plt.gca()
    plt.subplot(2, 1, 1)
    plt.plot(time_arr,TH, label='Loaded from file!')
    plt.xlabel('Time')
    plt.ylabel('Value')
    axes.set_ylim([0,100])
    plt.title('Messwerte - ' + date)
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(time_arr,L , label='Loaded from file!')
    plt.xlabel('Time')
    plt.ylabel('lx')
    axes.set_ylim([0,1000])
    plt.legend()
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.5)
    

    
    plt.savefig(path+"/test.svg", format="svg", dpi=600)
    plt.show()
    #fig.savefig(my_path + '/Sub Directory/graph.png')
   
    #plt.savefig(path+"test.jpg", format="jpg")
    
    '''
    my_path = os.path.abspath(__file__) # Figures out the absolute path for you in case your working directory moves around.
    fig.savefig(my_path + '/Sub Directory/graph.png')
    '''
    
    