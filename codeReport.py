import csv
from reports.tables import StandardTable
from student_list.student_list import StudentList

#Inputs
filepath=input("Path to .csv: ")
studentColumn=input("Enter the exact name of the column header containing students: ")
outputFilepath=input("Path to save .pdf: ")

students=StudentList(filepath,studentColumn).student_list()
s=StandardTable(students)

s.createPDF(outputFilepath)
