from django.shortcuts import render
from random import randint
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red,white,HexColor
from PyPDF2 import PdfFileMerger
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from addition.models import inner_page
from addition.addition_make import *






# numbering set up
def numbering_setup(pdf,font,numbering_font_size,n_l_r,x,i,j,y,n_u_d,d_f_s,cnt):
    
    pdf.setFont(font, numbering_font_size)
    pdf.setFillColor(HexColor('#6d757a'))
    pdf.drawString((x-n_l_r)*inch,(y+n_u_d)*inch, str(cnt)+".")
    
    
def digit_setup(pdf,font,d_f_s,upper_digit,front_inc,x,d_s,lower_digit,y):
    pdf.setFillColor('black' )
    pdf.setFont(font, d_f_s)
    len_up = len(str(upper_digit))
    # rem_len = len_up+front_inc
    len_lower = len(str(lower_digit))
    upper_space = 0.12
    up_start = upper_space
    # print(upper_digit)
    xx = str(upper_digit)

    while(len_up):
        pdf.drawString((x-upper_space)*inch,y*inch, str(xx[len_up-1]))
        upper_space += 0.18+d_s
        len_up -=1
    # print("done")
    YY = str(lower_digit)
    upper_space = 0.12
    while(len_lower):
        pdf.drawString((x-upper_space)*inch,(y-(.2+d_s*.2+front_inc))*inch, str(YY[len_lower-1]))
        len_lower -=1
        upper_space += 0.18+d_s
        
    pdf.drawString((x-(upper_space))*inch,(y-(.2+d_s*.2+front_inc))*inch, str("+"))
     

    sum = upper_digit+lower_digit
    sol_len = len(str(sum))
    
def recta_setup(pdf,x,y,rem_x,rem_y,r_l_r,r_u_d,l_r_i,u_d_i):
    # print(str(r_u_d)+" r-l-r  "+str(r_l_r))
    # print()
    # print("dfdf ",rem_x)
    pdf.roundRect((x-rem_x+rem_x/2 -0.3 +r_l_r)*inch,(y-0.67+r_u_d)*inch,(rem_x/2 +0.4+l_r_i)*inch,(0.87+u_d_i)*inch,.1*inch, fill=False, stroke=True)
    # pdf.roundRect((x- rem_x+1+r_l_r)*inch,(y-0.67+r_u_d)*inch,(rem_x/2 )*inch,(0.87+u_d_i)*inch,.1*inch, fill=False, stroke=True)

def line_setup(pdf,x,y,rem_x,r_l_r,l_r_i,l_i,l_u_d,l_l_r,p_p_c,u_d_i,r_u_d):
    # print("xx ",x - rem_x/2 +0.4+l_r_i )
    pdf.line((x+l_l_r-rem_x+rem_x/2 -0.3 +r_l_r)*inch,(y-0.25+l_u_d+r_u_d)*inch, (x+l_l_r - rem_x/2 +(1.87-(p_p_c*0.2))+l_r_i + l_i+r_l_r)*inch,(y-0.25+l_u_d+r_u_d)*inch)
    


class in_pdf:
    def update_on_database(info,front_inc,font,header_fonts,header_up_down,header_left_right,font_inc_dec,numbering_font_size,numbering_up_down,numbering_left_right,number_on_off,digit_font_size,digit_up_down,digit_left_right,digit_space,length_of_digit,prob_per_row,prob_per_col,ineer_space,rec_l_r_inc,rec_u_d_inc,rec_on_off,ractangle_up_down,ractangle_left_right,line_inc,line_up_down,line_left_right):
        info.header_fonts = header_fonts
        info.header_up_down = header_up_down
        info.header_left_right = header_left_right
        info.font_inc_dec = font_inc_dec
        
        # number and digit seciton
        info.digit_number_font =font
        info.number_on_off = number_on_off
        info.numbering_font_size = numbering_font_size
        info.numbering_up_down = numbering_up_down
        info.numbering_left_right = numbering_left_right
        
        
        # digit section
        info.digit_font_size = digit_font_size
        info.digit_left_right = digit_left_right
        info.digit_up_down = digit_up_down
        info.digit_space = digit_space
        info.front_inc = front_inc
        info.prob_per_row = prob_per_row
        info.prob_per_col = prob_per_col
        info.length_of_digit = length_of_digit
        info.ineer_space = ineer_space
        
    #   rectangle section
        info.ractangle_up_down = ractangle_up_down
        info.ractangle_left_right =ractangle_left_right
        info.rec_l_r_inc = rec_l_r_inc
        info.rec_u_d_inc = rec_u_d_inc
        info.rec_on_off = rec_on_off
        # line section
        info.line_inc = line_inc
        info.line_up_down = line_up_down
        info.line_left_right = line_left_right
        info.save()
        
           
    def inner_pdf_design(pdf,font,numbering_font_size,n_u_d,n_l_r,d_f_s,d_u_d,d_l_r,d_s,front_inc,p_p_r,p_p_c,l_o_d,r_l_r,r_u_d,l_r_i,u_d_i,l_i,l_u_d,l_l_r,r_o_f,n_o_o,d_i_s,cnt):    
        rem_len_up = 2
        x=1.8+ d_l_r

        y=9.5-front_inc +d_u_d
        
        # column problem control
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
        for i in range(p_p_r):
            for j in range(p_p_c):
                # print(str(y)+" down "+ str(y-(d_s*.2+front_inc)))
                if( y<0.8  or x>(8)):
                    break
                
                upper_digit = randint(1,pow(10,l_o_d))
                lower_digit = randint(1,pow(10,l_o_d))
                cnt+=1            
                if len(str(lower_digit))> len(str(upper_digit)):
                    upper_digit,lower_digit = lower_digit,upper_digit
                if n_o_o:
                    numbering_setup(pdf,font,numbering_font_size,n_l_r,x,i,j,y,n_u_d,d_f_s,cnt)
                digit_setup(pdf,font,d_f_s,upper_digit,front_inc,x,d_s,lower_digit,y)   
                if r_o_f:             
                    recta_setup(pdf,x,y,xx,yy,r_l_r,r_u_d,l_r_i,u_d_i)
                line_setup(pdf,x,y,xx,r_l_r,l_r_i,l_i,l_u_d,l_l_r,p_p_c,u_d_i,r_u_d)
                x += xx+d_i_s
            y -= yy
            x =1.8+d_l_r
            # print()
        
        return cnt
    def page_title_set_up(pdf,day,font,f_i_d,h_u_d,h_l_r,cnt):
        pdf.setPageSize((8.5 * inch, 11 * inch)) 
        x = 0.8+h_l_r
        y = 9.9+h_u_d

        logo = ImageReader('./media/addition/image1.png')
       
        
        pdf.setFont(font, 23+f_i_d)
        pdf.setFillColor(HexColor('#131921'))
        pdf.roundRect(x*inch,(y-0.08)*inch,2.1*inch,.69*inch,.2*inch, fill=True, stroke=False)
        pdf.drawImage(logo,  x*inch, (y+0.02)*inch, 0.8*inch,0.8*inch ,mask='auto')
        # puzzle_per_page = int(puzzle_per_page)
        # pdf.setFillColor(HexColor('#ffffff'))
        pdf.setFillColor(HexColor('#ffffff'))
        s = "Day %d"%day
        pdf.drawString((x+0.7)*inch,(y+0.3)*inch,s)
        pdf.setFont(font, 13+f_i_d)
        s2= "Adding Digits %d-%d"%(10,100)
        len_s =len(s2)
        len_s =len_s/2
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

