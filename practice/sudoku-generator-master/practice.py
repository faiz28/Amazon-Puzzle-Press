from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
def hello(c):
    c.setPageSize((8.5 * inch, 11 * inch)) 
    
    c.setFont("Times-Roman", 23)
    c.drawString(.65*inch, 9.7*inch, "Puzzle # 1")
    c.grid([0.65*inch, 0.87*inch, 1.09*inch, 1.31*inch,1.53*inch,1.75*inch,1.97*inch,2.19*inch,2.41*inch,2.63*inch,2.85*inch,3.07*inch,3.29*inch,3.51*inch,3.73*inch,3.95*inch,4.17*inch], [9.6*inch, 9.35*inch, 9.1*inch, 8.85*inch,8.6*inch,8.35*inch,8.1*inch,7.85*inch,7.6*inch,7.35*inch,7.1*inch,6.85*inch,6.6*inch,6.35*inch,6.1*inch,5.85*inch,5.6*inch])
    # print data
    c.setFont("Times-Roman", 18)
    x = 0.7
    y=9.4
    for i in range(16):
        for j in range(16):
            i%=9
            c.drawString(x*inch,y*inch,str(i+1))
            x+=.22
        x=.7
        y-=.25

    c.setFont("Times-Roman", 23)
    c.drawString(4.3*inch, 9.7*inch, "Puzzle # 2")
    c.grid([4.38*inch,4.6*inch,4.82*inch,5.04*inch,5.26*inch,5.48*inch,5.7*inch,5.92*inch,6.14*inch,6.36*inch,6.58*inch,6.8*inch,7.02*inch,7.24*inch,7.46*inch,7.68*inch,7.9*inch], [9.6*inch, 9.35*inch, 9.1*inch, 8.85*inch,8.6*inch,8.35*inch,8.1*inch,7.85*inch,7.6*inch,7.35*inch,7.1*inch,6.85*inch,6.6*inch,6.35*inch,6.1*inch,5.85*inch,5.6*inch])
    c.setFont("Times-Roman", 18)
    x = 4.35
    y = 9.4
    for i in range(16):
        for j in range(16):
            i%=9
            c.drawString(x*inch,y*inch,str(i+1))
            x+=.225
        x=4.35
        y-=.225

    c.setFont("Times-Roman", 23)
    c.drawString(0.65*inch, 4.6*inch, "Puzzle # 3")
    c.grid([0.65*inch, 0.875*inch, 1.1*inch, 1.325*inch,1.55*inch,1.775*inch,2*inch,2.225*inch,2.45*inch,2.675*inch,2.9*inch,3.125*inch,3.35*inch,3.575*inch,3.8*inch,4.025*inch,4.25*inch], [4.5*inch, 4.275*inch, 4.05*inch, 3.825*inch,3.6*inch,3.375*inch,3.15*inch,2.925*inch,2.7*inch,2.475*inch,2.25*inch,2.025*inch,1.8*inch,1.575*inch,1.325*inch,1.125*inch,.9*inch])
    # c.grid([4.4*inch,4.6*inch,4.8*inch,5*inch,5.2*inch,5.4*inch,5.6*inch,5.8*inch,6*inch,6.2*inch,6.4*inch,6.6*inch,6.8*inch,7*inch,7.2*inch,7.4*inch,7.6*inch], [10*inch, 9.8*inch, 9.6*inch, 9.4*inch,9.2*inch,9*inch,8.8*inch,8.6*inch,8.4*inch,8.2*inch,8*inch,7.8*inch,7.6*inch,7.4*inch,7.2*inch,7*inch,6.8*inch])

    
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()