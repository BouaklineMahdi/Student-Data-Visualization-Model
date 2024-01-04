# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Mahdi Bouakline, Kirkland Irving, Van Pham, Kathryn Gallagher"

# Update "" with your team (e.g. T102)
__team__ = "T-59"

#==========================================#
# Place your sort_students_age_bubble function after this line


def sort_students_age_bubble(data: list, order: str) -> list:
    """function takes two input parameters: the first parameter is a list of dictionaries and the second parameter is a string (“A” or “D”) to determine if the students will be sorted in ascending or descending order. The function uses the bubble sort algorithm to sort the list of students’ dictionaries by the “Age” attribute. If “Age” is a key in the dictionary, the function returns the sorted list, if not return a message '“Age” key is not present'.

    Preconditions: 'A' for ascending and 'D' for descending

    >>> sort_students_age_bubble([{"Ag":10,"School":"GP"},{"Ag":19,"School":"MS"}], 'D')
    "Age" key is not present.
    >>> sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":20,"School":"MS"}, {"Age":17,"School":"GP"}], 'D')
    [{'Age': 20, 'School': 'MS'}, {'Age': 17, 'School': 'GP'}, {'Age': 10, 'School': 'GP'}]
    >>> sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":20,"School":"MS"}, {"Age":17,"School":"GP"}], 'A')
    [{'Age': 10, 'School': 'GP'}, {'Age': 17, 'School': 'GP'}, {'Age': 20, 'School': 'MS'}]
    """

    swap = True

    while swap:
        swap = False

        for i in range(len(data) - 1):

            if 'Age' not in data[i]:
                print('"Age" key is not present.')
                return data

            elif order == 'D' and data[i]['Age'] < data[i + 1]['Age']:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
                swap = True

            elif order == 'A' and data[i]['Age'] > data[i + 1]['Age']:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
                swap = True

    return data

#==========================================#
# Place your sort_students_time_selection function after this line


def sort_students_time_selection(given_list: list, order: str):
    """ Sort the list of students’ dictionaries by the “StudyTime” attribute. If “StudyTime” is a key in the dictionary, the function returns the sorted list. If “StudyTime” is not a key in the dictionary, the function prints a message stating the key is not in the dictionary and returns the original list.

    >>> sort_students_time_selection([{"StudyTime":10.2,"School":"GP"}, {"StudyTime":19.1,"School":"MS"}], "D")
    [{"StudyTime": 19.1, "School":"MS"}, {"StudyTime":10.2, "School":"GP"}]
    >>> sort_students_time_selection([{"School":"GP"},{"School":"MS"}], "D")
    "StudyTime" key is not present
    [{"School":"GP"}, {"School":"MS"}]
    """
    first = given_list[0]
    found = False
    for key in first:
        if key == "StudyTime":
            found = True

    if not found:
        print('"StudyTime" key is not present')
        return given_list

    if order == 'A':
        for i in range(len(given_list)):
            min_idx = i
            for j in range(i + 1, len(given_list)):
                if given_list[min_idx]["StudyTime"] > given_list[j]["StudyTime"]:
                    min_idx = j
                    given_list[i], given_list[min_idx] = given_list[min_idx], given_list[i]
        return given_list
    elif order == 'D':
        for i in range(len(given_list)):
            min_idx = i
            for j in range(i + 1, len(given_list)):
                if given_list[min_idx]["StudyTime"] < given_list[j]["StudyTime"]:
                    min_idx = j
                    given_list[i], given_list[min_idx] = given_list[min_idx], given_list[i]
        return given_list

#==========================================#
# Place your sort_students_g_avg_insertion function after this line


def sort_students_g_avg_insertion(students, order):
    """
    Sorts the list of students' dictionaries by the "G_Avg" attribute using the insertion sort algorithm.
    If "G_Avg" is not a key in a dictionary, prints a message stating the key is not present and returns the original list.

    >>> sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "D")
    [{'G_Avg': 9.1, 'School': 'MS'}, {'G_Avg': 7.2, 'School': 'GP'}]
    >>> sort_students_g_avg_insertion([{"School":"GP"},{"School":"MS"}], "D")
    "G_Avg" key is not present
    [{'School': 'GP'}, {'School': 'MS'}]
    >>> sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "A")
    [{'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 9.1, 'School': 'MS'}]
    """

    for i in range(1, len(students)):
        key_item = students[i]
        last_sorted_index = i - 1
        while last_sorted_index >= 0 and key_item.get("G_Avg") and ((order == "A" and students[last_sorted_index].get("G_Avg", 0) > key_item["G_Avg"])
                                                                    or (order == "D" and students[last_sorted_index].get("G_Avg", 0) < key_item["G_Avg"])):
            students[last_sorted_index + 1] = students[last_sorted_index]
            last_sorted_index -= 1
        students[last_sorted_index + 1] = key_item

    if all("G_Avg" in student for student in students):
        return students
    else:
        print('"G_Avg" key is not present')
        return students

#==========================================#
# Place your sort_students_failures_bubble function after this line


def sort_students_failures_bubble(dict_list: list, letter: str) -> list:
    """This function returns the list inputed sorted by failures either going from lowest to highest number of failures if 'A' is enterred in the letter variable, or from highest to lowest failures if 'D' is enterred in the letter variable. If failures isn't in the dictionary list, the function tells you it's not in the list and returns the orignal list. If 'A' or 'D' isn't enterred it tells you to enter 'A' or 'D'.

    Preconditions: 'A' or 'D' must be enterred in the letter varibale, and failures must be in the dictionary list.

    >>>sort_students_failures_bubble ([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    [{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]
    >>>sort_students_failures_bubble ([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "A")
    [{'Failures': 10, 'School': 'GP'}, {'Failures': 19, 'School': 'MS'}]
    >>>sort_students_failures_bubble ([{"Fafilures":10,"School":"GP"},{"Failfures":19,"School":"MS"}], "D")
    "Failures" key is not present
    [{'Fafilures': 10, 'School': 'GP'}, {'Failfures': 19, 'School': 'MS'}]
    >>>sort_students_failures_bubble ([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "J")
    Enter either 'A' or 'D'
    """

    i = 0

    r = 0

    dictionary = dict_list[0]

    g = len(dict_list)

    for j in range(len(dict_list)):
        if dictionary.get('Failures') == None:
            r += 1

        i += 1

        dictionary = dict_list[g - i]

    if r != 0:
        print('"Failures" key is not present')
        return dict_list

    else:

        swap = True

        for i in range(len(dict_list) - 1):

            if dict_list[i]['Failures'] > dict_list[i + 1]['Failures']:

                start = dict_list[i]['Failures']

                dict_list[i]['Failures'] = dict_list[i + 1]['Failures']

                dict_list[i + 1]['Failures'] = start

                swap = True

    if letter == "A":

        return dict_list

    elif letter == "D":

        dict_list.reverse()

        return dict_list

    else:

        print("Enter either 'A' or 'D'")

#==========================================#
# Place your sort function after this line


def sort(data: list, order: str, key: str) -> list:
    """
    Sorts the list of dictionaries by the specified key in either ascending or descending order.

    >>> sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"D","Age")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
    >>> sort([{"School":"GP"},{"School":"MS"}], "D", "School")
    Cannot be sorted by "School"
    [{"School":"GP"}, {"School":"MS"}]

    """

    keys = ["Age", "StudyTime", "G_Avg", "Failures"]

    if key not in keys:
        print(f'Cannot be sorted by "{key}"')
        return data

    if order == "A":
        for i in range(len(data)):
            min_index = i

            for j in range(i + 1, len(data)):
                if data[min_index][key] > data[j][key]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]

    elif order == "D":
        for i in range(len(data)):
            max_index = i

            for j in range(i + 1, len(data)):
                if data[max_index][key] < data[j][key]:
                    max_index = j
            data[i], data[max_index] = data[max_index], data[i]

    return data


# Do NOT include a main script in your submission
