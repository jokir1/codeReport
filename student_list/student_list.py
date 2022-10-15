import csv

# This sub classed DictReader doesn't skip blank rows
class NoSkipDictReader(csv.DictReader):
    def next(self):
        if self.line_num == 0:
            # Used only for its side effect.
            self.fieldnames
        row = self.reader.next()
        self.line_num = self.reader.line_num

        d = dict(zip(self.fieldnames, row))
        lf = len(self.fieldnames)
        lr = len(row)
        if lf < lr:
            d[self.restkey] = row[lf:]
        elif lf > lr:
            for key in self.fieldnames[lr:]:
                d[key] = self.restval
        return d

class StudentList:
    def __init__(self,filepath,col_name):
        self.filepath=filepath
        self.col_name=col_name

    def __str__(self):
        return f"filepath:{self.filepath}, col_name:{self.col_name}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: \'{self.filepath}\', \'{self.col_name}\'>"

    def student_list(self):
        f=open(self.filepath, newline='')
        reader=csv.DictReader(f)
        student_list=[row[self.col_name] for row in reader]
        return student_list

    def split_by_course(self):
        f=open(self.filepath, newline='')
        reader=csv.reader(f)
        index=0
        courses=[]
        course=[]
        for row in reader:
            if self.col_name in row:
                index=row.index(self.col_name)
            elif all(s=='' or s.isspace() for s in row):
                courses.append(course)
                course=[]
            else:
                course.append(row[index])
        course_cleaned=[course for course in courses if course != []]
        return courses_cleaned
