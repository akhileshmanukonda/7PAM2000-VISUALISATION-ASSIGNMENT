#!/usr/bin/env python
# coding: utf-8

# # 7PAM2000 Applied Data Science 1 Assignment 1: Visualisation

# In[1]:


#header files to access the dataframe and graphs.
import numpy as nps
import pandas as pan
import matplotlib.pyplot as mat


# In[2]:


#read the dataframe from the excel
data_f = pan.read_csv("short-format.csv",skiprows=3)
data_f


# In[3]:


#print the information of the dataframe
data_f.info() 


# In[4]:


#count the null value of the dataframe
data_f.isnull().sum()


# In[5]:


#handle the null value contain in the dataframe
data_f = data_f.fillna(0)
data_f


# In[6]:


#count the null value of the dataframe
data_f.isnull().sum()


# In[7]:


#Describe the statistics of the dataframe
data_f.describe()


# In[8]:


'''The line graph display the details of the Overweight and underweight child based on the Country Short Name.
The suptitle used to set the title of the graph.The xlabel and ylabel used to label both the axis of the graph.
The xticks and yticks used to rotate the attributes names.The legend show the detail of the different data
ploted in the graph.'''

def line_graph(dataf):
    data_f1 = dataf.sample(15)
    data_f1.plot(x= "Country Short Name", y=['Overweight','Underweight'],figsize = (15,7)) #plot the graph
    mat.suptitle("\nOverweight and Underweight based on Country Short Name") #Title of the graph 
    mat.xlabel("Country Short Name")    #xlabels based on the dataframe
    mat.ylabel("Overweight, Underweight")   #ylabels based on the dataframe
    mat.xticks(rotation=90)             #using xticks to rotate the x-axis label
    mat.yticks(rotation=90)             #using yticks to rotate the y-axis label
    mat.legend()                        #show the ledgend


# In[10]:


line_graph(data_f)


# In[87]:


'''Pie chart is used to display the detail of afghanisthan based on the year period of wasting based on the sample.
The suptitle used to display the title of the graph.The xlabel and ylabel used to label both the axis of the graph.
The xticks and yticks used to rotate the attributes names.The legend show the detail of the different data
ploted in the graph.'''
def pie_Graph():
    #ploting the pie graph
    data_f2 = data_f.sample(5,random_state=1)
    data_f2.plot(x="Year period", y= "Wasting", kind='pie',figsize = (15,5)) 
    #The graph title 
    mat.suptitle("\n\nDetail of Afghanistan based on the Year period of wasting") 
    #xlabels based on the dataframe
    mat.xlabel("Afghanistan")
    #ylabels based on the dataframe
    mat.ylabel("Wasting") 
    #using xticks to rotate the x-axis label 
    mat.xticks(rotation=90)
    #using yticks to rotate the y-axis label 
    mat.yticks(rotation=90)     
    mat.legend(data_f["Year period"],loc = (1.1,0.5)) 


# In[88]:


pie_Graph()


# In[51]:


'''The bar plot is used to plot the graph that display the serever wasting, wasting, overweight, stunting, and underweight.
The serever wasting and wasting was the detail of the food and the overweight, studting and underweight of the childrens.
The suptitle() function was used to show the title.The xlabel and ylabel used to display the labels of both the axis.
The xticks and yticks both were used to rotate the axis attributes.
The legend was used to dislay the contain detial of based on the graph.'''
def bar_Graph():
    #ploting the kde graph with years
    data_f3 = data_f.sample(10)
    axes = data_f3.plot(x = "Year period",y= ["Severe wasting","Wasting","Overweight","Stunting","Underweight"],kind='bar',figsize =(15,7),cmap = "tab20_r")    
    #the graph title using suptitle
    mat.suptitle("\nDefine wastage of the food and weight of the child!")              
    #xlabels asign the value year
    mat.xlabel("Year") 
    #ylabels asign the value 2019
    mat.ylabel("Severe wasting, Wasting, Overweight, Stunting, Underweight")  
    #rotate the x-asix label using function-xticks
    mat.xticks(rotation=90)
    #rotate the y-axix label using function-yticks
    mat.yticks(rotation=90)    
    mat.legend(loc = 1)


# In[52]:


bar_Graph()


# In[ ]:




