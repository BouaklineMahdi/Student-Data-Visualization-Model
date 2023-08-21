School board data sorting program
11/04/2023
Python 3.11.1
Mahdi Bouakline 101257788 mahdibouakline@cmail.carleton.ca

Description: Our software is software that can manipulate student data from a school board. Data can be represented in many different ways and sorted with the functions we've created. Some examples include students attending a specific school, students who failed a certain number of times and even the health of the student. Our software is also able to extrapolate additional information from the given data. This includes: Calculating the average, arranging the standard in decreasing or increasing order and even plotting the data. The created modules put all of this together by creating one module with access to all the created functions. Our software is a data visualizer.


Dependencies:
-Python
-matplotlib.pyplot
-numpy

Installation: For the program to run, you need to complete these steps...(It is assumed that the user has dwonloaded ALL required files)
-Create a new folder, with an appropriate/easy to remember title
-Transfer following functions into the folder:
	-text_UI.py
	-bacht_UI.py
	-curve_fit.py
	-histogram.py
	-sort.py
	-load_data.py
-Once you have assured all appropriate files are in the folder, the software should be good to go.

Usage: A video has been created to explain to users how to start and correctly use the program. There are also tips in these videos to help a new user understand the program. 


Credits:
-Lab 2:
	-Contract: Team effort to brainstorm, typed up by Kathryn Gallagher.
-Lab 3:
	-Kathryn Gallagher: student_school_list function
	-Kirkland Irving: student_health_list function
	-Van Pham: student_age_list function, load_data function
	-Mahdi Bouakline: student_failures_list function, add_average function
-Lab 4:
	-Kirkland Irving: test1 function
	-Kathryn Gallagher:test2 function
	-Van Pham: test3 function, test_load_data function
	-Mahdi Bouakline: test4 function, test_load_data function
-Lab 5:
	-Van Pham: sort_students_age_bubble function
	-Kathryn Gallagher: sort_students_time_selection function
	-Mahdi Bouakline: sort_students_g_avg_insertion function, sort function
	-Kirkland Irving: sort_students_failures_bubble function
-Lab 6:
	-Van Pham: curve_fit function
	-Kathryn Gallagher: histogram function
	-Kirkland Irving: text_UI module, video demo
	-Mahdi Bouakline: batcht_UI module, README file, video demo

License:
MIT License

Copyright (c) [2023] [Mahdi Bouakline]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
