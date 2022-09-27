import csv

class StudentList:
    def __init__(self,filepath,col_name):
        self.filepath=filepath
        self.col_name=col_name

    def student_list(self):
        f=open(self.filepath, newline='')
        reader=csv.DictReader(f)
        student_list=[]
        for row in reader:
            student_list.append(row[self.col_name])
        return student_list
