# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 14:00:59 2016
@author: Yuecai Zhu
"""



import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from dataProcess import *



"""
@param data1: list of lists which contain your data. Left hand side of each bar (or array of arrays, iterable)
@param data2: list of lists which contain your data. right hand side of each bar (or array of arrays, iterable)
@param xlabel: name of the x axis
@param bar_labels: name of each bar, hence must have the same length as data 1 and 2
@param title: title of the figure
@param filename: the name of the saved figure file  


"""
class TwoSidedVioline(self):
    self.xoffset = 0.5
    self.yoffset = 2
    def __init__(self,filename = 'foo.png',data1,data2,xlabel,bar_labels,title='',points=50,widths=0.85):
        self.data1= data1
        self.data2= data2
        self.xlabel = xlabel
        self.bar_labels = bar_labels
        self.title = title
        self.points = points
        self.widths = widths
        self.filename = filename
        if len(data1)!=len(data2):
            raise Exception('data1 and data2 must have the same length')
        if len(data1)!=len(bar_labels):
            raise Exception('data1 and bar_labels must have the same length')
         
    """
    plot function will save the resulting figure file
    """    
    def plot(self):
        violine_plot_2side(self.data1,self.data2,self.xlable,self.bar_labels,self.title,self.xoffset,self.yoffset)
            
    
    #private function, show the value on the figure, could be cmean, cmax etc.   
    def show_value_by_name(ax,figure_element,title,direction,y_offset = 0):
        segment = figure_element[title].get_segments()
        #m1 = np.mean(figure_elements_1["cmeans"].get_paths()[0].vertices[:, 0])
        value_segment=[]
        min_r=0
        max_r = 0
        for v in segment: 
            min_r = min(min_r,v[0][1])
            max_r = max(max_r,v[0][1])
            
            if direction == "right":       
                value_segment.append([[0.5*(v[0][0]+v[1][0]),v[0][1]],v[1]])
                ax.text(v[1][0],v[1][1]+y_offset,title + "="+str(recover_range(v[1][1])))
                #plt.annotate(title + "="+str(recover_range(v[1][1])), xy=v[1], xytext=v[1], arrowprops=dict(facecolor='black', shrink=0.02), width = 0.1)
            else:
                value_segment.append([v[0],[0.5*(v[0][0]+v[1][0]),v[1][1]]])
                ax.text(v[0][0],v[0][1]+y_offset,title + "="+str(recover_range(v[1][1])))
                #plt.annotate(title + "="+str(recover_range(v[1][1])), xy=v[0], xytext=v[0], arrowprops=dict(facecolor='black', shrink=0.05))
        figure_element[title].set_segments(value_segment)
        return [min_r,max_r]
    
    # def anotate_value_by_name(figure_element,title,value,direction):
    #     segment = figure_element[title].get_segments()
    #     #m1 = np.mean(figure_elements_1["cmeans"].get_paths()[0].vertices[:, 0])
    #     value_segment=[]
    #     for v in segment:        
    #         plt.annotate(title + "="+str(recover_range(v[1][1])), xy=v[1], xytext=v[1], arrowprops=dict(facecolor='black', shrink=0.05))
    #two sided violine plot, input 2 list of data, 1 list of position
    
    #plotting function, used to plot the figure
    def violine_plot_2side(data1,data2,xlable,labels,title,xoffset,yoffset):
        plt.figure()
        figure_size = (20, 7)
        
        #length_position = len(position)
        #l = [i*30+20 for i in xrange(length_position)]
        position = np.arange(0, len(data1))
        #plot_width = ( 40* 0.6)
        f, ax = plt.subplots(figsize=figure_size)#figsize=(18, 7)
        figure_elements_1 = ax.violinplot(data1, points=50, positions=position, widths=0.85,
                   showmeans=True, showextrema=True, showmedians=True)
        for b in figure_elements_1['bodies']:
            m = np.mean(b.get_paths()[0].vertices[:, 0])
            b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], -np.inf, m)
            b.set_color('r')
        figure_elements_2= ax.violinplot(data2, points=50, positions=position, widths=0.85,
                   showmeans=True, showextrema=True, showmedians=True)
        for b in figure_elements_2['bodies']:
            m = np.mean(b.get_paths()[0].vertices[:, 0])
            b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
            b.set_color('b')
    
        show_value_by_name(ax,figure_elements_1,"cmeans","right",-1)
        show_value_by_name(ax,figure_elements_1,"cmedians","right",0)
        
        min_1 = show_value_by_name(ax,figure_elements_1,"cmins","right")[0]
        max_1=show_value_by_name(ax,figure_elements_1,"cmaxes","right",0.2)[1]
        
        show_value_by_name(ax,figure_elements_2,"cmeans","left",)
        show_value_by_name(ax,figure_elements_2,"cmedians","left",)
        
        min_2 =show_value_by_name(ax,figure_elements_2,"cmins","left")[0]
        max_2=show_value_by_name(ax,figure_elements_2,"cmaxes","left")[1]
        
        min_y = min(min_1,min_2)
        max_y = max(max_1,max_2)
    
        plt.xlim(position[0]-xoffset,position[1]+xoffset)
        plt.ylim(min_y,max_y+2.5+yoffset)
        plt.xlabel(xlable)
        plt.ylabel("log1p(gain hour)")
        ax.get_xaxis().set_visible(False)
        #plt.axis('off')
        proxies = [create_proxy(item) for item in ["r","b"]]
        ax.legend(proxies, ["gain hours in failure detection","gain hours in frt"], numpoints=1, markerscale=2)
        
        for i in xrange(len(data1)):
            ax.text(position[i],min_y-1,labels[i])
        # the line at y=0
        ax.plot([position[0]-xoffset,position[1]+xoffset],[0,0],linestyle = '--')
        ax.text(0.5*(position[len(data1)-1]+position[0]),min_y-yoffset,xlable)
        plt.title(title)
    
        #plt.show()
        plt.savefig(self.filename)
    
        #plt.savefig('foo.png')
    #private function, a helper to make the legend
    def create_proxy(label):
    line = matplotlib.lines.Line2D([0], [0], linestyle='-', mfc=label,
                mec='none', color = label)#marker=r'$\mathregular{{{}}}$'.format(label))
    return line
"""
execution: python script_name.py  period n_runner
"""
if __name__ =="__main__":

   
    violine_plot_2side(data_failure_detection,data_frt,xlable,lables,title)
