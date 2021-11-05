from django.shortcuts import render
from random import randint
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red,white,HexColor
from PyPDF2 import PdfFileMerger



def make_pdf(pdf,book_detail,pdf_sol,min_val,max_val,puzzle_per_page,day):
    pdf.setPageSize((8.5 * inch, 11 * inch)) 
    pdf.setFont("Times-Roman", 23)
    pdf.setFillColor(HexColor('#131921'))
    pdf.roundRect(.8*inch,9.9*inch,2.2*inch,.68*inch,.2*inch, fill=True, stroke=False)
    puzzle_per_page = int(puzzle_per_page)
    pdf.setFillColor(HexColor('#ffffff'))
    s = "Day %d"%day
    pdf.drawString(1.5*inch,10.3*inch,s)
    pdf.setFont("Times-Roman", 18)
    s2= "Adding Digits %d-%d"%(min_val,max_val)
    len_s =len(s2)
    len_s =len_s/2
    pdf.drawString((2.28-(len_s*.15))*inch,10*inch,s2)
    pdf.setFillColor(black)
    pdf.setFont("Times-Roman", 20)
    pdf.drawString(3.12*inch,9.95*inch, 'Name :')
    pdf.line(3.95*inch,9.95*inch, 5.92*inch,9.95*inch)
    pdf.circle(6.4*inch,10.18*inch, .36*inch)
    pdf.setFont("Times-Roman", 13)
    pdf.drawString(6.18*inch,10.3*inch, 'Score  ')
    
    pdf.drawString(6.5*inch,10*inch, '/60')
    pdf.roundRect(6.9*inch,9.9*inch,1*inch,.6*inch,.2*inch, fill=False, stroke=True)
    pdf.line(6.9*inch,10.25*inch,7.9*inch,10.25*inch)
    pdf.drawString(7.2*inch,10.33*inch, 'Time')



    pdf_sol.setPageSize((8.5 * inch, 11 * inch))
    pdf_sol.setFillColor(HexColor('#131921'))
    pdf_sol.roundRect(3*inch,9.9*inch,3*inch,.68*inch,.2*inch, fill=True, stroke=False)
    pdf_sol.setFillColor(HexColor('#ffffff'))
    pdf_sol.setFont("Times-Roman", 18)
    pdf_sol.drawString(3.75*inch,10.3*inch,s+" Solution")
    pdf_sol.setFont("Times-Roman", 13)
    pdf_sol.drawString((5.14-(len_s*.15))*inch,10*inch,s2)
   
    
    print(day)
    
    
    
    
    
    
    

   

    
    

    x=1.5
    y=9.5
    pdf.setFont("Helvetica-Bold", 16)
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
                pdf.setFont("Helvetica-Bold", 10)
                pdf.setFillColor(HexColor('#6d757a'))
                pdf.drawString((x-0.5)*inch,(y+0.15)*inch, str((i*6)+j +1)+")")
                pdf.setFillColor(black)
                pdf.setFont("Helvetica-Bold", 16)
                pdf.drawString((x-(len_up*.15))*inch,y*inch, str(upper_digit))
                pdf.drawString((x-(len_lower*.15))*inch,(y-0.25)*inch, str(lower_digit))
                pdf.drawString((x-(len_lower*.15)-.15)*inch,(y-0.23)*inch, "+")
                pdf.line((x-0.4)*inch,(y-.27)*inch,(x)*inch,(y-.27)*inch)



                pdf_sol.setFont("Helvetica-Bold", 10)
                pdf_sol.setFillColor(HexColor('#6d757a'))
                pdf_sol.drawString((x-0.5)*inch,(y+0.15)*inch, str((i*6)+j +1)+")")
                pdf_sol.setFillColor(black)
                pdf_sol.setFont("Helvetica-Bold", 16)
                pdf_sol.drawString((x-(len_up*.15))*inch,y*inch, str(upper_digit))
                pdf_sol.drawString((x-(len_lower*.15))*inch,(y-0.25)*inch, str(lower_digit))
                pdf_sol.drawString((x-(len_lower*.15)-.15)*inch,(y-0.23)*inch, "+")
                pdf_sol.line((x-0.4)*inch,(y-.27)*inch,(x)*inch,(y-.27)*inch)
                sum = upper_digit+lower_digit
                sol_len = len(str(sum))
                pdf_sol.drawString((x-(sol_len*.15))*inch,(y-0.46)*inch, str(sum))
                x += 1.2
            y -= .95
            x =1.5
            # print()
    

        
        


# Create your views here.
def addition(request):
    pdf = canvas.Canvas("./media/addition/addition.pdf")
    book_detail = canvas.Canvas("./media/addition/book_detail.pdf")
    pdf_sol = canvas.Canvas("./media/addition/solution.pdf")
    book_detail.setPageSize((8.5 * inch, 11 * inch))
    bd_x =1.8
    bd_y = 9.45
    bd_store_y = bd_y
    book_detail.setFont("Helvetica-Bold", 22)
    book_detail.drawString((bd_x+1.3)*inch,(bd_y+.40)*inch,'Table of content')
    book_detail.line((bd_x+1.3)*inch,(bd_y+.35)*inch,(bd_x+3.7)*inch,(bd_y+.35)*inch)
    book_detail.setFont("Times-Roman", 20)
    answer_check = ''

    if request.method == 'POST':
        total = request.POST.get('total_value')
        puzzle_per_page = request.POST.get("puzzle")
        day = request.POST.get("day")
        answer_check = request.POST.get("answer")
        day = int(day)

        # min = []
        # max = []
        # total_page = []
        cnt = 1
       
        count_page = 0
        store_page = 0

        if total !=None:
            total = int(total)
            for i in range(int(total)):
                min_val = request.POST.get("min"+str(i+1))
                max_val = request.POST.get("max"+str(i+1))
                total_page = request.POST.get("page"+str(i+1))
                count_page  += int(total_page)
                min_val = int(min_val)
                max_val = int(max_val)
                x =min(min_val, max_val)
                max_val = max(min_val, max_val)
                
                min_val = x
                s= "Adding Digits %d-%d ............................ %d - %d"%(min_val,max_val,store_page,count_page-store_page)
                store_page = count_page
                book_detail.drawString(bd_x*inch,bd_y*inch,s)
                bd_y -= .35
                cnt+=1

                for i in range(int(total_page)):
                    make_pdf(pdf,book_detail,pdf_sol,min_val,max_val,puzzle_per_page,day)
                    day += 1
                    pdf.showPage()
                    pdf_sol.showPage()
                
    
        else:
            tota = 0

        

        # book Details
        book_detail.setFillColor(HexColor('#cccccc'))
        book_detail.roundRect((bd_x-.45)*inch,bd_y*inch,5.8*inch,(bd_store_y+.7-bd_y)*inch,.2*inch, fill=False, stroke=True)
        book_detail.showPage()

                

    #     up_min = request.POST.get('up_min')
    #     up_max = request.POST.get('up_max')
    #     lower_min = request.POST.get('low_min')
    #     lower_max = request.POST.get('low_max')
    #     puzzle = request.POST.get('puzzle')
    #     page = request.POST.get('page')

    #     make_pdf(c_pdf,c_pdf_sol,up_min,up_max,lower_min,lower_max,puzzle,page)


    pdf.save()
    book_detail.save()
    pdf_sol.save()

    merger = PdfFileMerger()
    

    merger.append("./media/addition/book_detail.pdf")
    merger.append("./media/addition/addition.pdf")
    if answer_check:
        merger.append("./media/addition/solution.pdf")
    merger.write("./media/addition/final.pdf")
    merger.close()

    return render(request,'addition.html')