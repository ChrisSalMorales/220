"""
Christopher Morales
lab8.py

Problem: To develop a python program that uses numeric data from a text file.

Certification of Authenticity:
I certify that this assignment is my own work.
"""
def weighted_average(in_file_name, out_file_name):
    open_infile = open(in_file_name, "r")
    open_outfile = open(out_file_name, "w+")
    for line in open_infile:
        split_line = line.split(": ")
        grade = (split_line[1])
        grades = grade.split()
        total_of_grade = [str(integer) for integer in grades]
        string = " ".join(total_of_grade)
        print("Name: " + str(split_line[0]))
        print(grade)
        print(string)
        total = sum(grade)
        print(total)
