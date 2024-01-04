# ECOR 1042 Lab 4 - team submission

# import check module here
import check

# import load_data module here
import load_data
from load_data import add_average
from load_data import student_school_list
from load_data import student_age_list
from load_data import student_health_list
from load_data import student_failures_list

# Update "" with your the name of the active members of the team
__author__ = "Mahdi Bouakline, Kirkland Irving, Van Pham, Kathryn Gallagher"

# Update "101257788" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-59"

#==========================================#


# Place test_return_list function here


def test_return_list():
    # Complete the function with your test cases

    # test that student_school_list returns a list (3 different test cases required

    for i in range(3):

        num = 1

        if num == 1:
            school = str("GP")

        elif num == 2:
            school = str("MB")

        else:
            school = str("CF")

        y = (load_data.student_school_list('student-test.csv', int(num)))

        num += 1

        j = isinstance(y, list)

        check.equal(j, True)

    # test that student_age_list returns a list (3 different test cases required)

    for i in range(3):

        num = 1

        z = (load_data.student_age_list('student-test.csv', (int(num) + 14)))

        num += 1

        l = isinstance(z, list)

        check.equal(l, True)

    # test that student_health_list returns a list (3 different test cases required)

    for i in range(3):

        num = 1

        x = (load_data.student_health_list('student-test.csv', int(num)))

        num += 1

        k = isinstance(x, list)

        check.equal(k, True)

    # test that student_failures_list returns a list (3 different test cases required)

    for i in range(3):

        num = 1

        a = (load_data.student_failures_list(
            'student-test.csv', (int(num) - 1)))

        num += 1

        m = isinstance(a, list)

        check.equal(m, True)

    # test that load_data returns a list (6 different test cases required)
    for g in range(6):

        var = 1

        if var == 1:
            funct = ('All', -1)

        if var == 2:
            funct = ('Failures', 0)

        if var == 3:
            funct = ('Health', 2)

        if var == 4:
            funct = ('Absences', 1)

        if var == 5:
            funct = ('Age', 16)

        if var == 6:
            funct = ('School', "GP")

        h = (load_data.load_data('student-test.csv', (funct)))

        g += 1
        var += 1

        e = isinstance(h, list)

        check.equal(e, True)

    # test that add_average returns a list (3 different test cases required)

    for i in range(3):

        num = 1

        if num == 1:

            stud_list = [{'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
                          'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}]

        elif num == 2:

            stud_list = [{'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
                          'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 3, 'G2': 5, 'G3': 6}]

        else:

            stud_list = [{'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
                          'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 6, 'G2': 6, 'G3': 6}]

        b = (load_data.add_average(stud_list))

        num += 1

        n = isinstance(b, list)

        check.equal(n, True)

    check.summary()

# Place test_return_list_correct_lenght function here


def test_return_list_correct_lenght():
    """ Test that all six functions in the load data module return a list of the correct length.
    >>> add_average([])
    0
    >>> load_data("student-test.csv", ("School", "A"))
    0
    >>> student_age_list("student-test.csv", 18)
    4
    """
    # Complete the function with your test cases

    # test that student_school_list returns a list with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_school_list(
        'student-test.csv', 'GP')), 3)
    check.equal(len(load_data.student_school_list(
        'student-test.csv', 'G')), 0)
    check.equal(len(load_data.student_school_list(
        'student-test.csv', 'MS')), 4)

    # test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_age_list('student-test.csv', 19)), 0)
    check.equal(len(load_data.student_age_list('student-test.csv', 18)), 4)
    check.equal(len(load_data.student_age_list('student-test.csv', 17)), 6)

    # test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_health_list('student-test.csv', 3)), 8)
    check.equal(len(load_data.student_health_list('student-test.csv', 5)), 3)
    check.equal(len(load_data.student_health_list('student-test.csv', 1)), 1)

    # test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    check.equal(
        len(load_data.student_failures_list('student-test.csv', 0)), 66)
    check.equal(
        len(load_data.student_failures_list('student-test.csv', 1)), 6)
    check.equal(
        len(load_data.student_failures_list('student-test.csv', 4)), 0)

    # test that load_data returns a list with the correct lenght (6 different test cases required)
    check.equal(len(load_data.load_data(
        'student-test.csv', ("School", "A"))), 0)
    check.equal(len(load_data.load_data(
        'student-test.csv', ("School", "GP"))), 3)
    check.equal(len(load_data.load_data(
        'student-test.csv', ("Age", "18"))), 4)
    check.equal(len(load_data.load_data(
        'student-test.csv', ("Failures", "0"))), 11)
    check.equal(len(load_data.load_data(
        'student-test.csv', ("Health", "1"))), 1)
    check.equal(len(load_data.load_data(
        'student-test.csv', ("Absences", "12"))), 0)

    # test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(load_data.add_average(
        load_data.load_data("student-test.csv", ("Age", 18)))), 4)
    check.equal(len(load_data.add_average(
        load_data.load_data("student-test.csv", ("School", "GP")))), 3)
    check.equal(len(load_data.add_average(
        load_data.load_data("student-test.csv", ("Failures", 2)))), 2)

    check.summary()

# Place test_return_correct_dict_inside_list function here


def test_return_correct_dict_inside_list():
    # Complete the function with your test cases

    # test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    outcome_school1 = student_school_list("student-test.csv", "GP")[0]
    expexted_school_dict1 = {'Age': '18', 'StudyTime': '2', 'Failures': '0',
                             'Health': '3', 'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}
    check.equal(outcome_school1, expexted_school_dict1, "")

    outcome_school2 = student_school_list("student-test.csv", "MS")[3]
    expexted_school_dict2 = {'Age': '18', 'StudyTime': '3', 'Failures': '0',
                             'Health': '5', 'Absences': '2', 'G1': '9', 'G2': '8', 'G3': '8'}
    check.equal(outcome_school2, expexted_school_dict2, "")

    outcome_school3 = student_school_list("student-test.csv", "MF")
    expexted_school_dict3 = []
    check.equal(outcome_school3, expexted_school_dict3, "")

    # test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    outcome_age1 = student_age_list("student-test.csv", 0)
    expected_age_dict1 = []
    check.equal(outcome_age1, expected_age_dict1, "")

    outcome_age2 = student_age_list("student-test.csv", 17)[-1]
    expected_age_dict2 = {'School': 'MS', 'StudyTime': 3, 'Failures': 0,
                          'Health': 4, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}
    check.equal(outcome_age2, expected_age_dict2, "")

    outcome_age3 = student_age_list("student-test.csv", 17)[-3]
    expected_age_dict3 = {'School': 'MS', 'StudyTime': 1, 'Failures': 0,
                          'Health': 4, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10}
    check.equal(outcome_age3, expected_age_dict3, "")

    # test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    outcome_health1 = student_health_list("student-test.csv", 1)[0]
    expected_health_dict1 = {'School': 'MS', 'Age': 17, 'StudyTime': 3,
                             'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}
    check.equal(outcome_health1, expected_health_dict1, "")

    outcome_health2 = student_health_list("student-test.csv", 3)[-1]
    expected_health_dict2 = {'School': 'BD', 'Age': 18, 'StudyTime': 3,
                             'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12}
    check.equal(outcome_health2, expected_health_dict2, "")

    outcome_health3 = student_health_list("student-test.csv", 0)
    expected_health_dict3 = []
    check.equal(outcome_health3, expected_health_dict3, "")

    # test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    outcome_failures1 = student_failures_list("student-test.csv", 2)[0]
    expected_failures_dict1 = {'School': 'CF', 'Age': 15, 'StudyTime': 5.0,
                               'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}
    check.equal(outcome_failures1, expected_failures_dict1, "")

    outcome_failures2 = student_failures_list("student-test.csv", 9)
    expected_failures_dict2 = []
    check.equal(outcome_failures2, expected_failures_dict2, "")

    outcome_failures3 = student_failures_list("student-test.csv", 0)[1]
    expected_failures_dict3 = {'School': 'GP', 'Age': 18, 'StudyTime': 2.0,
                               'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}
    check.equal(outcome_failures3, expected_failures_dict3, "")

    # test that load_data returns a correct dictionary inside the list (6 different test cases required)
    outcome_load_data1 = load_data.load_data(
        'student-test.csv', ('School', 'GP'))[-1]
    expected_load_data_dict1 = {'Age': 15, 'StudyTime': 2.0, 'Failures': 3,
                                'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}
    check.equal(outcome_load_data1, expected_load_data_dict1, "")

    outcome_load_data2 = load_data.load_data(
        'student-test.csv', ('hello', 'I dont care'))
    expected_load_data_dict2 = 'Invalid Value'
    check.equal(outcome_load_data2, expected_load_data_dict2, "")

    outcome_load_data3 = load_data.load_data(
        'student-test.csv', ('Health', 4))[-2]
    expected_load_data_dict3 = {'School': 'MS', 'Age': 17, 'StudyTime': 1.0,
                                'Failures': 0, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10}
    check.equal(outcome_load_data3, expected_load_data_dict3, "")

    outcome_load_data4 = load_data.load_data(
        'student-test.csv', ('Age', 18))[0]
    expected_load_data_dict4 = {'School': 'GP', 'StudyTime': 2.0,
                                'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}
    check.equal(outcome_load_data4, expected_load_data_dict4, "")

    outcome_load_data5 = load_data.load_data('student-test.csv', {'School': 'GP', 'Age': 17, 'StudyTime': 3.0,
                                                                  'Failures': 0, 'Health': 1, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9})
    expected_load_data_dict5 = {'School': 'GP', 'Age': 17, 'StudyTime': 3.0,
                                'Failures': 0, 'Health': 1, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9, 'G_Ave': 10.0}
    check.equal(outcome_load_data5, expected_load_data_dict5, "")

    outcome_load_data6 = load_data.load_data(
        'student-test.csv', ('Failures', 0))[-2]
    expected_load_data_dict6 = {'School': 'MS', 'Age': 17, 'StudyTime': 3.0,
                                'Health': 4, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}
    check.equal(outcome_load_data6, expected_load_data_dict6, "")

    # test that add_average returns a lcorrect dictionary inside the list  (3 different test cases required)
    outcome_add_average1 = add_average(
        [{'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])
    expected_add_average1 = [{'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0,
                              'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8, 'G_Avg': 8.33}]
    check.equal(outcome_add_average1, expected_add_average1, "")

    outcome_add_average2 = add_average(
        [{'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Failures': 2, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}])
    expected_add_average2 = [{'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Failures': 2,
                              'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0, 'G_Avg': 4.33}]
    check.equal(outcome_add_average2, expected_add_average2, "")

    outcome_add_average3 = add_average(
        [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])
    expected_add_average3 = [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0,
                              'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}]
    check.equal(outcome_add_average3, expected_add_average3, "")

    check.summary()

# Place test_add_average function here


def test_add_average():
    # Test case 1: School is not a key of the dictionary
    data = load_data.load_data("student-test.csv", ("Age", 18))
    updated_data = load_data.add_average(data)

    # Check if list size remains the same
    check.equal(len(updated_data), len(data))

    # Check if number of keys increase by 1
    check.equal(len(updated_data[0]), len(data[0]))

    for i, student in enumerate(data):
        grades = [student['G1'], student['G2'], student['G3']]
        # Ignore None values
        grades = [grade for grade in grades if grade is not None]
        avg_grade = round(sum(grades) / len(grades),
                          2) if len(grades) > 0 else None
        check.equal(float(updated_data[i]["G_Avg"]), avg_grade)

    # Test case 2: Health is not a key of the dictionary
    data = load_data.load_data("student-test.csv", ("School", "GP"))
    updated_data = load_data.add_average(data)

    # Check if list size remains the same
    check.equal(len(updated_data), len(data))

    # Check if number of keys increase by 1
    check.equal(len(updated_data[0]), len(data[0]))

    for i, student in enumerate(data):
        grades = [student['G1'], student['G2'], student['G3']]
        # Ignore None values
        grades = [grade for grade in grades if grade is not None]
        avg_grade = round(sum(grades) / len(grades),
                          2) if len(grades) > 0 else None
        check.equal(float(updated_data[i]["G_Avg"]), avg_grade)

    # Test case 3: Age is not a key of the dictionary
    data = load_data.load_data("student-test.csv", ("Failures", 2))
    updated_data = load_data.add_average(data)

    # Check if list size remains the same
    check.equal(len(updated_data), len(data))

    # Check if number of keys increase by 1
    check.equal(len(updated_data[0]), len(data[0]))

    for i, student in enumerate(data):
        grades = [student['G1'], student['G2'], student['G3']]
        # Ignore None values
        grades = [grade for grade in grades if grade is not None]
        avg_grade = round(sum(grades) / len(grades),
                          2) if len(grades) > 0 else None
        check.equal(float(updated_data[i]["G_Avg"]), avg_grade)

    # Test case 4: Failures is not a key of the dictionary
    data = load_data.load_data("student-test.csv", ("Health", "1"))
    updated_data = load_data.add_average(data)
    # Check if list size remains the same
    check.equal(len(updated_data), len(data))
    # Check if number of keys increase by 1
    check.equal(len(updated_data[0]), len(data[0]))
    sum_grades = 0
    for student in data:
        sum_grades += int(student["G1"]) + \
            int(student["G2"]) + int(student["G3"])
    avg_grade = round(sum_grades / (len(data) * 3), 2)
    # Check if G_Avg is properly calculated
    check.equal(float(updated_data[0]["G_Avg"]), avg_grade)

    check.summary()

# Do NOT include a main script in your submission
