import unittest
import names

from reportlab.lib.pagesizes import inch
from reports.tables import StandardTable

class TestStandardTable(unittest.TestCase):
    #This is for creating test classes
    def students(self,class_size):
        students=[]
        while len(students)<class_size:
            students.append(names.get_full_name())

    def test_columnWidth_function(self):
        givenInput1=StandardTable(self.students(25),[3,5,4])
        expectedOutput1=[3*inch,5*inch,5*inch,5*inch,5*inch,5*inch,4*inch]
        self.assertEqual(givenInput1.columnWidths(), expectedOutput1, f"Should be {expectedOutput1}")

        givenInput2=StandardTable(self.students(29),[1.2,0.5,0.2])
        expectedOutput2=[1.2*inch,0.5*inch,0.5*inch,0.5*inch,0.5*inch,0.5*inch,0.2*inch]
        self.assertEqual(givenInput2.columnWidths(), expectedOutput2, f"Should be {expectedOutput2}")

if __name__=="__main__":
    unittest.main()
