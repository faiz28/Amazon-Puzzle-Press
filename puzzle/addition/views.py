from django.shortcuts import render
from random import randint
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red,white,HexColor
from PyPDF2 import PdfFileMerger
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# font 
# ######################################################################################################################
# ######################################################################################################################
# ######################################################################################################################

DejaVuSans = "./media/fonts/DejaVuSans.ttf"
pdfmetrics.registerFont(TTFont('DejaVuSans',DejaVuSans))
AngryCyborg = "./media/fonts/AngryCyborg.ttf"
pdfmetrics.registerFont(TTFont('AngryCyborg',AngryCyborg))
AngryCyborg3D = "./media/fonts/AngryCyborg3D.ttf"
pdfmetrics.registerFont(TTFont('AngryCyborg3D',AngryCyborg3D))
AnimalCuteIcon = "./media/fonts/AnimalCuteIcon.ttf"
pdfmetrics.registerFont(TTFont('AnimalCuteIcon',AnimalCuteIcon))
ArialTh = "./media/fonts/ArialTh.ttf"
pdfmetrics.registerFont(TTFont('ArialTh',ArialTh))
ARIBL0 = "./media/fonts/ARIBL0.ttf"
pdfmetrics.registerFont(TTFont('ARIBL0',ARIBL0))
BabyFreedom = "./media/fonts/BabyFreedom.ttf"
pdfmetrics.registerFont(TTFont('BabyFreedom',BabyFreedom))
BabyFreedom = "./media/fonts/BabyPink-gxRY4.ttf"
pdfmetrics.registerFont(TTFont('BabyFreedom',BabyFreedom))
BabyFreedom = "./media/fonts/Berlin.ttf"
pdfmetrics.registerFont(TTFont('BabyFreedom',BabyFreedom))
# Boge = "./media/fonts/Boge.ttf"
# pdfmetrics.registerFont(TTFont('Boge',Boge))
Bold_Dragon_ttf = "./media/fonts/Bold-Dragon.ttf"
pdfmetrics.registerFont(TTFont('Bold_Dragon_ttf',Bold_Dragon_ttf))
BuzluBuz = "./media/fonts/BuzluBuz.ttf"
pdfmetrics.registerFont(TTFont('BuzluBuz',BuzluBuz))
Calibri = "./media/fonts/Calibri.ttf"
pdfmetrics.registerFont(TTFont('Calibri',Calibri))
calibrib = "./media/fonts/calibrib.ttf"
pdfmetrics.registerFont(TTFont('calibrib',calibrib))
Cambria = "./media/fonts/Cambria.ttf"
pdfmetrics.registerFont(TTFont('Cambria',Cambria))
cambriab = "./media/fonts/cambriab.ttf"
pdfmetrics.registerFont(TTFont('cambriab',cambriab))
CAMBRIAI = "./media/fonts/CAMBRIAI.TTF"
pdfmetrics.registerFont(TTFont('CAMBRIAI',CAMBRIAI))
CAMBRIAZ = "./media/fonts/CAMBRIAZ.TTF"
pdfmetrics.registerFont(TTFont('CAMBRIAZ',CAMBRIAZ))
Chainwhacks = "./media/fonts/Chainwhacks.otf"
pdfmetrics.registerFont(TTFont('Chainwhacks',Chainwhacks))
# Cronisse = "./media/fonts/Cronisse.otf"
# pdfmetrics.registerFont(TTFont('Cronisse',Cronisse))
Dakota_Regular = "./media/fonts/Dakota-Regular.ttf"
pdfmetrics.registerFont(TTFont('Dakota_Regular',Dakota_Regular))
DejaVuSans = "./media/fonts/DejaVuSans.ttf"
pdfmetrics.registerFont(TTFont('DejaVuSans',DejaVuSans))
DejaVuSans_Bold = "./media/fonts/DejaVuSans-Bold.ttf"
pdfmetrics.registerFont(TTFont('DejaVuSans_Bold',DejaVuSans_Bold))
DejaVuSans_BoldOblique = "./media/fonts/DejaVuSans-BoldOblique.ttf"
pdfmetrics.registerFont(TTFont('DejaVuSans_BoldOblique',DejaVuSans_BoldOblique))
DejaVuSansCondensed = "./media/fonts/DejaVuSansCondensed.ttf"
pdfmetrics.registerFont(TTFont('DejaVuSansCondensed',DejaVuSansCondensed))
DejaVuSansCondensed_Bold = "./media/fonts/DejaVuSansCondensed-Bold.ttf"
pdfmetrics.registerFont(TTFont('DejaVuSansCondensed_Bold',DejaVuSansCondensed_Bold))
DejaVuSans_Oblique = "./media/fonts/DejaVuSans-Oblique.ttf"
pdfmetrics.registerFont(TTFont('DejaVuSans_Oblique',DejaVuSans_Oblique))
DissimilarHeadlines = "./media/fonts/DissimilarHeadlines.ttf"
pdfmetrics.registerFont(TTFont('DissimilarHeadlines',DissimilarHeadlines))
DoodleCartoon_1 = "./media/fonts/DoodleCartoon 1.ttf"
pdfmetrics.registerFont(TTFont('DoodleCartoon_1',DoodleCartoon_1))
Eatday = "./media/fonts/Eatday.ttf"
pdfmetrics.registerFont(TTFont('Eatday',Eatday))
EBGaramond_VariableFont_wght = "./media/fonts/EBGaramond_VariableFont_wght.ttf"
pdfmetrics.registerFont(TTFont('EBGaramond_VariableFont_wght',EBGaramond_VariableFont_wght))
futur = "./media/fonts/futur.ttf"
pdfmetrics.registerFont(TTFont('futur',futur))
# HELLOJUCKY_PERSONAL_USE_ONLY = "./media/fonts/HELLOJUCKY_PERSONAL_USE_ONLY.otf"
# pdfmetrics.registerFont(TTFont('HELLOJUCKY_PERSONAL_USE_ONLY',HELLOJUCKY_PERSONAL_USE_ONLY))
Helvetica = "./media/fonts/Helvetica.ttf"
pdfmetrics.registerFont(TTFont('Helvetica',Helvetica))
# helvetica_compressed = "./media/fonts/helvetica-compressed-5871d14b6903a.ttf"
# pdfmetrics.registerFont(TTFont('helvetica_compressed',helvetica_compressed))
# helvetica_rounded = "./media/fonts/helvetica_rounded.otf"
# pdfmetrics.registerFont(TTFont('helvetica_rounded',helvetica_rounded))
# HymalaFont = "./media/fonts/HymalaFont.ttf"
# pdfmetrics.registerFont(TTFont('HymalaFont',HymalaFont))
# ######################################################################################################################
# ######################################################################################################################
# ######################################################################################################################
# ######################################################################################################################




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
    

        
        

def inner_pdf_design(pdf,font,numbering_font_size,d_f_s,n_u_d,n_l_r):    


        
    
    pdf.setPageSize((8.5 * inch, 11 * inch)) 
    pdf.setFont(font, 23)
    pdf.setFillColor(HexColor('#131921'))
    pdf.roundRect(.8*inch,9.9*inch,2.2*inch,.68*inch,.2*inch, fill=True, stroke=False)
    puzzle_per_page = int(60)
    pdf.setFillColor(HexColor('#ffffff'))
    day = 1 
    s = "Day %d"%day
    pdf.drawString(1.5*inch,10.3*inch,s)
    pdf.setFont(font, 18)
    min_val = 0
    max_val = 12
    s2= "Adding Digits %d-%d"%(min_val,max_val)
    len_s =len(s2)
    len_s =len_s/2
    pdf.drawString((2.28-(len_s*.15))*inch,10*inch,s2)
    pdf.setFillColor(black)
    pdf.setFont(font, 20)
    pdf.drawString(3.12*inch,9.95*inch, 'Name :')
    pdf.line(3.95*inch,9.95*inch, 5.92*inch,9.95*inch)
    pdf.circle(6.4*inch,10.18*inch, .36*inch)
    pdf.setFont(font, 13)
    pdf.drawString(6.18*inch,10.3*inch, 'Score  ')
    
    pdf.drawString(6.5*inch,10*inch, '/60')
    pdf.roundRect(6.9*inch,9.9*inch,1*inch,.6*inch,.2*inch, fill=False, stroke=True)
    pdf.line(6.9*inch,10.25*inch,7.9*inch,10.25*inch)
    pdf.drawString(7.2*inch,10.33*inch, 'Time')
    
    

    x=1.5
    y=9.5
    pdf.setFont(font, 16)
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
                pdf.setFont(font, numbering_font_size)
                pdf.setFillColor(HexColor('#6d757a'))
                pdf.drawString((x-n_l_r)*inch,(y+n_u_d)*inch, str((i*6)+j +1)+" )")
                pdf.setFillColor('black' )
                pdf.setFont(font, d_f_s)
                
                # upper digit   
                upper_space = 0.25
                print(upper_digit)
                xx = str(upper_digit)
                while(len_up):
                    pdf.drawString((x-upper_space)*inch,y*inch, str(xx[len_up-1]))
                    upper_space +=.2
                    len_up -=1
                print("done")
                upper_space = 0.25
                while(len_lower):
                    pdf.drawString((x-upper_space)*inch,(y-.27)*inch, str(xx[len_up-1]))
                    upper_space +=.2
                    len_lower -=1
                print("done")
                # pdf.drawString((x-(len_lower*.15))*inch,(y-0.25)*inch, str(lower_digit))
                # pdf.drawString((x-(len_lower*.15)-.15)*inch,(y-0.23)*inch, "+")
                # pdf.line((x-0.4)*inch,(y-.27)*inch,(x)*inch,(y-.27)*inch)
                # pdf.roundRect((x-0.8)*inch,(y-.5)*inch,1.15*inch,.68*inch,.1*inch, fill=False, stroke=True)

                sum = upper_digit+lower_digit
                sol_len = len(str(sum))
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
    addition = '../media/addition/final.pdf'
    return render(request,'addition.html',{'addition':addition})

def inner_design(request):
    
    inner_design =  canvas.Canvas("./media/addition/inner_design.pdf")
    inner_design.setPageSize((8.5 * inch, 11 * inch))
    bd_x =1.8
    bd_y = 9.45
    ##############################################  
    ##############################################  
    ##############################################  
    # by default set the value 
    # ineer section desing ......
    ##############################################  
    ##############################################  
    ##############################################  
    
    font = "DissimilarHeadlines"
    numbering_font_size = 10
    digit_font_size = 16
    numbering_up_down = 0.15
    numbering_left_right = 0.9
    
    if request.method == "POST":
        font = request.POST.get('fonts')
        
        
        
        
        # numbering sector  
        n_f_s = request.POST.get('numbering_font_size')
        n_u_d = request.POST.get('numbering_up_down')
        n_l_r = request.POST.get('numbering_left_right')
        if n_f_s:
            numbering_font_size = int(n_f_s) +  numbering_font_size
        if n_u_d:
            numbering_up_down = int(n_u_d)*.04 +numbering_up_down
        if n_l_r:
            numbering_left_right =  - int(n_l_r)*.07 +numbering_left_right
            
        #digit sector
        d_f_s = request.POST.get('digit_font_size')
        print(d_f_s)
        if d_f_s:
            digit_font_size = int(d_f_s) + digit_font_size
            
        if font=="0":
            font = "DissimilarHeadlines"
        
        print(font)
        
    
    inner_design.setFont("DejaVuSans", 22)
    inner_pdf_design(inner_design,font,numbering_font_size,digit_font_size,numbering_up_down,numbering_left_right)
    inner_design.save()
    in_desing = '../media/addition/inner_design.pdf'
    
    
    
    
    return render(request,'inner-page.html',{'inner_design':in_desing})