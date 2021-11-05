from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red,white,HexColor

pdf = canvas.Canvas("./addition.pdf")

pdf.setPageSize((8.5 * inch, 11 * inch))
pdf.setFont("Helvetica-Bold", 22)
x =1.8
y = 9.45
store_y = y
pdf.drawString((x+1.3)*inch,(y+.40)*inch,'Table of content')
pdf.line((x+1.3)*inch,(y+.35)*inch,(x+3.7)*inch,(y+.35)*inch)


pdf.setFont("Times-Roman", 20)
for i in range(12):
    pdf.drawString(x*inch,y*inch,'pdf.setFont("Helvetica-Bold", 20)......10-800')
    y -= .35

pdf.setFillColor(HexColor('#cccccc'))
pdf.roundRect((x-.45)*inch,y*inch,5.8*inch,(store_y+.7-y)*inch,.2*inch, fill=True, stroke=True)
print(x)
print(y)
pdf.showPage()
pdf.save()