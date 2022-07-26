from os import listdir
from os.path import isfile, join
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import random
import string
import os
from wordsearch.models import wordsearch_inner_page
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red,white,HexColor
from wordsearch.solution_pdf import *
from wordsearch.puzzle_make import *

file_source = './media/file'
files = [f for f in listdir(file_source) if isfile(join(file_source, f))]



    
# def print_puzzle(puzzle,grid_size_row,grid_size_col):
#         cnt=0
#         for i in range(grid_size_row):
#             for j in range(grid_size_col):
#                 # print(puzzle[i][j],end = ' ')
#                 if (puzzle[i][j]!='#'):
#                     cnt+=1
#             # print()

#         # print(cnt)

# # Create your views here.

def pdf_make(c,yy,word_font_size,word_up_down,word_left_right,word_l_r_s,word_u_d_s,final_word,puzzle,grid_size_row,grid_size_col,value,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,puzzle_up_down,step):    
    c.setPageSize((8.5 * inch, 11 * inch)) 
    c.setFont("Times-Roman", alphabate_font_size+numbering_font_size)

    # yy=-4 #downward 
    
    # cnt=1
    strr="Puzzle #"+str(step)
    l = len(str(step))
    if number_show==2:
        c.line((numbering_left_right-0.1)*inch, (numbering_up_down-0.08+line_up_down+yy)*inch, (numbering_left_right+1.44+line_left_right+len(str(step))*0.2)*inch, (numbering_up_down-0.08+line_up_down+yy)*inch)
    if number_show==3:
        c.roundRect((numbering_left_right-0.2)*inch,(numbering_up_down-0.15+yy)*inch,(1.8+line_left_right)*inch,(0.5+line_up_down)*inch, 6, stroke=1, fill=0)  
    if number_show==4:
        c.roundRect((numbering_left_right-0.2)*inch,(numbering_up_down-0.15+yy)*inch,(1.8+line_left_right)*inch,(0.5+line_up_down)*inch, 6, stroke=0, fill=1)
        c.setFillColor('white')
        
    c.drawString((numbering_left_right+text_left_right)*inch, (numbering_up_down+text_up_down+yy)*inch, strr)

    c.setFont("Times-Roman", alphabate_font_size)
    c.setFillColor('black')
    
    
    x = 4.5 -((grid_size_col*0.42)/2)
    y=9.4+yy
    inc=0
    c.roundRect((x-0.25+rectangle_left_right)*inch,(y-(grid_size_row*0.42+rectangle_up_down)+0.4+alphabate_up_down)*inch,(grid_size_col*alphabate_space_l_r*1.1+(rectangle_left_right_inc*0.1))*inch,((grid_size_row*0.42) - (rectangle_up_down_inc*0.1))*inch, 1, stroke=1, fill=0)
    # c_sol.rect(4.3*inch,5.5*inch,3.56*inch,3.56*inch, fill=0)
    
    
    
    x+=alphabate_left_right
    y+=alphabate_up_down
    # print(len(puzzle))
    # print(len(puzzle[0]))
    for i in range(grid_size_row):
        for j in range(grid_size_col):
            # print(i,j)
            c.drawString(x*inch,y*inch,puzzle[i][j])            
            x+=alphabate_space_l_r
        x=4.5 -((grid_size_col*0.42)/2)+alphabate_left_right
        y-=alphabate_space_u_d


    x= word_left_right
    c.setFont("Helvetica", word_font_size)
    total= len(final_word)

    
    if total%3!=0:
        length= int(total/3)+1
    else: 
        length = int(total/3)

    rem_x = x
    y = word_up_down+yy
    rem_y = y
    # print(total,length)
    inc  =0
    for i in range(length):
        for j in range(3):
            if inc>=total:
                break
            if((y-0.5<(rem_y-abs(puzzle_up_down)) and yy==0 )or y<0.7):
                break
            if x+len(str(final_word[inc].strip()))*0.12<7.7:
                c.drawString(x*inch,y*inch, str(final_word[inc]))
                inc+=1
                x+=word_l_r_s
            else:
                x = rem_x
                y-=word_u_d_s+0.5
                # print("Y ",y)
                c.drawString(x*inch,y*inch, str(final_word[inc]))
                inc+=1
                x+=word_l_r_s


def delete_all(old_path,check):
    xx = os.listdir(old_path)
    for path in xx:
        if path!=str("%d_inner_design.pdf"%check) and ("inner_design" in path):
            os.remove(old_path+path)
   
def update_info(info,grid_size_row,grid_size_col,word_font_size,word_left_right,word_up_down,word_u_d_s,word_l_r_s,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,alphabate_font_size,alphabate_left_right,alphabate_up_down,alphabate_space_l_r,alphabate_space_u_d,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,puzzle_up_down):
    info.row = grid_size_row
    info.column = grid_size_col
    info.word_font_size = word_font_size
    info.word_left_right = word_left_right
    info.word_up_down = word_up_down
    info.word_up_down_space = word_u_d_s
    info.word_left_right_space = word_l_r_s
    info.rectangle_l_r = rectangle_left_right
    info.rectangle_u_d = rectangle_up_down
    info.rectangle_l_r_i = rectangle_left_right_inc
    info.rectangle_u_d_i = rectangle_up_down_inc
    info.alphabate_font_size = alphabate_font_size
    info.alphabate_left_right = alphabate_left_right
    info.alphabate_up_down = alphabate_up_down
    info.alphabate_left_right_space = alphabate_space_l_r
    info.alphabate_up_down_space = alphabate_space_u_d
    # numbering section
    info.numbering_left_right = numbering_left_right
    info.numbering_up_down = numbering_up_down
    info.number_show = number_show
    info.problem_per_page = problem_per_page
    info.line_left_right = line_left_right
    info.line_up_down = line_up_down
    info.text_left_right = text_left_right
    info.text_up_down = text_up_down
    info.numbering_font_size = numbering_font_size
    info.puzzle_up_down = puzzle_up_down
    info.save()

    return True
# per page problem 2
def create():
    info = wordsearch_inner_page.objects.create(word_font_size=11.40,word_up_down=10.3,word_left_right=6.15,word_left_right_space=1.78,word_up_down_space=-0.28,alphabate_font_size=14.72,alphabate_up_down=0.19,alphabate_left_right=0.30,alphabate_left_right_space=.25,alphabate_up_down_space=0.28,row=10,column=20,rectangle_l_r=0.46,rectangle_u_d=-1.1,rectangle_l_r_i=-4.75,rectangle_u_d_i=12.5,numbering_left_right=0.68,numbering_up_down=10.26,number_show=4,line_left_right=3.25,line_up_down=-0.05,text_left_right=1.49,text_up_down=-0.05,puzzle_up_down=-4.54,problem_per_page=2)
    info.save()
    info = wordsearch_inner_page.objects.all().filter(problem_per_page=2).first()        
    return info
# per page problem 1
def create_per_1():
    info = wordsearch_inner_page.objects.create(problem_per_page=1)
    info.save()
    info = wordsearch_inner_page.objects.all().filter(problem_per_page=1).first()        
    return info

# puzzle solution
def update_puzzle(puzzle,rows,cols):
    for i in range(rows):
        for j in range(cols):
            if puzzle[i][j]=='#':
                puzzle[i][j]=random.choice(string.ascii_letters).upper()
            else:
                puzzle[i][j]=puzzle[i][j].upper()
    return puzzle
    
class design2:
    def make_pdf(pdf,rand,solution_pdf,font,word_font_size,word_left_right,word_up_down,word_u_d_s,word_l_r_s,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,row, col,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,puzzle_up_down,total_problem,test):
        
        pdf.setPageSize((8.5 * inch, 11 * inch))
        path = './media/file'
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        
        
        # wordsearch take save data
        
        if problem_per_page==1:
            info = wordsearch_inner_page.objects.all().filter(problem_per_page=1).first()
            if info==None:
                info = create_per_1()
        if problem_per_page==2:
            info = wordsearch_inner_page.objects.all().filter(problem_per_page=2).first()
            if info==None:
                info = create()
            


        grid_size_row = int(row) if row else info.row
        grid_size_col = int(col) if col else info.column
        word_font_size = info.word_font_size+int(word_font_size)*0.1 if word_font_size else info.word_font_size
        word_left_right = info.word_left_right+int(word_left_right)*0.05 if word_left_right else info.word_left_right
        word_up_down = info.word_up_down+int(word_up_down)*0.05 if word_up_down else info.word_up_down
        word_u_d_s = info.word_up_down_space+int(word_u_d_s)*0.008 if word_u_d_s else info.word_up_down_space
        word_l_r_s = info.word_left_right_space+int(word_l_r_s)*0.02 if word_l_r_s else info.word_left_right_space
        
        # alphabate section
        alphabate_font_size = info.alphabate_font_size+int(alphabate_font_size)*0.07 if alphabate_font_size else info.alphabate_font_size
        alphabate_left_right = info.alphabate_left_right+int(alphabate_left_right)*0.05 if alphabate_left_right else info.alphabate_left_right   
        alphabate_up_down = info.alphabate_up_down+int(alphabate_up_down)*0.05 if alphabate_up_down else info.alphabate_up_down
        alphabate_space_l_r = info.alphabate_left_right_space+int(alphabate_space_l_r)*0.002 if alphabate_space_l_r else info.alphabate_left_right_space
        alphabate_space_u_d = info.alphabate_up_down_space+int(alphabate_space_u_d)*0.008 if alphabate_space_u_d else info.alphabate_up_down_space
        
        
            
        # rectangle section
        rectangle_left_right = info.rectangle_l_r+int(rectangle_left_right)*(0.05) if rectangle_left_right else info.rectangle_l_r
        rectangle_up_down = info.rectangle_u_d+int(rectangle_up_down)*(-0.05) if rectangle_up_down else info.rectangle_u_d
        rectangle_left_right_inc = info.rectangle_l_r_i + int(rectangle_left_right_inc)*(0.1) if rectangle_left_right_inc else info.rectangle_l_r_i
        rectangle_up_down_inc = info.rectangle_u_d_i + int(rectangle_up_down_inc)*(-0.1) if rectangle_up_down_inc else info.rectangle_u_d_i
        
        # print("r_ u_d ",rectangle_up_down_inc)
        #numbering section
        
        numbering_font_size = info.numbering_font_size+int(numbering_font_size)*0.5 if numbering_font_size else info.numbering_font_size    
        numbering_left_right = info.numbering_left_right+int(numbering_left_right)*0.07 if numbering_left_right else info.numbering_left_right 
        numbering_up_down = info.numbering_up_down+int(numbering_up_down)*0.07 if numbering_up_down else info.numbering_up_down
        number_show = int(number_show) if int(number_show)>0 else info.number_show 
        line_left_right = info.line_left_right+int(line_left_right)*0.1 if line_left_right else info.line_left_right
        line_up_down = info.line_up_down+int(line_up_down)*0.05 if line_up_down else info.line_up_down
        text_left_right = info.text_left_right+int(text_left_right)*0.1 if text_left_right else info.text_left_right
        text_up_down = info.text_up_down+int(text_up_down)*0.05 if text_up_down else info.text_up_down
        
        # print("text u d ",text_up_down)
        # down puzzle possitioning
        puzzle_up_down = info.puzzle_up_down+int(puzzle_up_down)*0.05 if puzzle_up_down else info.puzzle_up_down
        # problem per page 
        problem_per_page = int(problem_per_page) if int(problem_per_page)>0 else info.problem_per_page
        update_info(info,grid_size_row,grid_size_col,word_font_size,word_left_right,word_up_down,word_u_d_s,word_l_r_s,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,alphabate_font_size,alphabate_left_right,alphabate_up_down,alphabate_space_l_r,alphabate_space_u_d,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,puzzle_up_down)
            
        
        pro_cnt=0
        puzzle_Arr=[]
        final_word_Arr = []
        store_all_info = []
        page_cnt=0
        # for solution in solution_list:
        r = (0.2*grid_size_row)+0.5
        c = (0.2* grid_size_col)+0.35
        sol_x = 1.3
        sol_y = 9.8
        x_axis = int(7.5/c)
        y_axis = int(9.8/r)
        sol_one_side = 0
        # for solution in solution_list:
        
        
        for file in onlyfiles:
            file_path = path+"/"+file;
            f = open(file_path, "r")
            # print(file)
            if(pro_cnt>=total_problem):
                break
            word_list = []
            for x in f:
                if x!=None:
                    word_list.append(x.strip())
            f.close()
            # print(len(word_list))
            pzl = [['#' for i in range(grid_size_col +2)] for j in range(grid_size_row+2)] 
            f_w = []
            a_i = []
            three_time =3
            mx_total=0
            
            while three_time>=0:
                three_time -= 1    
                puzzle = [['#' for i in range(grid_size_col +2)] for j in range(grid_size_row+2)] 
                total,final_word,puzzle,all_info= Solution.create_puzzle(word_list,puzzle,grid_size_row,grid_size_col)  
                if mx_total<total:
                    mx_total=total
                    f_w = final_word
                    a_i = all_info
                    pzl = puzzle
            # print(all_info)
            if mx_total ==0:
                continue
            # final_word,puzzle,store_all = wordsearch_puzzle.puzzle_possition_set(word_list,grid_size_row,grid_size_col)
            final_word_Arr.append(f_w)
            pzl = update_puzzle(pzl,grid_size_row,grid_size_col)
            puzzle_Arr.append(pzl)
            store_all_info.append(a_i)
            pro_cnt+=1
            # make pdff
            if pro_cnt%problem_per_page==0:
                # print("in")
                page_cnt+=1
                step = pro_cnt-problem_per_page
                value = 1
                yy=0
                xx=puzzle_up_down
                tt=problem_per_page
                while(tt):
                    tt-=1
                    # print(final_word_Arr[step])
                    pdf_make(pdf,yy,word_font_size,word_up_down,word_left_right,word_l_r_s,word_u_d_s,final_word_Arr[step],puzzle_Arr[step],grid_size_row,grid_size_col,value,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,xx,step+1)   
                    yy+=puzzle_up_down
                    # print(puzzle_Arr[step])
                    xx-=puzzle_up_down
                    step+=1
                pdf.showPage()
            # print solution
            tt  = x_axis * y_axis
            if test==0 and pro_cnt%tt==0 and test==0:
                solution_pdf.setPageSize((8.5 * inch, 11 * inch))
                step = pro_cnt-tt
                y_down = abs(9.8 - y_axis*r)/2 
                every_x = abs(8.2 - x_axis*c)/2 - 0.5
                rem_x = sol_x+every_x
                rem_y = y_axis
                y = sol_y - y_down
                if sol_one_side%2:
                    rem_x -=0.7

                while(rem_y):
                    rem_y-=1
                    x=rem_x
                        
                    zz = x_axis
                    while (zz):
                        zz-=1
                        tt-=1
                        solution_design.solution_func(solution_pdf,final_word_Arr[step],puzzle_Arr[step],store_all_info[step],grid_size_row,grid_size_col,x,y,step,c)
                        x = x+c
                        step+=1
                        # if(step>=pro_cnt-1):
                        #     break
                    x = rem_x
                    y= y-r
                solution_pdf.showPage()
                sol_one_side+=1
                    # step+=1
                
                # solution_pdf.showPage()
            
        
        # extra pdf page
        # print("pro_cnt ",pro_cnt%problem_per_page)
        if pro_cnt%problem_per_page:
            page_cnt+=1
            step = pro_cnt-(pro_cnt%problem_per_page)
            # print("step ",step)
            value = 1
            yy=0
            xx=puzzle_up_down
            tt=pro_cnt%problem_per_page
            while(tt):
                tt-=1
                # print(final_word_Arr[step])
                pdf_make(pdf,yy,word_font_size,word_up_down,word_left_right,word_l_r_s,word_u_d_s,final_word_Arr[step],puzzle_Arr[step],grid_size_row,grid_size_col,value,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,xx,step+1)   
                yy+=puzzle_up_down
                # print(puzzle_Arr[step])
                xx-=puzzle_up_down
                step+=1
            pdf.showPage()
        
        # if odd page add extra page
        print("page cnt ",page_cnt)
        if page_cnt%2:
            pdf.showPage()
        
        # extra pdf solution page  
        tt =  x_axis * y_axis
        extra = pro_cnt%tt
        if(pro_cnt%tt  and test==0):
            solution_pdf.setPageSize((8.5 * inch, 11 * inch))
            step = pro_cnt - pro_cnt%tt
            y_down = abs(9.8 - y_axis*r)/2 
            every_x = abs(8.2 - x_axis*c)/2 - 0.5
            rem_x = sol_x+every_x
            rem_y = int(extra/y_axis) +1
            y = sol_y 
            if sol_one_side%2:
                    rem_x -=0.7
                    # print(rem_y)
            while(step<pro_cnt):
                rem_y-=1
                x= rem_x
                zz = x_axis
                while (zz):
                    zz-=1
                    tt-=1
                    solution_design.solution_func(solution_pdf,final_word_Arr[step],puzzle_Arr[step],store_all_info[step],grid_size_row,grid_size_col,x,y,step,c)
                    x = x+c
                    step+=1
                    if(step>=pro_cnt-1):
                        break
                x = rem_x
                y= y-r
            solution_pdf.showPage()
                
                
        
            
        # pdf_make2(pdf,word_font_size,word_up_down,word_left_right,word_l_r_s,word_u_d_s,final_word,puzzle,grid_size_row,grid_size_col,value,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down)   
        
        pdf.save()
        if test:
            path ="./media/wordsearch/"
            delete_all(path,rand)  
        else:
            path ="./media/wordsearch/solution/"
            delete_all(path,rand) 
            solution_pdf.save()
              
            
    def check_path_inner_design():
        paths = os.listdir('./media/wordsearch/')
        file_path =""
        for path in paths:
            if "inner_design" in path:
                file_path = os.path.join('../media/wordsearch/'+path)
        return file_path
    def check_solution():
        paths = os.listdir('./media/wordsearch/solution/')
        file_path =""
        for path in paths:
            if "inner_design" in path:
                file_path = os.path.join('../media/wordsearch/solution/'+path)
        return file_path

