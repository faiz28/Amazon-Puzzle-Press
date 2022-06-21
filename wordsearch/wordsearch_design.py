from os import listdir
from os.path import isfile, join
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


file_source = './media/file'
files = [f for f in listdir(file_source) if isfile(join(file_source, f))]

class design:
    def make_pdf():
        pdf  =  canvas.Canvas("./media/wordsearch/inner_design.pdf")
        pdf.setPageSize((8.5 * inch, 11 * inch))
        
        for file in files:
            print(file)
        pdf.showPage()
        pdf.save()
        print("Hello here")