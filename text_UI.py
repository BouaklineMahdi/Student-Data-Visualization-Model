# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Kirkland Irving"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101275314"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-59"

#==========================================#
# Place your script for your text_UI after this line
from sort import *
from load_data import *
from curve_fit import *
from histogram import *


def text():
    the_list = ['L', 'S', 'C', 'H', 'E']
    loaddataaverage = []
    schools = ["GP", "MB", "CF", "BD", "MS"]

    operator = input(
        "The available commands are:\n    L)oad data\n    S)ort data\n    C)urve fit\n    H)istogram\n    E)xit\n\nPlease type your command: ")

    if operator.capitalize() == "L":
        load_operator = input("Please enter the name of the file: ")
        load_attribute = input(
            "Please enter the attribute to use a filter: ")
        if load_attribute == "All":
            print("Please enter: 'StudyTime', 'Absences', 'G1', 'G2', 'G3', 'School', 'Age', 'Health', or 'Failures'")
            load_attribute = input(
                "Please enter the attribute to use a filter: ")

        if load_attribute == "School":
            load_value = input("Please enter the value of the attribute: ")
            if load_value not in schools:
                load_value = input(
                    "Please enter either the school:\n'GP', 'MB', 'CF', 'BD', 'MS': ")

            if load_value in schools:
                loaddata = load_data(
                    load_operator, (load_attribute, load_value))

                loaddataaverage = add_average(loaddata)

                print('Data loaded')

                operator = input(
                    "The available commands are:\n    L)oad data\n    S)ort data\n    C)urve fit\n    H)istogram\n    E)xit\n\nPlease type your command: ")

        else:
            load_value = input("Please enter the value of the attribute: ")

            loaddata = load_data(load_operator, (load_attribute, load_value))

            loaddataaverage = add_average(loaddata)

            print('Data loaded')

            operator = input(
                "The available commands are:\n    L)oad data\n    S)ort data\n    C)urve fit\n    H)istogram\n    E)xit\n\nPlease type your command: ")

    if operator.capitalize() == "S":
        data_set = {'Age', 'StudyTime', 'Failures', 'G_Avg'}

        empty = []

        if loaddataaverage == empty:
            print("File not loaded. Please, load a file first")
            return(text())

        sort_operator = input(
            "Please enter the attribute you want to use for sorting:   \n'Age'    'StudyTime'    'Failures'    'G_Avg'\n: ")

        if sort_operator not in data_set:
            print("Invalid command")
            return(text())

        order = input("Ascending (A) or Descending (D) order: ")

        if sort_operator in data_set:

            age_sort = sort(loaddataaverage, order, sort_operator)

            yesorno = input(
                'Data Sorted. Do you want to display the data?\n')

            if yesorno == 'Y':
                print(age_sort)
                return(text())

            else:
                return(text())

        return (text())

    if operator.capitalize() == "C":

        empty = []

        if loaddataaverage == empty:
            print("File not loaded. Please, load a file first")
            return(text())

        curve_data = {'Age', 'Health', 'G_Avg',
                      'Failures', 'StudyTime', 'G1', 'G2', 'G3'}

        curve_attribute = input(
            "Please enter the attribute you want to use to find the best fit for G_Avg: ")

        if curve_attribute not in curve_data:
            print('Invalid command.')

        curve_order = input(
            "Please enter the order of the polynomial to be fitted: ")

        curvy = curve_fit(loaddataaverage, curve_attribute, curve_order)

        print(curvy)

        return(text())

    if operator.capitalize() == "H":

        empty = []

        if loaddataaverage == empty:
            print("File not loaded. Please, load a file first")
            return(text())

        hist_data = {'Age', 'Health', 'G_Avg',
                     'Failures', 'StudyTime', 'G1', 'G2', 'G3', 'School'}

        hist_attribute = input(
            "Please enter the attribute you want to use to find the best fit for G_Avg: ")

        if hist_attribute not in hist_data:
            print('Invalid command.')

        histy = histogram(loaddataaverage, hist_attribute)

        print(histy)

        return(text())

    if operator.capitalize() == "E":
        return

    if operator.capitalize() not in the_list:
        print("Please enter a valid command\n'L', 'S', 'C', 'H', 'E'")
        return(text())
