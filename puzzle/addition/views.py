from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def make_pdf(c,c_sol,up_min,up_max,lower_min,lower_max,puzzle,page):
    c.setPageSize((8.5 * inch, 11 * inch)) 
    c_sol.setPageSize((8.5 * inch, 11 * inch))
    digit_min= min(int(up_min),int(lower_min))
    digit_max= max(int(up_max),int(lower_max))
    a = '%s %s %s %s'%(up_min,up_max,lower_min,lower_max)
    print(a)
    c.setFont("Times-Roman", 23)
    c.rect(1*inch,9.8*inch,2*inch,.7*inch, fill=0)
    c.showPage()
    c.save()


# Create your views here.
def addition(request):
    c_pdf = canvas.Canvas("./media/addition/addition.pdf")
    c_pdf_sol = canvas.Canvas("./media/addition/solution.pdf")

    if request.method == 'POST':
        up_min = request.POST.get('up_min')
        up_max = request.POST.get('up_max')
        lower_min = request.POST.get('low_min')
        lower_max = request.POST.get('low_max')
        puzzle = request.POST.get('puzzle')
        page = request.POST.get('page')

        make_pdf(c_pdf,c_pdf_sol,up_min,up_max,lower_min,lower_max,puzzle,page)


    
    return render(request,'addition.html')