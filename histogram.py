# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Kathryn Gallagher"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101272689"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-59"

#==========================================#
# Place your histogram function after this line

import matplotlib.pyplot as plt


def histogram(list1: list[dict], attribute_plotted: str):
    """  Plot and show histogram based on number of students with each attribute.

    >>> histogram( [{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "School")
    <<histogram displayed>>
    1 student for GP and 1 for MS

    >>> histogram( [{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}, {"School":"MS"}], "Age")
    <<histogram displayed>>
    1 student for 10 and 1 for 19
    >>>

    """
    attribute_list = []
    for dict in list1:
        for key in dict:
            if key == attribute_plotted:
                dict1 = {}
                dict1 = dict[key]
                attribute_list.append(dict1)

    x = []
    for str in attribute_list:
        if str not in x:
            x.append(str)

    y = []
    for str in x:
        n = 0
        n = attribute_list.count(str)
        y.append(n)

    if len(x) >= 2 and isinstance(x[1], float):
        fig1 = plt.figure
        plt.xlabel(attribute_plotted)
        plt.ylabel("Number of Students")
        plt.title("Number of Students per Attribute")
        bins = [0, 3, 6, 9, 12, 15, 18, float('inf')]
        plt.hist(attribute_list, bins)
        plt.show()
    else:
        fig1 = plt.figure
        plt.xlabel(attribute_plotted)
        plt.ylabel("Number of Students")
        plt.title("Number of Students per Attribute")
        plt.bar(x, y)
        plt.show()


# Do NOT include a main script in your submission
