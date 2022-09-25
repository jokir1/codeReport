import csv
from reports.tables import StandardTable

#Inputs
filepath=input("Path to .csv: ")
studentColumn=input("Enter the exact name of the column header containing students: ")
outputFilepath=input("Path to save .pdf: ")

f=open(filepath, newline='')
reader=csv.DictReader(f)

students=[]
for row in reader:
    students.append(row[studentColumn])

s=StandardTable(students)

s.createPDF(outputFilepath)
