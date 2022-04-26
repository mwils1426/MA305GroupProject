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
    Dates Format ex: [1/10/2021, 1/11/2021] list od strings, can't skip days!
    Numbers ex: [2, 6, 7, 8, 14, 23, 200] list of integers

Example code:
    
print_covid_graph(['1/10/2021', '11/11/2021'], [1, 10], 'standard')

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
        x_datapoints.append(i)
    
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
            
    #find max of numbers
    max_number = np.max(Numbers)
    # tick markers
    num_ticks = np.ceil(len(Dates)/5)
    a = 0
    tick_mark = [Dates[0]]
    for j in Dates:
        a = a + 1
        if a == num_ticks:
            tick_mark.append(j)
            a = 0
    tick_mark.append(Dates[-1])
    fig, ax= plt.subplots()
    ax.plot(Dates, Numbers,'-')
    ax.legend(['data'], loc='best')
    plt.ylim(1, max_number*1.1)
    #plt.xlim(x_datapoints[0],x_datapoints[-1]) # automatic y limits
    plt.xlim(Dates[0], Dates[-1])  # month
    plt.xlabel('Month')
    plt.ylabel('Percentage of population with covid')
    ax.set_xticks((tick_mark))
    if Title == 'standard':
        fig.suptitle('Percentage of population with COVID-19 per Month')
    else:
        fig.suptitle(Title)
    return plt.show()

#==========================================================================

#function display test code 

test_numbers = np.array([12918813, 13436108, 15701638, 15647349, 16644019, 16436393,17409442, 1982448, 22697489, 25232343, 25199142, 26636596])
test_dates = np.array(['1/1/2021', '2/1/2021', '3/1/2021', '4/1/2021', '5/1/2021', '6/1/2021', '7/1/2021', '8/1/2021', '9/1/2021', '10/1/2021', '11/1/2021', '12/1/2021'])
title = 'Test plot'

print_covid_graph(test_dates, test_numbers, title)






