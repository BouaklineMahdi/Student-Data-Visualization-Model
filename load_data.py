# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Mahdi Bouakline, Kirkland Irving, Van Pham, Kathryn Gallagher"

# Update "" with your team (e.g. T102)
__team__ = "T-59"

#==========================================#
# Place your student_school_list function after this line


def student_school_list(file_name: str, school_name: str) -> list[dict]:
    """ Return a list of students (stored as a dictionary) that attended the school provided as the input parameters

    >>> student_school_list('student-mat.csv', 'CF')
    [{'Age': '16', 'StudyTime': '2', 'Failures': '1', 'Health': '5', 'Absences': '4', 'G1': '10', 'G2': '12', 'G3': '12'}, ...]

    >>> student_school_list('student-mat.csv', '')
    []
    """
    student_list = []
    with open(file_name, "r") as f:
        header = f.readline().strip().split(',')
        for line in f:
            line = line.strip().split(',')
            if line[0] == school_name:
                student = dict(zip(header, line))
                del student['School']
                student_list.append(student)
    return student_list


#==========================================#
# Place your student_health_list function after this line
def student_health_list(filename: str, health_value: int) -> list:
    """Return a directory (dict), of each student who contains the health_value enterred.

    Preconditions: the health_value enterred has to be a 1-5 int or it will retrun an empty list.

    >>>student_health_list('student-mat.csv', 2)
    [ {'School': 'MS', 'Age': 20, 'StudyTime': 2, 'Failures': 1, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7}, {another student with the same health_value}, ...]
    >>>student_heelth_list('student-mat.csv', 0)
    []
    >>>student_health_list('student-mat.csv, 1)
    [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, {another student with the same health_value}, ...]
    ...
    """
    infile = open(filename, "r")

    student_list = []

    first_line = True

    for line in infile:

        line_list = line.strip().split(',')

        if first_line == True:
            first_line = False
            continue

        if line_list[4] == str(health_value):
            student = {'School': line_list[0], 'Age': int(line_list[1]), 'StudyTime': int(line_list[2]), 'Failures': int(
                line_list[3]), 'Absences': int(line_list[5]), 'G1': int(line_list[6]), 'G2': int(line_list[7]), 'G3': int(line_list[8])}

            student_list.append(student)

    infile.close()
    return student_list

#==========================================#
# Place your student_age_list function after this line


def student_age_list(filename: str, age: int) -> list:
    """The function returns a list of students with the same age.
    Precondition: age>0
    >>> student_age_list('student-mat.csv', 22)
    [{'School': 'BD', 'StudyTime': 1, 'Failures': 3, 'Health': 1, 'Absences': 16, 'G1': 6, 'G2': 8, 'G3': 8}]
    >>> student_age_list('student-mat.csv', 21)
    [{'School': 'MS', 'StudyTime': 1, 'Failures': 3, 'Health': 3, 'Absences': 3, 'G1': 10, 'G2': 8, 'G3': 7}]
    """
    infile = open(filename, "r")  # open file
    age_list = []
    first = True
    for line in infile:  # skip the first line
        if (first):
            first = False
            continue
        # remove /n and convert dictionary to list
        line_list = line.strip().split(",")
        student_list = {"School": line_list[0], "StudyTime": int(line_list[2]), "Failures": int(line_list[3]), "Health": int(
            line_list[4]), "Absences": int(line_list[5]), "G1": int(line_list[6]), "G2": int(line_list[7]), "G3": int(line_list[8])}

        # if age is same as input value, add the student's info to the list
        if age == int(line_list[1]):
            age_list = age_list + [student_list]
    infile.close()
    return age_list

#==========================================#
# Place your student_failures_list function after this line


def student_failures_list(filename: str, num_of_failures: int) -> dict:
    """
    Return a list of the students with the same number of failures as the inputted value

    >>> student_failures_list('student-mat.csv', 3)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}...]
    >>> student_failures_list('student-mat.csv', 2)
    [{'School': 'GP', 'Age': 16, 'StudyTime': 1.0, 'Health': 5, 'Absences': 14, 'G1': 6, 'G2': 9, 'G3': 8}...]
    >>> student_failures_list('student-mat.csv', 1)
    [{'School': 'GP', 'Age': 16, 'StudyTime': 2.0, 'Health': 3, 'Absences': 25, 'G1': 7, 'G2': 10, 'G3': 11}...]
    """
    students = []
    with open(filename, 'r') as file:

        header = file.readline().strip().split(',')
        header.remove('Failures')

        for line in file:

            line = line.strip().split(',')

            if line[3] == str(num_of_failures):
                student = {}
                line.remove(line[3])

                for i in range(len(header)):
                    if i == 0:
                        student[header[i]] = line[i]
                    elif i == 2:
                        student[header[i]] = float(line[i])
                    else:
                        student[header[i]] = int(line[i])
                        students.append(student)
        return students


#==========================================#
# Place your load_data function after this line

def load_data(file_name: str, filter_data: tuple) -> list[dict]:
    """
    Return 

    >>> load_data('student-mat.csv', ('Age', 15))
    [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}...]
    >>> load_data('student-mat.csv', ('School', 'GP'))
    [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}...]
    >>> load_data('student-mat.csv', ('StudyTime', 55.0))
    Invalid Value
    []

    """
    valid_filters = {'School', 'Age', 'Health', 'Failures', 'All'}
    valid_attributes = {'StudyTime', 'Absences', 'G1', 'G2', 'G3'}
    students = []

    if type(filter_data) == dict:
        ave = (int(filter_data['G1']) +
               int(filter_data['G1']) + int(filter_data['G1'])) / 3.0
        filter_data['G_Ave'] = round(ave, 2)
        return filter_data

    elif type(filter_data) == tuple:

        if filter_data[0] not in valid_filters:
            return 'Invalid Value'

        with open(file_name, 'r') as file:
            header = file.readline().strip().split(',')

            for line in file:
                values = line.strip().split(',')
                student = {}

                if filter_data[0] == 'All' or values[header.index(filter_data[0])] == str(filter_data[1]):
                    for i in range(len(header)):
                        if header[i] != filter_data[0]:
                            if header[i] == 'Age' or header[i] == 'Health' or header[i] == 'Failures' or header[i] == 'Absences' or header[i] == 'G1' or header[i] == 'G2' or header[i] == 'G3':
                                student[header[i]] = int(values[i])
                            elif header[i] == 'School':
                                student[header[i]] = values[i]
                            elif header[i] == 'StudyTime':
                                student[header[i]] = float(values[i])
                    students.append(student)

        return students


#==========================================#
# Place your add_average function after this line

def add_average(student_list: list) -> list:
    """
    Computes the average of the grades (G1, G2 and G3) for each student in the given list
    of dictionaries and adds it as a new key-value pair with the key 'G_Avg'

    >>> add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7,              'Failures': 1, 'Health': 3, 'Absences': 7,              'G1': 5, 'G2': 6, 'G3': 6}])
    [{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}]
    >>> add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7,              'Failures': 1, 'Health': 3, 'Absences': 7,              'G1': 3, 'G2': 5, 'G3': 6}])
    [{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 3, 'G2': 5, 'G3': 6, 'G_Avg': 4.67}]
    >>> add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7,              'Failures': 1, 'Health': 3, 'Absences': 7,              'G1': 6, 'G2': 6, 'G3': 6}])
    [{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 6, 'G2': 6, 'G3': 6, 'G_Avg': 6.0}]
    """

    for student in student_list:
        grades = [student['G1'], student['G2'], student['G3']]
        # Ignore None values
        grades = [grade for grade in grades if grade is not None]
        average = round(sum(grades) / len(grades),
                        2) if len(grades) > 0 else None
        # Add a new key-value pair to the dictionary
        student['G_Avg'] = average
    return student_list



