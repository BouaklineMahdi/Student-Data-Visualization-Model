# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Mahdi Bouakline"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101257788"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-59"

#==========================================#
# Place your script for your batch_UI after this line

import load_data
import sort
import curve_fit
import histogram

data = ""

for line in open(input("Please enter the name of the file where your commands are stored: ")):
    commands = line.split(";")
    if commands[0].lower() == "l":
        if len(commands) < 4:
            print("Error: not enough parameters for load command")
            continue
        if commands[2] == "School":
            data = load_data.add_average(load_data.load_data(
                commands[1], (commands[2], commands[3].strip())))
        elif commands[2] == "StudyTime":
            data = load_data.add_average(load_data.load_data(
                commands[1], (commands[2], float(commands[3]))))
        else:
            data = load_data.add_average(load_data.load_data(
                commands[1], (commands[2], int(commands[3]))))
    elif isinstance(data, str):
        print("File is not loaded. Please, load a file first.")
    elif commands[0].lower() == "s":
        data = sort.sort(data, commands[2], commands[1])
        if commands[3].strip() != "N":
            print(data)
    elif commands[0].lower() == "c":
        print(curve_fit.curve_fit(data, commands[1], int(commands[2])))
    elif commands[0].lower() == "h":
        histogram.histogram(data, commands[1])






