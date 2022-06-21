from django.shortcuts import render
from random import randint
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red,white,HexColor
from PyPDF2 import PdfFileMerger
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from addition.models import inner_page
from addition.addition_make import *
from addition.inner_pdffff import *
from addition.title_result import *

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
    

# Create your views here.
def addition(request):
    
    print_final=0
    if request.method == 'POST':
        total = request.POST.get('total_value')
        puzzle_per_page = request.POST.get("puzzle")
        # days = request.POST.get("day")
        answer_check = request.POST.get("answer")
        day = 0
        cnt = 1
       
        count_page = 0
        store_page = 0

        if total !=None:
            total = int(total)
            dic=[{}]
            result=[[]]

            for i in range(int(total)):
                merger = PdfFileMerger()
                min_val = request.POST.get("min"+str(i+1))
                max_val = request.POST.get("max"+str(i+1))
                total_page = request.POST.get("page"+str(i+1))
                operation = request.POST.get("operation"+str(i+1))
                dic.append({'min':min_val,'max':max_val,'day':day,'operation':operation})
                
 
                
                if int(min_val)>int(max_val):
                    min_val,max_val = max_val,min_val
                max_val = int(max_val)
                min_val = int(min_val)                
                solution = make_addition.inner_page_print(min_val,max_val,total_page,operation,day)
                result.append(solution)
                merger.append("./media/addition/demo_addition.pdf")
                merger.write("./media/addition/addition%d.pdf"%i)
                merger.close()
                day += int(total_page)
            # inner section all file add
            merger = PdfFileMerger()
            for i in range(int(total)):
                merger.append("./media/addition/addition%d.pdf"%i)
                os.remove("./media/addition/addition%d.pdf"%i)
            merger.write("./media/addition/addition.pdf")
            merger.close()
            # title page ready
            Solution.title_pdf(dic,day)
            Solution.solution_pdf(result,dic,day)
            merger = PdfFileMerger()
            merger.append("./media/addition/title.pdf")
            merger.append("./media/addition/addition.pdf")
            merger.append("./media/addition/solution.pdf")
            print_final= randint(100,10000000)
            xx = "./media/addition/%s_final.pdf"%str(print_final)
            merger.write(xx)
            merger.close()
        else:
            total = 0

    
    path = Solution.delete_all(print_final)

        
    return render(request,'addition.html',{'addition':path})

    
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
    
    
    
    info = inner_page.objects.all().first()
    # print(info.header_fonts)
    # print("hello ",info['header_fonts'])
    # header section
    id = info.id
    header_fonts = info.header_fonts
    header_up_down = info.header_up_down
    header_left_right = info.header_left_right
    font_inc_dec = info.font_inc_dec
    
    # number and digit seciton
    font = info.digit_number_font
    number_on_off = info.number_on_off
    numbering_font_size = info.numbering_font_size
    numbering_up_down = info.numbering_up_down
    numbering_left_right = info.numbering_left_right
    
    
    # digit section
    digit_font_size = info.digit_font_size
    digit_left_right = info.digit_left_right
    digit_up_down = info.digit_up_down
    digit_space = info.digit_space
    front_inc = info.front_inc
    prob_per_row = info.prob_per_row
    prob_per_col = info.prob_per_col
    length_of_digit = info.length_of_digit
    if prob_per_row<=0:
        prob_per_row =1
    if prob_per_col<=0:
        prob_per_col =1
#   rectangle section
    ractangle_up_down = info.ractangle_up_down
    ractangle_left_right = info.ractangle_left_right
    rec_l_r_inc =info.rec_l_r_inc
    rec_u_d_inc =info.rec_u_d_inc
    rec_on_off = info.rec_on_off
    # line section
    line_inc =info.line_inc
    line_up_down = info.line_up_down
    line_left_right = info.line_left_right
    ineer_space = info.ineer_space
    
    cnt=0
    
    if request.method == "POST":
        fontsss = request.POST.get('fonts')
        # header section
        h_f = request.POST.get('header_fonts')
        f_i = request.POST.get('font_inc_dec')
        h_u_d = request.POST.get('header_up_down')
        h_l_r = request.POST.get('header_left_right')
        if h_f:
            header_fonts = h_f
        if f_i:
            font_inc_dec = int(f_i)*0.5
        if h_u_d:
            header_up_down = int(h_u_d)*0.1
        if h_l_r:
            header_left_right = int(h_l_r)*0.1
        
        # numbering sector  
        n_f_s = request.POST.get('numbering_font_size')
        n_u_d = request.POST.get('numbering_up_down')
        n_l_r = request.POST.get('numbering_left_right')
        n_o_o = request.POST.get('number_on_off')
        if n_f_s:
            numbering_font_size = int(n_f_s) +  numbering_font_size
        if n_u_d:
            numbering_up_down = int(n_u_d)*.04 +numbering_up_down
        if n_l_r:
            numbering_left_right =  - int(n_l_r)*.07 +numbering_left_right
        if n_o_o:
            number_on_off =int(n_o_o)
            
        #digit sector
        d_f_s = request.POST.get('digit_font_size')
        
        d_u_d = request.POST.get('digit_up_down')
        d_l_r = request.POST.get('digit_left_right')
        d_s = request.POST.get('digit_space')
        p_p_r = request.POST.get('prob_per_row')
        p_p_c = request.POST.get('prob_per_col')
        l_o_d = request.POST.get('length_of_digit')
        d_i_s = request.POST.get('ineer_space')
        
        # digit section
        if d_f_s:
            digit_font_size = int(d_f_s) + digit_font_size
            front_inc += int(d_f_s)*0.01
        if d_u_d:
            digit_up_down = int(d_u_d)*.07 +digit_up_down
        if d_l_r:
            digit_left_right =  int(d_l_r)*.07 +digit_left_right
        if d_s:
            digit_space = int(d_s)*.02 +digit_space
        if l_o_d:
            length_of_digit = int(l_o_d)
        if p_p_r:
            prob_per_row = int(p_p_r)
        if p_p_c:
            prob_per_col = int(p_p_c)
        if d_i_s:
            ineer_space  = 0.1*int(d_i_s)
            
            
        # rectangle sector
        r_u_d = request.POST.get('ractangle_up_down')
        r_l_r = request.POST.get('ractangle_left_right')
        l_r_i = request.POST.get("rec_l_r_inc")
        u_d_i = request.POST.get("rec_u_d_inc")
        r_o_f = request.POST.get("rec_o_o")
        
        if r_u_d:
            ractangle_up_down = int(r_u_d)*0.1+ractangle_up_down
        if r_l_r:
            ractangle_left_right = int(r_l_r)*0.1+ractangle_left_right
        if l_r_i:
            rec_l_r_inc = int(l_r_i)*0.1+rec_l_r_inc
        if u_d_i:
            rec_u_d_inc = int(u_d_i)*0.04+rec_u_d_inc 
            
        if r_o_f:
            rec_on_off=1-int(r_o_f)
        # line section
        l_l_r = request.POST.get('line_left_right')
        l_u_d = request.POST.get('line_up_down')
        l_i = request.POST.get("line_inc")
        if l_l_r:
            line_left_right = int(l_l_r)*0.05+line_left_right
        if l_u_d:
            line_up_down = int(l_u_d)*0.05+line_up_down
        if l_i:
            line_inc = int(l_i)*0.05+line_inc    
        
        if fontsss:
            font = fontsss
        # info = inner_page.objects.get(id=id)
        in_pdf.update_on_database(info,front_inc,font,header_fonts,header_up_down,header_left_right,font_inc_dec,numbering_font_size,numbering_up_down,numbering_left_right,number_on_off,digit_font_size,digit_up_down,digit_left_right,digit_space,length_of_digit,prob_per_row,prob_per_col,ineer_space,rec_l_r_inc,rec_u_d_inc,rec_on_off,ractangle_up_down,ractangle_left_right,line_inc,line_up_down,line_left_right)
        
    # inner_design.setFont(font, 22)
    cnt = in_pdf.inner_pdf_design(inner_design,font,numbering_font_size,numbering_up_down,numbering_left_right,digit_font_size,digit_up_down,digit_left_right,digit_space,front_inc,prob_per_row,prob_per_col,length_of_digit,ractangle_left_right,ractangle_up_down,rec_l_r_inc,rec_u_d_inc,  line_inc,line_up_down,line_left_right,rec_on_off,number_on_off,ineer_space,cnt)
    in_pdf.page_title_set_up(inner_design,1,header_fonts,font_inc_dec,header_up_down,header_left_right,cnt)
    
    inner_design.save()
    in_desing = '../media/addition/inner_design.pdf'
    
    
    

    return render(request,'inner-page.html',{'inner_design':in_desing,'info':info})