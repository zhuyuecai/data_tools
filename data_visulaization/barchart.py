# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:52:47 2016

@author: MusfiqurRahman
"""

import numpy as np
import matplotlib.pyplot as plt
from pylab import *

student = [3, 4, 3, 2, 0, 2]
BCEE = [2, 0, 3, 4, 4, 0]
CSE = [0, 2, 4, 3, 0, 2]
ECE = [2, 0, 4, 0, 0, 2]
ENCS = [2, 3, 2, 4, 0, 2]


def autolabel(rects, ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        #print(height)
        if height == 4.0:
            ax.text(rect.get_x() + rect.get_width()/2.,1.0*height + .05, 'A', ha='center', va='bottom', fontsize = 8)
        elif height == 3.0:
            ax.text(rect.get_x() + rect.get_width()/2.,1.0*height + .05, 'B', ha='center', va='bottom', fontsize = 8)
        elif height == 2.0:
            ax.text(rect.get_x() + rect.get_width()/2.,1.0*height + .05, 'C', ha='center', va='bottom', fontsize = 8)
        else:
            ax.text(rect.get_x() + rect.get_width()/2.,1.0*height + .05, 'F', ha='center', va='bottom', fontsize = 8)



def hist(ID):
    graph_title = "Visual representation of the performace of ID: " + str(ID) + " in different Graduate Attributes"    
    N = len(student)
    
    ind = np.arange(N) + 10   # the x locations for the groups
    width = 0.15       # the width of the bars
    #plt.xlim([0,10])
    fig, ax = plt.subplots()
    
    #rects0 = ax.bar(ind)
    rects1 = ax.bar(ind, tuple(student), width, color='royalblue')
    rects2 = ax.bar(ind + width, tuple(BCEE), width, color='red')
    rects3 = ax.bar(ind+ 2*width, tuple(CSE), width, color='yellow')
    rects4 = ax.bar(ind+ 3*width, tuple(ECE), width, color='green')
    rects5 = ax.bar(ind+ 4*width, tuple(ENCS), width, color='gray')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Grades Points', fontsize = 10)
    ax.set_title(str(graph_title), fontsize = 10)
    ax.set_xlabel('Graduate Attributes')
    plt.xlim(9.8, (9.8+N + 0.2))
    plt.ylim(0, 5)
    labels = ('GA 1', 'GA 2', 'GA 3', 'GA 4', 'GA 5', 'GA 6')
    print(labels)
    ax.get_xaxis().set_visible(True)
    ax.set_xticks(ind + 2.5*width)
    ax.set_xticklabels(labels, fontsize = 8)
    """    
    labels = list(str(student_average.keys()))
    print(labels)
    point = 10.2
    position = []
    for i in range (0, len(labels)):
        position.append(point)
        point = point + 1
    print(position)    
    #position = [10.2, 11.2, 12.2, 13.2, 14.2, 15.2, 16.2, 17.2, 18.2, 19.2, 20.2, 21.2]
    min_y = 0
    for i in xrange(len(labels)):
            ax.text(position[i],min_y-2,labels[i], fontsize = 10)
    """
    ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('Student\'s Avg', 'BCEE Avg', 'CSE Avg', 'ECE Avg', 'ENCS Avg'), fontsize = 10)    
        
    autolabel(rects1, ax)
    autolabel(rects2, ax)
    autolabel(rects3, ax)
    autolabel(rects4, ax)
    autolabel(rects5, ax)
    plt.show()
    #plt.savefig("/home/sumit/Documents/CEAB/Plots/ResultsForUS2_Plots/" + str(ID) +".pdf")

hist ('2567866')
