from addition.models import inner_page
from reportlab.pdfgen import canvas
from django.shortcuts import render
from reportlab.lib.units import inch
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red,white,HexColor
from PyPDF2 import PdfFileMerger
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from addition.addition_make import *
from reportlab.lib.utils import ImageReader
import random
op={1:'addition',2:'subtraction',3:'multiplication',4:'division'}


def page_title_set_up(pdf,font,f_i_d,h_u_d,h_l_r,cnt,min_val,max_val,day,operation,same_mixed,x_update):
    pdf.setPageSize((8.5 * inch, 11 * inch)) 
    x = x_update-0.8+h_l_r
    y = 9.9+h_u_d
    pdf.setFont(font, 23+f_i_d)
    # print("page title")
    logo = ImageReader('./media/addition/image1.png')
    pdf.setFillColor(HexColor('#131921'))
    pdf.roundRect(x*inch,(y-0.08)*inch,2.1*inch,.69*inch,.2*inch, fill=True, stroke=False)
    pdf.drawImage(logo,  x*inch, (y+0.2)*inch, 0.6*inch,0.6*inch ,mask='auto')
    pdf.setFillColor(HexColor('#ffffff'))
    s = "Day %d"%(day)
    pdf.drawString((x+0.7)*inch,(y+0.3)*inch,s)
    pdf.setFont(font, 13+f_i_d)
   
    if operation=='multiplication':
        if min_val==0 or min_val==1:
            s2= "Multiplying 0's and 1's"
        elif same_mixed==1:
            s2= "Multiplication Mixed"
        else:
            s2 = "Multiplying %d's'"%(min_val)
    if operation=='division':
        if min_val==0 or min_val==1:
            s2= "Dividing 0's and 1's"
        elif same_mixed==1:
            s2= "Division Mixed"
        else:
            s2 = "Dividing %d's'"%(min_val)
    if operation=='mul_div':
        s2= "Multiplication and Division Mixed"
    if operation=='all_mixed':
        s2= "Mixed Problems"

    if len(s2)>20:
        pdf.setFont(font, 13+f_i_d-3.8)
        pdf.drawString((x+0.05)*inch,(y+0.05)*inch,s2)
    else:
        pdf.drawString((x+0.1)*inch,(y+0.05)*inch,s2)
    pdf.setFillColor(black)
    pdf.setFont(font, 18+f_i_d)
    pdf.drawString((x+2.2)*inch,(y+0.05)*inch, 'Name : ')
    pdf.line((x+3.05)*inch,(y)*inch,(x+5)*inch,(y)*inch)
    pdf.circle((x+5.3)*inch,(y+0.28)*inch, .36*inch)
    pdf.setFont(font, 13+f_i_d)
    pdf.drawString((x+5.1)*inch,(y+0.4)*inch, 'Score  ')
    pdf.setFont(font, 16+f_i_d)
    strss = "/"+str(cnt)
    pdf.drawString((x+5.3)*inch,(y+0.1)*inch, strss)
    pdf.setFont(font, 13+f_i_d)
    pdf.roundRect((x+5.82)*inch,y*inch,1*inch,.6*inch,.2*inch, fill=False, stroke=True)
    pdf.line((x+5.82)*inch,(y+0.32)*inch,(x+6.82)*inch,(y+0.32)*inch)
    pdf.drawString((x+6.15)*inch,(y+0.43)*inch, 'Time')
    pdf.setFont(font, 18+f_i_d)
    pdf.drawString((x+6.2)*inch,(y+0.1)*inch, ' : ')

# numbering set up
def numbering_setup(pdf,font,numbering_font_size,n_l_r,x,i,j,y,n_u_d,d_f_s,cnt):
    pdf.setFont(font, numbering_font_size)
    pdf.setFillColor(HexColor('#6d757a'))
    pdf.drawString((x-n_l_r)*inch,(y+n_u_d)*inch, str(cnt)+".")

def  check_divisibility(upper_digit,lower_digit,min_val,max_val):
    # print(min_val,10*min_val)
    upper_digit = randint(min_val,10*min_val)
    if min_val==0:
        return 0,random.randint(1,10)
    cnt=0
    lower_digit = min_val
    
    
    while (True):
        if int(upper_digit)%int(lower_digit)==0:
            break
        upper_digit= randint(min_val,10*min_val)
        cnt+=1
        if cnt>10000:
            return 4,2
        
    return upper_digit,lower_digit
    
def digit_setup(pdf,font,d_f_s,upper_digit,front_inc,x,d_s,lower_digit,y,min_val,max_val,operation,result):
    # operator select
    

    if operation=='addition':
        op_val = "+"
    if operation=='subtraction':
        op_val = "–"
    if operation=='multiplication':
        op_val = "x"
    if operation=='division':
        op_val = "÷"
    if operation=='add_sub':
        if randint(0,1)==0:
            op_val = "+"
        else:
            op_val = "–"
            
    if operation=='mul_div':
        if randint(0,1)==0:
            op_val = "x"
        else:
            op_val = "÷"
            
    if operation=='all_mixed':
        rem_val = randint(0,3)
        if rem_val==0:
            op_val = "+"
        elif rem_val==1:
            op_val = "–"
        elif rem_val==2:
            op_val = "x"
        else:
            op_val = "÷"
            
    # digit font
    pdf.setFillColor('black' )
    pdf.setFont(font, d_f_s)
    if(op_val=='÷'):
        # upper_digit = 0;lower_digit=9
        upper_digit,lower_digit = check_divisibility(upper_digit,lower_digit,min_val,max_val)
    
    
    len_up = len(str(upper_digit))
    # rem_len = len_up+front_inc
    
    upper_space = 0.12
    up_start = upper_space
    # print(upper_digit)
    xx = str(upper_digit)
    

    while(len_up):
        pdf.drawString((x-upper_space)*inch,y*inch, str(xx[len_up-1]))
        upper_space += 0.18+d_s
        len_up -=1
    # print("done")
    upper_space = 0.12
    len_lower = len(str(lower_digit))
    yy = str(lower_digit)
    while(len_lower):
        pdf.drawString((x-upper_space)*inch,(y-(.2+d_s*.2+front_inc))*inch, str(yy[len_lower-1]))
        len_lower -=1
        upper_space += 0.18+d_s
    
    pdf.drawString((x-(upper_space))*inch,(y-(.2+d_s*.2+front_inc))*inch, op_val) 
    
    if op_val=='+':
        result.append(upper_digit+lower_digit)
    elif op_val=='–':
        result.append(upper_digit-lower_digit)
    elif op_val=='x':
        result.append(upper_digit*lower_digit)
    else:
        result.append(upper_digit/lower_digit)
    
def recta_setup(pdf,x,y,rem_x,rem_y,r_l_r,r_u_d,l_r_i,u_d_i):
    # print(str(r_u_d)+" r-l-r  "+str(r_l_r))
    # print()
    # print("dfdf ",rem_x)
    pdf.roundRect((x-rem_x+rem_x/2 -0.3 +r_l_r)*inch,(y-0.67+r_u_d)*inch,(rem_x/2 +0.4+l_r_i)*inch,(0.87+u_d_i)*inch,.1*inch, fill=False, stroke=True)
    # pdf.roundRect((x- rem_x+1+r_l_r)*inch,(y-0.67+r_u_d)*inch,(rem_x/2 )*inch,(0.87+u_d_i)*inch,.1*inch, fill=False, stroke=True)

def line_setup(pdf,x,y,rem_x,r_l_r,l_r_i,l_i,l_u_d,l_l_r,p_p_c,u_d_i,r_u_d):
    # print("xx ",x - rem_x/2 +0.4+l_r_i )
    pdf.line((x+l_l_r-rem_x+rem_x/2 -0.3 +r_l_r)*inch,(y-0.25+l_u_d+r_u_d)*inch, (x+l_l_r - rem_x/2 +(1.87-(p_p_c*0.2))+l_r_i + l_i+r_l_r)*inch,(y-0.25+l_u_d+r_u_d)*inch)

def inner_pdf_design(pdf,font,numbering_font_size,n_u_d,n_l_r,d_f_s,d_u_d,d_l_r,d_s,front_inc,p_p_r,p_p_c,l_o_d,r_l_r,r_u_d,l_r_i,u_d_i,l_i,l_u_d,l_l_r,r_o_f,n_o_o,d_i_s,min_val,max_val,operation,same_mixed,x_update):    
    # variable declaration
    global cnt
    result = []
    
    # task start
    x=x_update  #starting x
    rem_x = x
    y=9.5-front_inc +d_u_d #starting y
    
    # column positioning problem control
    if p_p_c<=3:
        xx= float(7/p_p_c)+0.6
    elif p_p_c==4:
        xx= float(7/p_p_c)+0.2
    elif p_p_c==5:
        xx= float(7/p_p_c)+0.1
    else:
        xx= float(7/p_p_c)
        
    # row problem control
    yy = float(9.5/p_p_r)
    
    rem_min =min_val
    
    # print value
    for i in range(p_p_r):
        for j in range(p_p_c):
            # print(str(y)+" down "+ str(y-(d_s*.2+front_inc)))
            if( y<0.8  or x>(8.4)):
                break
            
            # print("min_val "+str(min_val)+" max_val "+str(max_val))
            import random
            upper_digit = randint(min_val,max_val)
            
            if same_mixed:
                min_val = random.randint(0,min_val)
            
            if min_val==1 or min_val==0:
                min_val=random.randint(0,1)
            
            lower_digit = min_val
            
            randomize = random.randint(0,1)
            if randomize:
                lower_digit,upper_digit = upper_digit,lower_digit
                        
            cnt+=1            
            if len(str(lower_digit))> len(str(upper_digit)):
                upper_digit,lower_digit = lower_digit,upper_digit
                
            # print(str(upper_digit)+" low -> "+str(lower_digit))
            if n_o_o:
                numbering_setup(pdf,font,numbering_font_size,n_l_r,x,i,j,y,n_u_d,d_f_s,cnt)
            digit_setup(pdf,font,d_f_s,upper_digit,front_inc,x,d_s,lower_digit,y,min_val,max_val,operation,result)   
            if r_o_f:             
                recta_setup(pdf,x,y,xx,yy,r_l_r,r_u_d,l_r_i,u_d_i)
            line_setup(pdf,x,y,xx,r_l_r,l_r_i,l_i,l_u_d,l_l_r,p_p_c,u_d_i,r_u_d)
            x += xx+d_i_s  #digit inner space
        y -= yy
        x =rem_x
        # print()
    return result

cnt=0

class Multiplication_division:
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b
    def hello():
        print("hello")

    

    def inner_page_print(min_val,max_val,total_page,operation,day,same_mixed,odd_even_page,rand):
        
        pdf = canvas.Canvas("./media/addition/%d_demo_addition.pdf"%rand)

        # pdf.setPageSize((70, 5000))
        if odd_even_page%2==0:
            bd_x = 1.8
        else:
            bd_x = 1
        bd_y = 9.45
        info = inner_page.objects.all().first()
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
        solution=[[]]
        
        for i in range(int(total_page)):
            if odd_even_page%2==0:
                x_update = 2
            else:
                x_update = 1.2
            
            
            global cnt
            cnt=0
            day+=1
            
            result = inner_pdf_design(pdf,font,numbering_font_size,numbering_up_down,numbering_left_right,digit_font_size,digit_up_down,digit_left_right,digit_space,front_inc,prob_per_row,prob_per_col,length_of_digit,ractangle_left_right,ractangle_up_down,rec_l_r_inc,rec_u_d_inc,  line_inc,line_up_down,line_left_right,rec_on_off,number_on_off,ineer_space,min_val,max_val,operation,same_mixed,x_update)
            solution.append(result)
            page_title_set_up(pdf,header_fonts,font_inc_dec,header_up_down,header_left_right,cnt,min_val,max_val,day,operation,same_mixed,x_update)
            pdf.showPage()
            odd_even_page+=1
        pdf.save()
        
        
        return solution