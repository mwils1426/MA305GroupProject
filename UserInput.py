# This is the user input section of the code
def userInput():
    optionPick = input("Would you like to review vaccine(s) percentages (1), hospitalizations per state (2), "
                       "or current percentage of those COVID-19? (3)")
    match optionPick:
        case "1":
            vaccineType = input("Please enter the name of the vaccine you would like to review: ")
            print("Vaccine Type: " + vaccineType)
            if vaccineType == ("Moderna", "Pfizer", "J&J"):
                dateRange = input("Please enter a date range for the following data you have requested: ")
                print("Date Range: " + dateRange)
                print("Would you like to compare another vaccine against the one you have chosen? ")
                compareVaccine = input("Please enter yes or no: ")
                print("Answer: ", compareVaccine)
                if compareVaccine == "Yes" or compareVaccine == "yes":
                    vaccineType2 = input("Please enter another vaccine to compare: ")
                    print("You will be comparing " + vaccineType + vaccineType2)
                    # insert grabbing info from CSV for date range and vaccine types
                else:
                    # print data for just one vaccine and date range
            return vaccineType, dateRange, compareVaccine, vaccinetype2, None, None
        case "2":
            hospitalStateNumbers = input("Please enter which state you would like to review: ")
            print("State chosen: ", hospitalStateNumbers)
            return vaccineType, dateRange, compareVaccine, vaccinetype2, hospitalStateNumbers, hstateNums(hospitalStateNumbers)
        case "3":
            dateRange = input("Please enter a date: ")
            print("Date Range: " + dateRange)
            num = # the # of folks with covid 19 given the date range, has to be a list/array
            print("The total average percentage of the population that had COVID-19 for the following dates are: " + avg())

def avg(num):
    sum = 0
    for t in num:
        sum = sum + t
    average = sum / len(num)
    return average
def hstateNums(hospitalStateNumbers):
    # pull info from csv depending on state
    # maybe make an array and have it go through each row until it find the correct one