from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# we know some glyphs are missing, suppress warnings
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Nunito-Light', 'Nunito-Light.ttf'))


f=open('test.html','w')

studentList=['Josh','Randi','Loosey']

trs=""
for student in studentList:

    trs+=f"""<tr>
      <td>{student}</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    """

html=f"""

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <table>
        <tr>
            <th>Student</th>
            <th>M</th>
            <th>T</th>
            <th>W</th>
            <th>T</th>
            <th>F</th>
        </tr>
        {trs}
    </table>
  </body>
</html>
"""

f.write(html)
f.close()

doc = SimpleDocTemplate("test.pdf", pagesize=letter)
elements=[]
data=  [['Student', 'M', 'T', 'W', 'T', 'F']]

for student in studentList:
    data.append([f"{student}","","","","",""])

t=Table(data,style=[('GRID',(0,0),(-1,-1),1,colors.grey),
                    ('GRID',(0,0),(-1,0),1,colors.white),
                    ('LINEABOVE',(0,0),(-1,1),1,colors.black),
                    ('BOX',(0,0),(-1,-1),1.5,colors.black),
                    ('FONTNAME',(0,0),(-1,-1),'Nunito-Light'),
                    ('BACKGROUND',(0,0),(-1,0), colors.grey),
                    ('ROUNDEDCORNERS', [2, 2, 2, 2]),
                    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
                    ])

elements.append(t)
doc.build(elements)
