# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Van Pham"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101287770"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "59"

#==========================================#
# Place your curve_fit function after this line

import numpy as np
import matplotlib.pyplot as plt


def curve_fit(data: list, attribute: str, degree: int) ->str:
    """ The function takes three input parameters: (1) a list of dictionaries, (2) a string, and (3) an integer. The string indicates the attribute to which average grades will be compared. You can assume that only attributes with numerical values are provided. The integer represents the degree of the polynomial to be fitted to the data.
    
    >>> curve_fit([{'Health': 1 , 'Age': 10, 'G_Avg': 6}, {'Health': 2, 'Age': 17, 'G_Avg': 7}, {'Health': 3, 'Age': 20, 'G_Avg': 9}, {'Health': 2, 'Age': 17, 'G_Avg': 7.645}, {'Health': 1, 'Age': 17, 'G_Avg': 9.534}], 'Health', 2)
    'y = 10.33+-3.63x'
    >>> curve_fit([{'Health': 1 , 'Age': 10, 'G_Avg': 6}, {'Health': 2, 'Age': 17, 'G_Avg': 7}, {'Health': 3, 'Age': 20, 'G_Avg': 9}, {'Health': 2, 'Age': 17, 'G_Avg': 7.645}, {'Health': 1, 'Age': 17, 'G_Avg': 9.534}], 'Health', 0)
    'y = '
    >>> curve_fit([{'Health': 1 , 'Age': 10, 'G_Avg': 6}, {'Health': 2, 'Age': 17, 'G_Avg': 7}, {'Health': 1, 'Age': 17, 'G_Avg': 9.534}], 'Health', 9)
    'y = 8.53'
    """
    
    attribute_values = []
    for i in data:
        attribute_values = attribute_values + [i[attribute]]
    attribute_values = set(attribute_values)  
    list_average = []
    for n in attribute_values:
        G_Avg_values = []
        for m in data: #list of data[1], data[2]
            if m[attribute] == n:
                G_Avg_values = G_Avg_values + [m['G_Avg']]
                average = sum(G_Avg_values) / len(G_Avg_values)
        list_average = list_average + [average]
        
    x = list(attribute_values)
    y = list_average
    if len(x) < degree + 1:
        z = np.polyfit(x, y, len(x) - 1)
    else:
        z = np.polyfit(x, y, degree)
        
    p = np.poly1d(z)
    equation = ""
    for i in range(len(p)):
        if i == 0:
            equation += str(round(p[i], 2))
        elif i == 1:
            equation += '+' + str(round(p[i], 2)) + 'x'
        else:
            equation += '+' + str(round(p[i], 2)) + 'x^' + str(i)
    return 'y = ' + equation

# Do NOT include a main script in your submission
