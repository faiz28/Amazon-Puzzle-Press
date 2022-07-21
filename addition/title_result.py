from webbrowser import Opera
from addition.models import inner_page
from reportlab.pdfgen import canvas
from django.shortcuts import render
from random import randint
from reportlab.lib.units import inch
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red,white,HexColor
from PyPDF2 import PdfFileMerger
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from addition.addition_make import *
from reportlab.lib.utils import ImageReader

class Solution:
    def solution_pdf(result,dic,day):
        pdf = canvas.Canvas("./media/addition/solution.pdf")
        logo = ImageReader('./media/addition/image1.png')
        pdf.setPageSize((8.5 * inch, 11 * inch))
        x=8.5
        y = 11
        info = inner_page.objects.all().first()
        fonts = info.header_fonts
        font_inc_dec = info.font_inc_dec
        # solution start page
        pdf.setFont(fonts, 36+font_inc_dec)
        pdf.setFillColor(HexColor('#131921'))
        pdf.drawString((x/2-(len("Solution")*0.1+1))*inch,(y/2)*inch,'Solution')
        pdf.drawImage(logo,  (x/2)*inch, ((y/2)-0.2)*inch, 2*inch,2*inch,mask='auto')
        pdf.line((x/2 + (len("Solution")*0.1)+0.4)*inch,(y/2-0.1)*inch,(x/2 - (len("Solution")*0.15)-0.8)*inch,(y/2 - 0.1)*inch)
        pdf.showPage()
        
        # print solution

        # pdf.setFont(fonts, 23)
        
        rem_x = 8.5
        # pdf.setFillColor(HexColor('#131921'))
        # pdf.roundRect((rem_x/2 - 1.3)*inch,(y-1.5)*inch,2.8*inch,.69*inch,.2*inch, fill=True, stroke=False)
        # pdf.drawImage(logo,  (rem_x/2 - 1.2)*inch, (y-1.15)*inch, 0.8*inch,0.8*inch ,mask='auto')
        # pdf.setFillColor(HexColor('#ffffff'))
        # s = "Day %d Solution"%(day)
        # pdf.drawString((rem_x/2-1)*inch,(y-1.3)*inch,s)
        y = y-1.8
        x = 1.2
        day=1

        for xx in result:
            print(len(xx))
            for j in xx:
                # print(len(j))
                print(len(j))
                if len(j)<1:
                    continue
                pdf.setFont(fonts, 23)
                pdf.setFillColor(HexColor('#131921'))
                pdf.roundRect((rem_x/2 - 1.3)*inch,(y)*inch,2.8*inch,.69*inch,.2*inch, fill=True, stroke=False)
                pdf.drawImage(logo,  (rem_x/2 - 1.75)*inch, (y)*inch, 0.8*inch,0.8*inch ,mask='auto')
                pdf.setFillColor(HexColor('#ffffff'))
                s = "Day %d Solution"%(day)
                pdf.drawString((rem_x/2-1)*inch,(y+0.2)*inch,s)
                pdf.setFillColor(HexColor('#131921'))
                pdf.setFont(fonts, 17)
                y=y-0.3
                cnt=1
                for k in j:
                    pdf.drawString((x)*inch,(y)*inch,str(cnt)+")"+str(int(k)))
                    x+=1
                    cnt+=1
                    if x>=7.5:
                        x=1.2;y-=.5
                    if y<1:
                        pdf.showPage()
                        pdf.setFont(fonts, 17)
                        y=10

                y -=.8
                if y<1:
                    y=10
                    pdf.showPage()
                day+=1   
                x=1.2
        
        pdf.save()
    def delete_all(check):
        xx = os.listdir('./media/addition/')
        if check!=0:
            path = "../media/addition/%s_final.pdf"%str(check)
            for strrr in xx:
                if strrr != str(check)+"_final.pdf" and "_final"in strrr:
                    os.remove("./media/addition/%s"%strrr)
        else:
            cnt=0
            check =""
            for strrr in xx:
                if "_final"in strrr:
                    if cnt>0:
                        os.remove("../media/addition/%s"%strrr)
                        continue
                    cnt+=1
                    check= strrr
            path = "../media/addition/%s"%str(check)
        
        return path
            
        
    def title_pdf(doc,day):
        info = inner_page.objects.all().first()
        fonts = info.header_fonts
        font_inc_dec = info.font_inc_dec
        
        pdf = canvas.Canvas("./media/addition/title.pdf")
        pdf.setPageSize((8.5 * inch, 11 * inch))
        bd_x =1.8; bd_y = 9.45; bd_store_y = bd_y
        
        logo = ImageReader('./media/addition/image1.png')
        pdf.drawImage(logo,  5*inch, (2)*inch, 3*inch,3*inch ,mask='auto')
        pdf.setFont(fonts, 22+font_inc_dec)
        pdf.drawString((bd_x+1.3)*inch,(bd_y+.40)*inch,'Table of Contents')
        pdf.line((bd_x+1.3)*inch,(bd_y+.35)*inch,(bd_x+3.9)*inch,(bd_y+.35)*inch)
        
        pdf.setFont(fonts, 17+font_inc_dec)
        cnt=0
        dd=0

        for i in doc:
            cnt+=1
            if len(i)<3:
                continue
            if len(doc)==cnt:
                dd = str(day)
            else:
                if len(doc)>=cnt:
                    rem_doc = doc[cnt]
                    dd = rem_doc['day']
            print(i['operation']+ " addition")
            if i['operation'] ==str('addition'):
                s= "Adding Digits %s-%s ............................ %s - %s"%(i['min'],i['max'],str(int(i['day']+1)),dd)
            elif i['operation']=='subtraction':
                s= "Subtracting Digits %s-%s ....................... %s - %s"%(i['min'],i['max'],str(int(i['day']+1)),dd)
            elif i['operation']=='multiplication':
                s= "Multiplying Digits %s-%s ...................... %s - %s"%(i['min'],i['max'],str(int(i['day']+1)),dd)
            if i['operation']=='division':
                s= "Dividing Digits %s-%s .......................... %s - %s"%(i['min'],i['max'],str(int(i['day']+1)),dd)
            elif i['operation']=='add_sub':
                s= "Adding and Subtracting Mixed .......... %s - %s"%(str(int(i['day']+1)),dd)
            elif i['operation']=='mul_div':
                s= "Multiplying and Dividing Mixed ........ %s - %s"%(str(int(i['day']+1)),dd)
            elif i['operation']=='all_mixed':
                s= "Mixed Problems ..................... %s - %s"%(str(int(i['day']+1)),dd)
            pdf.drawString(bd_x*inch,bd_y*inch,s)
            bd_y -= .35
        pdf.drawString((bd_x+1)*inch,bd_y*inch,"(Answer Key in Back)")
        bd_y -= .35
        pdf.setFillColor(HexColor('#cccccc'))
        pdf.roundRect((bd_x-.45)*inch,bd_y*inch,5.8*inch,(bd_store_y+.7-bd_y)*inch,.2*inch, fill=False, stroke=True)
        pdf.showPage()
        pdf.save()