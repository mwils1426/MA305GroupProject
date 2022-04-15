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

# # COVID-19 API Data Import
# covid19 = COVID19Py.COVID19("https://my-awesome-covid19-backend")

# # get covid data for the United States and the timelines.
# location = covid19.getLocationByCountryCode("US", timelines=True)
# # print(location) #print US data
# location = np.array(location)

# data_dictionary = location[0]  # remove outer array from location leaving it in dictionary form
# timelines = data_dictionary['timelines']  # get the timelines dictionary from the complete data dictionary
# confirmed_timeline = timelines['confirmed']  # get confirmed timeline dictionary from the timelines dictionary
# print(confirmed_timeline['timeline'])  # print the timeline dict from the confirmed dictionary

# print('country: ', data_dictionary['country'])
# print('Population: ', data_dictionary['country_population'])

# timelines_data = confirmed_timeline['timeline']
# print(timelines_data['2022-02-23T00:00:00Z'])


# # function to transform a dictionary datatype into an cell array datatype.
# def dict_to_array(dictionary1):
#     array1 = ['time', 'running total']
#     for key in dictionary1:
#         new_row = [key, dictionary1[key]]
#         array1 = np.vstack([array1, new_row])

#     print(array1)




# def importCDCCovidData():
#     # Download webpage
#     http = urllib3.PoolManager()
#     r = http.request('GET', 'https://covid.cdc.gov/covid-data-tracker/#vaccinations_vacc-total-admin-rate-total',
#                      preload_content = False)
#     r.auto_close = False

#     csvfile = r"C:\Users\Max Wilson\PycharmProjects\MA305Covid19\CovidVaccines.csv"

#     # get CSV URL
#     csvURL = "https://covid.cdc.gov/covid-data-tracker/#vaccinations_vacc-total-admin-rate-total" \
#              "/covid19_vaccinations_in_the_united_states.csv"

#     # get CSV
#     csvresp = urllib3.connection_from_url(csvURL)


#     # save CSV
#     print("Saving To: ", csvfile)
#     f = open(csvfile, "w")
#     f.write(csvdata.replace(r"rn", "n"))
#     f.close()

# if __name__ == '__main__':
#     # pull all covid19 data
#     importCDCCovidData()


###########################################################################
#new code: by connor 

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

    
    
    
