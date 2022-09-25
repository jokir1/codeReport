from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# we know some glyphs are missing, suppress warnings
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Nunito-Light', 'fonts/Nunito-Light.ttf'))

class StandardTable:

    def __init__(self,students,col_widths=[2,0.8,2]):
        self.students = students
        self.col_widths=col_widths
        if len(col_widths)!=3:
            raise ValueError('Your column widths need to be a list of three widths for each type of column -> [student,days,comments]')

    def columnWidths(self):
        W=[self.col_widths[0]*inch]
        W.extend([self.col_widths[1]*inch]*5)
        W.extend([self.col_widths[2]*inch])
        return W

    def data(self):
        header=[['Student', 'M', 'T', 'W', 'T', 'F','Comments']]
        data=header
        for student in self.students:
            data.append([f"{student}","","","","","",""])
        return data

    def createTable(self):
        t=Table(self.data(),
                colWidths=self.columnWidths(),
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
        return t

    def createPDF(self,outputFilepath):
        doc = SimpleDocTemplate(outputFilepath, pagesize=letter)
        elements=[]

        t=self.createTable()

        elements.append(t)
        doc.build(elements)
