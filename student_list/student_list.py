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

    def student_list(self):
        f=open(self.filepath, newline='')
        reader=csv.DictReader(f)
        student_list=[]
        for row in reader:
            student_list.append(row[self.col_name])
        return student_list

    def split_by_course(self,delimiter=None):
        pass
