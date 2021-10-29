from django.shortcuts import render
from random import randint
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red,white,HexColor


def make_pdf(pdf,pdf_sol,min_val,max_val,puzzle_per_page,day):
    pdf.setPageSize((8.5 * inch, 11 * inch)) 
    pdf_sol.setPageSize((8.5 * inch, 11 * inch))
   
    pdf.setFont("Times-Roman", 23)
    pdf.setFillColor(HexColor('#131921'))
    pdf.roundRect(.8*inch,9.9*inch,2.2*inch,.68*inch,.2*inch, fill=True, stroke=False)
 
    
    puzzle_per_page = int(puzzle_per_page)
    pdf.setFillColor(HexColor('#ffffff'))
    s = "Day %d"%day
    day += 1
    print(day)
    pdf.drawString(1*inch,10.3*inch,s)
    
    pdf.setFillColor(black)
    pdf.setFont("Times-Roman", 20)
    pdf.drawString(3.12*inch,9.95*inch, 'Name :')
    pdf.line(3.95*inch,9.95*inch, 5.92*inch,9.95*inch)
    pdf.circle(6.4*inch,10.18*inch, .36*inch)
    pdf.setFont("Times-Roman", 13)
    pdf.drawString(6.18*inch,10.3*inch, 'Score  ')
    pdf.setFont("Times-Roman", 13)
    pdf.drawString(6.5*inch,10*inch, '/60')
    pdf.roundRect(6.9*inch,9.9*inch,1*inch,.6*inch,.2*inch, fill=False, stroke=True)
    pdf.line(6.9*inch,10.25*inch,7.9*inch,10.25*inch)
    pdf.drawString(7.2*inch,10.33*inch, 'Time')

    x=1.5
    y=9.5
    pdf.setFont("Helvetica-Bold", 17)
    if puzzle_per_page>=60:
        for i in range(10):
            for j in range(6):
                upper_digit = randint(min_val,max_val)
                lower_digit = randint(min_val,max_val)
                # print(upper_digit+lower_digit,end=" ")
                len_up = len(str(upper_digit))
                len_lower = len(str(lower_digit))

                if len_lower>len_up:
                    swap  = upper_digit
                    upper_digit = lower_digit
                    lower_digit = swap
                    swap = len_up
                    len_up = len_lower
                    len_lower = swap
                pdf.drawString((x-(len_up*.15))*inch,y*inch, str(upper_digit))
                pdf.drawString((x-(len_lower*.15))*inch,(y-0.25)*inch, str(lower_digit))
                pdf.drawString((x-(len_lower*.15)-.15)*inch,(y-0.23)*inch, "+")
                pdf.line((x-0.4)*inch,(y-.27)*inch,(x)*inch,(y-.27)*inch)
                x += 1.2
            y -= .95
            x =1.5
            # print()
    

        
        


# Create your views here.
def addition(request):
    pdf = canvas.Canvas("./media/addition/addition.pdf")
    pdf_sol = canvas.Canvas("./media/addition/solution.pdf")

    if request.method == 'POST':
        total = request.POST.get('total_value')
        puzzle_per_page = request.POST.get("puzzle")
        day = request.POST.get("day")
        day = int(day)

        # min = []
        # max = []
        # total_page = []

        if total !=None:
            total = int(total)
            for i in range(int(total)):
                # print(i+1)
                min_val = request.POST.get("min"+str(i+1))
                max_val = request.POST.get("max"+str(i+1))
                total_page = request.POST.get("page"+str(i+1))
                min_val = int(min_val)
                max_val = int(max_val)
                x =min(min_val, max_val)
                max_val = max(min_val, max_val)
                min_val = x
                # print(min_val)
                # print(max_val)
                
                for i in range(int(total_page)):
                    make_pdf(pdf,pdf_sol,min_val,max_val,puzzle_per_page,day)
                    pdf.showPage()
    
        else:
            tota = 0
        
        
                

    #     up_min = request.POST.get('up_min')
    #     up_max = request.POST.get('up_max')
    #     lower_min = request.POST.get('low_min')
    #     lower_max = request.POST.get('low_max')
    #     puzzle = request.POST.get('puzzle')
    #     page = request.POST.get('page')

    #     make_pdf(c_pdf,c_pdf_sol,up_min,up_max,lower_min,lower_max,puzzle,page)


    pdf.save()
    return render(request,'addition.html')