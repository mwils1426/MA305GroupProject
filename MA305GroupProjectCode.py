
# Authors: Connor Castleberry, Max Wilson, Hannah Braslawsce, John Scheer
# Date: 2 / 18 / 2022
# Description: MA 305 Class Project, Covid statistics analyzer

# Note: COVID19PY code must be in the same folder as this program

# imports data
import COVID19Py
import numpy as np
import urllib3
import io
import openpyxl as openpyxl
import pandas as pd
# imports user-defined functions
#from UserInput import *

###########################################################################
#new code: by Connor 

#this section is for saving data from the CSV file to an excel spreadsheet
# note must turn csv into a panda file. or we could manual take the csv file and use the built
# excel csv file reader and do it without coding


from openpyxl import Workbook
from openpyxl.utils import get_column_letter

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
from itertools import islice
from openpyxl import load_workbook
wb = load_workbook(filename = 'Covid by state.xlsx')
sheet_cases = wb['Cases']

data = sheet_cases.values
cols = next(data)[1:]
data = list(data)
idx = [r[0] for r in data]
data = (islice(r, 1, None) for r in data)
df = pd.DataFrame(data, index=idx, columns=cols)


#get vaccineType numbers

# apply date range to vaccinetype1

# print graph 1

# if second vaccine requested
    # get vaccineType2 numbers

    # apply date range to vaccinetype2
    # print graph 2
###########################################################################
