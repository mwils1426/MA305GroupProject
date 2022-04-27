
# Authors: Connor Castleberry, Max Wilson, Hannah Braslawsce, John Scheer
# Date: 2 / 18 / 2022
# Description: MA 305 Class Project, Covid statistics analyzer

# Note: COVID19PY code must be in the same folder as this program

# imports data
#import COVID19Py
import numpy as np
#import urllib3
import io
import openpyxl
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from itertools import islice
from openpyxl import load_workbook
# imports user-defined functions
#from UserInput import *
import UserInput

vaccineType, dateRange, compareVaccine, vaccineType2, empty1, empty2 = UserInput()


###########################################################################
#new code: by Connor 

#this section is for saving data from the CSV file to an excel spreadsheet
# note must turn csv into a panda file. or we could manual take the csv file and use the built
# excel csv file reader and do it without coding


# wb = Workbook()

# dest_filename = 'covid19_data.xlsx'
# ws1 = wb.active
#ws1.title = "covid_data"
# below is dataframe it needs to filled with the data
df = pd.DataFrame()

# for r in pd.dataframe_to_rows(df, index=True, header=True):
#     ws1.append(r)

# for cell in ws['A'] + ws[1]:
#     cell.style = 'Pandas'

# wb.save(filename = dest_filename)

#
#vaccineType, dateRange, compareVaccine, vaccinetype2, hospitalStateNumbers, hstateNumbers = UserInput()

#importing data from excel sheet

#This section can be used if we store the data in excel as a panda dataframe
wb = load_workbook(filename = 'Covid by state.xlsx')
sheet_cases = wb['Cases']

data = sheet_cases.values
cols = next(data)[1:]
data = list(data)
idx = [r[0] for r in data]
data = (islice(r, 1, None) for r in data)
df = pd.DataFrame(data, index=idx, columns=cols)

# get data

# if bool(vaccineType):  #if no vaccine requested
# # is false: report cases numbers 
#          get data for cases
# elif bool(vaccineType2):  #if only one vaccine requested
#   #get data for the the vaccine 1
# else:  #if a rtwo vaccine is request
#   #get data for the the vaccine 1 and 2

#graphing 

# # graph vaccineType1
# if bool(vaccineType):
#     print_covid_graph(dates, cases, ('Covid Case between', dates[0], 'and', dates[-1]))
# elif not bool(vaccineType2):
#      print_covid_graph(dates, vaccine_1, (VaccineType, 'administered between', dates[0], 'and', dates[-1]))
#      print_covid_graph(dates, vaccine_2, (VaccineType2, 'administered between', dates[0], 'and', dates[-1]))
# else:
#     print_covid_graph(dates, vaccine_1, (VaccineType, 'administered between', dates[0], 'and', dates[-1]))

###########################################################################
    
    
    
