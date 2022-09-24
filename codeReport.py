import csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# we know some glyphs are missing, suppress warnings
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Nunito-Light', 'fonts/Nunito-Light.ttf'))

#Inputs
filepath=input("Path to .csv: ")
studentColumn=input("Enter the exact name of the column header containing students: ")
outputFilepath=input("Path to save .pdf: ")

f=open(filepath, newline='')
reader=csv.DictReader(f)

students=[]
for row in reader:
    students.append(row[studentColumn])

doc = SimpleDocTemplate(outputFilepath, pagesize=letter)
elements=[]
data=  [['Student', 'M', 'T', 'W', 'T', 'F','Comments']]

for student in students:
    data.append([f"{student}","","","","","",""])
columnWidths=[2*inch,0.8*inch,0.8*inch,0.8*inch,0.8*inch,0.8*inch,2*inch]

t=Table(data,
        colWidths=columnWidths,
        style=[('GRID',(0,0),(-1,-1),1,colors.grey),
                    ('GRID',(0,0),(-1,0),1,colors.white),
                    ('LINEABOVE',(0,0),(-1,1),1,colors.black),
                    ('BOX',(0,0),(-1,-1),1.5,colors.black),
                    ('FONTNAME',(0,0),(-1,-1),'Nunito-Light'),
                    ('BACKGROUND',(0,0),(-1,0), colors.grey),
                    ('ROUNDEDCORNERS', [2, 2, 2, 2]),
                    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
                    ('FONTSIZE',(0,1),(-1,-1),10),
                    ('ALIGNMENT',(0,0),(-1,0),'CENTER')
                    ])

elements.append(t)
doc.build(elements)
