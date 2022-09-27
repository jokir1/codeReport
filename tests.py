import unittest
import csv

from reportlab.lib.pagesizes import inch
from reports.tables import StandardTable
from student_list.student_list import StudentList

class TestStandardTable(unittest.TestCase):
    #This is for creating test classes
    students=['Vernon Magar', 'Laurence Adragna', 'Jami Wright', 'Matthew Lewis', 'Kim Torrez',
            'Betty Kleinman', 'Frank Gomez', 'Martin Salvato', 'Andy Goodwin', 'Shannon Smyth',
            'Robert Crouch', 'George Froelich', 'James Brown', 'Michael Vandyke', 'Dorothy Oyler',
            'Karl Cavanaugh', 'Joan Walls', 'Jerry Willardson', 'Dennis Olson', 'Susan Rodriguez',
            'Catherine Robinson', 'Hillary Baker', 'Rosa Hoang', 'Gerald Lary', 'Laurie Pree']

    def test_columnWidth_function(self):
        givenInput1=StandardTable(self.students,[3,5,4])
        expectedOutput1=[3*inch,5*inch,5*inch,5*inch,5*inch,5*inch,4*inch]
        self.assertEqual(givenInput1.columnWidths(), expectedOutput1, f"Should be {expectedOutput1}")

        givenInput2=StandardTable(self.students,[1.2,0.5,0.2])
        expectedOutput2=[1.2*inch,0.5*inch,0.5*inch,0.5*inch,0.5*inch,0.5*inch,0.2*inch]
        self.assertEqual(givenInput2.columnWidths(), expectedOutput2, f"Should be {expectedOutput2}")

    def test_data_function(self):
        givenInput1=StandardTable(self.students,[3,5,4])
        expectedOutput1=[['Student', 'M', 'T', 'W', 'T', 'F','Comments'],
                        ['Vernon Magar','','','','','',''],
                        ['Laurence Adragna','','','','','',''],
                        ['Jami Wright','','','','','',''],
                        ['Matthew Lewis','','','','','',''],
                        ['Kim Torrez','','','','','',''],
                        ['Betty Kleinman','','','','','',''],
                        ['Frank Gomez','','','','','',''],
                        ['Martin Salvato','','','','','',''],
                        ['Andy Goodwin','','','','','',''],
                        ['Shannon Smyth','','','','','',''],
                        ['Robert Crouch','','','','','',''],
                        ['George Froelich','','','','','',''],
                        ['James Brown','','','','','',''],
                        ['Michael Vandyke','','','','','',''],
                        ['Dorothy Oyler','','','','','',''],
                        ['Karl Cavanaugh','','','','','',''],
                        ['Joan Walls','','','','','',''],
                        ['Jerry Willardson','','','','','',''],
                        ['Dennis Olson','','','','','',''],
                        ['Susan Rodriguez','','','','','',''],
                        ['Catherine Robinson','','','','','',''],
                        ['Hillary Baker','','','','','',''],
                        ['Rosa Hoang','','','','','',''],
                        ['Gerald Lary','','','','','',''],
                        ['Laurie Pree','','','','','','']]
        self.assertEqual(givenInput1.data(), expectedOutput1, f"Should be {expectedOutput1}")

#This is just so you can execute in the terminal with the command:
#    python3 -m unittest tests
class TestStudentList(unittest.TestCase):
    givenFilePath='csvtest.csv'
    givenColumnName='fullName'

    #This will test the method that returns a list of students.
    def test_student_list_method(self):
        givenInput=StudentList(self.givenFilePath,self.givenColumnName)
        expectedOutput=['Vernon Magar', 'Laurence Adragna', 'Jami Wright', 'Matthew Lewis', 'Kim Torrez',
                'Betty Kleinman', 'Frank Gomez', 'Martin Salvato', 'Andy Goodwin', 'Shannon Smyth',
                'Robert Crouch', 'George Froelich', 'James Brown', 'Michael Vandyke', 'Dorothy Oyler',
                'Karl Cavanaugh', 'Joan Walls', 'Jerry Willardson', 'Dennis Olson', 'Susan Rodriguez',
                'Catherine Robinson', 'Hillary Baker', 'Rosa Hoang', 'Gerald Lary', 'Laurie Pree']
        self.assertEqual(givenInput.student_list(), expectedOutput, f"Should be {expectedOutput}")

if __name__=="__main__":
    unittest.main()
