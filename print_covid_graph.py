"""
Authors: Connor Castleberry, Max Wilson, Hannah Braslawsce, John Scheer
Date: 2 / 18 / 2022 
made by: Connor Castleberry
Description: MA 305 Class Project: This program is for printing result to
show the user graphs

Last Update: 4/18/2022

Instrustions: Dates is x-values of data point, Numbers is the y-values of 
data points, Title should be a string. Title will default to "Percentage of
population with COVID-19 per Month", if you input 'standard'.
input formats:
    Dates Format ex: [1/10/2021, 1/11/2021] list of dates, can't skip days!
    Numbers ex: [2, 6, 7, 8, 14, 23, 200] list of integers

Example code:
    
print_covid_graph([1/10/2021, 11/11/2021], [1, 10], 'standard')

"""
import numpy as np
import matplotlib.pyplot as plt

def print_covid_graph(Dates, Numbers, Title):
    #setup variables
    x_datapoints = []
    first_date = str(Dates[0])
    last_date = str(Dates[-1])
    
    # this section takes m/d/yyyy and turn it into into a number line
    for i in range(len(np.array(Dates ,dtype=object))):
        x_datapoints = [x_datapoints, i]
    
    if first_date[-1] == last_date[-1]: #if start and end dates are in same year
        if first_date[1] != '/':  #if month in double digits
            fd_month = int(first_date[0:1])
            if first_date[4] != '/': #if day of month in double digits
                fd_day = int(first_date[3:4])
            else:
                fd_day = int(first_date[3])
        else:  #else month in one digit save first digit
            fd_month = int(first_date[0])
            if first_date[3] != '/': #if day of month in double digits
                fd_day = int(first_date[2:3])
            else:
                fd_day = int(first_date[2])
    else:
        dates_length = 'longer than year'
            
            
    fig = plt.figure()
    plt.plot(x_datapoints, Numbers,'-')
    plt.legend(['data'], loc='best')
    #plt.ylim(1, 100)
    #plt.ylim(Dates[0],Dates[-1]) # automatic y limits
    #plt.xlim('January', 'December')  # month
    plt.xlabel('Month')
    plt.ylabel('Percentage of population with covid')
    if Title == 'standard':
        plt.title('Percentage of population with COVID-19 per Month')
    else:
        plt.title(Title)
    plt.show()
    

