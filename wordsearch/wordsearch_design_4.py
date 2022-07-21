from os import listdir
from os.path import isfile, join
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import random
import string
import os
from wordsearch.models import wordsearch_inner_page
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red,white,HexColor


file_source = './media/file'
files = [f for f in listdir(file_source) if isfile(join(file_source, f))]


def take_pos(x,y,direction,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,dir_x,dir_y):
        if new_x<0 or new_x>=grid_size_row or new_y<0 or new_y>=grid_size_col: 
            return False
        store = []
        store_x = x
        store_y = y
        for i in range(len(word)-1):
            if puzzle[x][y] == '#' :
                if word[i] == puzzle[x][y]:
                    store.append(i)

                puzzle[x][y] = word[i]
                x = x+dir_x 
                y = y+dir_y
            else:
                store.append(-1)
                store_cnt = 0
                
                for x in range(i):
                        if store[store_cnt]== x:
                            store_cnt += 1
                            continue
                        else:
                            puzzle[store_x][store_y] = '#'
                        store_x +=dir_x
                        store_y +=dir_y
                return False 
        return True
    
def print_puzzle(puzzle,grid_size_row,grid_size_col):
        cnt=0
        for i in range(grid_size_row):
            for j in range(grid_size_col):
                # print(puzzle[i][j],end = ' ')
                if (puzzle[i][j]!='#'):
                    cnt+=1
            # print()

        # print(cnt)

# Create your views here.
def select_pos(x,y,word,grid_size_row,grid_size_col,puzzle):
    upper = 4
    right = 5
    down = 6
    left = 7
    up_right=0
    right_down = 1
    down_left = 2
    left_up = 3

    rand = random.randint(0, 7)

    for i in range(rand,rand+8):
        i = i % 8
        
        if i==0:
            new_x = x - len(word)
            new_y = y + len(word)
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,-1,1)
        if i==1:
            new_x = x + len(word)
            new_y = y + len(word)
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,1,1)
        if i==2:
            new_x = x + len(word)
            new_y = y - len(word)
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,1,-1)
        if i==3:
            new_x = x - len(word)
            new_y = y - len(word)
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,-1,-1)
        if i==4:
            new_x = x - len(word)
            new_y = y
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,-1,0)
        if i==5:
            new_x = x 
            new_y = y + len(word)
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,0,1)
        if i==6:
            new_x = x + len(word)
            new_y = y 
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,1,0)
        if i==7:
            new_x = x 
            new_y = y - len(word)
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,0,-1)
        
        if Check_validity == True:
            return True,x,y,new_x,new_y
    return False,x,y,new_x,new_y

def pdf_make(c,yy,word_font_size,word_up_down,word_left_right,word_l_r_s,word_u_d_s,final_word,puzzle,grid_size_row,grid_size_col,value,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,puzzle_up_down,step,right_puzzle):    
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
        # pdf.roundRect((x-rem_x+rem_x/2 -0.3 +r_l_r)*inch,(y-0.67+r_u_d)*inch,(rem_x/2 +0.4+l_r_i)*inch,(0.87+u_d_i)*inch,.1*inch, fill=False, stroke=True)
    if number_show==4:
        c.roundRect((numbering_left_right-0.2)*inch,(numbering_up_down-0.15+yy)*inch,(1.8+line_left_right)*inch,(0.5+line_up_down)*inch, 6, stroke=0, fill=1)
        c.setFillColor('white')
    # print("t l r -->>> ",numbering_left_right+text_left_right)
    # print("t u d -->>> ",text_up_down)
    c.drawString((numbering_left_right+text_left_right)*inch, (numbering_up_down+text_up_down+yy)*inch, strr)
    # c_sol.drawString(1.3*inch, 9*inch, x)
    c.setFont("Times-Roman", alphabate_font_size)
    c.setFillColor('black')
    
    
    x = 4.5 -((grid_size_col*0.42)/2)
    y=9.4+yy
    inc=0
    c.roundRect((x-0.25+rectangle_left_right)*inch,(y-(grid_size_row*0.42+rectangle_up_down)+0.4+alphabate_up_down)*inch,(grid_size_col*alphabate_space_l_r*1.1+(rectangle_left_right_inc*0.1))*inch,((grid_size_row*0.42) - (rectangle_up_down_inc*0.1))*inch, 1, stroke=1, fill=0)
    # c_sol.rect(4.3*inch,5.5*inch,3.56*inch,3.56*inch, fill=0)
    
    
    
    x+=alphabate_left_right
    y+=alphabate_up_down
    for i in range(grid_size_row):
        for j in range(grid_size_col):
            if puzzle[i][j]!='#':
                c.drawString(x*inch,y*inch,puzzle[i][j])
            else:               
                ran= random.choice(string.ascii_letters).upper()
                c.drawString(x*inch,y*inch,ran )
                
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
    rem_y=y
    # print("y -->> "+str(y)+" yy "+str(yy))
    # print("lengthj ",str(len(final_word)))
    for i in range(length):
        for j in range(3):
            if inc>=total:
                break
            # print("xx ",x+len(str(final_word[inc].strip()))*0.1)
            # print(str(final_word[inc].strip()))
            # print("y -> "+str(yy)+" pud "+str(11-abs(puzzle_up_down)))
            if((y+.6<11.25-abs(puzzle_up_down) and yy==0) or y<0.7):
                break
            if  x+len(str(final_word[inc].strip()))*0.1<right_puzzle+0.24:
                c.drawString(x*inch,y*inch, str(final_word[inc].strip()))
                inc+=1
                x+=word_l_r_s
            else:
                x = rem_x
                y-=word_u_d_s+0.5
                # print("Y ",y)
                c.drawString(x*inch,y*inch, str(final_word[inc].strip()))
                inc+=1
                x+=word_l_r_s
                                 
def pdf_make2(c,yy,word_font_size,word_up_down,word_left_right,word_l_r_s,word_u_d_s,final_word,puzzle,grid_size_row,grid_size_col,value,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,puzzle_up_down,step,right_puzzle):    
    c.setFont("Times-Roman", alphabate_font_size+numbering_font_size)

    # yy=-4 #downward 
    
    x_val_update = right_puzzle
    # cnt=1
    strr="Puzzle #"+str(step)
    l = len(str(step))
    if number_show==2:
        c.line((numbering_left_right-0.1+x_val_update)*inch, (numbering_up_down-0.08+line_up_down+yy)*inch, (numbering_left_right+1.44+line_left_right+x_val_update+len(str(step))*0.2)*inch, (numbering_up_down-0.08+line_up_down+yy)*inch)
    if number_show==3:
        c.roundRect((numbering_left_right-0.2+x_val_update)*inch,(numbering_up_down-0.15+yy)*inch,(1.8+line_left_right)*inch,(0.5+line_up_down)*inch, 6, stroke=1, fill=0)  
    if number_show==4:
        c.roundRect((numbering_left_right-0.2+x_val_update)*inch,(numbering_up_down-0.15+yy)*inch,(1.8+line_left_right)*inch,(0.5+line_up_down)*inch, 6, stroke=0, fill=1)
        c.setFillColor('white')
    # print("t l r -->>> ",numbering_left_right+text_left_right)
    # print("t u d -->>> ",text_up_down)
    c.drawString((numbering_left_right+text_left_right+x_val_update)*inch, (numbering_up_down+text_up_down+yy)*inch, strr)
    # c_sol.drawString(1.3*inch, 9*inch, x)
    c.setFont("Times-Roman", alphabate_font_size)
    c.setFillColor('black')
    
    
    x = 4.5 -((grid_size_col*0.42)/2)+x_val_update
    y=9.4+yy
    inc=0
    c.roundRect((x-0.25+rectangle_left_right)*inch,(y-(grid_size_row*0.42+rectangle_up_down)+0.4+alphabate_up_down)*inch,(grid_size_col*alphabate_space_l_r*1.1+(rectangle_left_right_inc*0.1))*inch,((grid_size_row*0.42) - (rectangle_up_down_inc*0.1))*inch, 1, stroke=1, fill=0)
    # c_sol.rect(4.3*inch,5.5*inch,3.56*inch,3.56*inch, fill=0)
    
    
    
    x+=alphabate_left_right
    y+=alphabate_up_down
    for i in range(grid_size_row):
        for j in range(grid_size_col):
            if puzzle[i][j]!='#':
                c.drawString(x*inch,y*inch,puzzle[i][j])
            else:               
                ran= random.choice(string.ascii_letters).upper()
                c.drawString(x*inch,y*inch,ran )
                
            x+=alphabate_space_l_r
        x=4.5 -((grid_size_col*0.42)/2)+alphabate_left_right+x_val_update
        y-=alphabate_space_u_d


    x= word_left_right+x_val_update
    c.setFont("Helvetica", word_font_size)
    total= len(final_word)

    
    if total%3!=0:
        length= int(total/3)+1
    else: 
        length = int(total/3)

    rem_x = x
    y = word_up_down+yy
    rem_y=y
    # print("y -->> "+str(y)+" yy "+str(yy))
    # print("lengthj ",str(len(final_word)))
    for i in range(length):
        for j in range(3):
            if inc>=total:
                break
            # print("xx ",x+len(str(final_word[inc].strip()))*0.1)
            # print(str(final_word[inc].strip()))
            # print("y -> "+str(y)+" pud "+str(abs(puzzle_up_down)))
            if((y+.6<11.25-abs(puzzle_up_down) and yy==0) or y<0.7):
                break
            if x+len(str(final_word[inc].strip()))*0.11<8.2:
                c.drawString(x*inch,y*inch, str(final_word[inc].strip()))
                inc+=1
                x+=word_l_r_s
            else:
                x = rem_x
                y-=word_u_d_s+0.5
                # print("Y ",y)
                c.drawString(x*inch,y*inch, str(final_word[inc].strip()))
                inc+=1
                x+=word_l_r_s
                 

def delete_all(old_path,check):
    xx = os.listdir(old_path)
    for path in xx:
        if path!=str("%d_inner_design.pdf"%check) and ("inner_design" in path):
            os.remove(old_path+path)
   
def update_info(info,grid_size_row,grid_size_col,word_font_size,word_left_right,word_up_down,word_u_d_s,word_l_r_s,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,alphabate_font_size,alphabate_left_right,alphabate_up_down,alphabate_space_l_r,alphabate_space_u_d,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,puzzle_up_down,right_puzzle):
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
    info.right_puzzle = right_puzzle
    info.save()
    
    return True

def create():
    info = wordsearch_inner_page.objects.create(word_font_size=11.40,word_up_down=6.7,word_left_right=1,word_left_right_space=1.78,word_up_down_space=-0.28,alphabate_font_size=14.72,alphabate_up_down=0.19,alphabate_left_right=-1.2,alphabate_left_right_space=.25,alphabate_up_down_space=0.28,row=10,column=10,rectangle_l_r=-1.1,rectangle_u_d=-1.15,rectangle_l_r_i=-.75,rectangle_u_d_i=12.5,numbering_left_right=1.38,numbering_up_down=10.12,number_show=2,line_left_right=0.45,line_up_down=-0.05,text_left_right=0.09,text_up_down=-0.042,puzzle_up_down=-5.24,problem_per_page=4)
    info.save()
    info = wordsearch_inner_page.objects.all().filter(problem_per_page=4).first()        
    return info

def puzzle_possition_set(word_list,grid_size_row,grid_size_col):
    s_word = sorted(word_list,key=len)
    rows,cols = grid_size_row+5, grid_size_col+5
    puzzle = [['#' for i in range(cols)] for j in range(rows)] 
    dic=[]
    total_word=0
    for i in range( len(s_word)):
        cnt = 0
        while cnt<10:

            x = random.randint(0, grid_size_row-1)
            y = random.randint(0, grid_size_col-1)
            list=[]
            value_placement,x,y,new_x,new_y = select_pos(x,y,s_word[i],grid_size_row,grid_size_col,puzzle)
            
            cnt+=1
            if value_placement==True:
                # list=[s_word[i],x,y,new_x,new_y]
                total_word +=len(s_word[i])-1
                dic.append(s_word[i])
                break
    word = []

    for i in range(len(s_word)):
            x = s_word[i] in dic
            if x==False:
                word.append(s_word[i])
    
    word.append("-1")
    pos=0
    for i in  range(grid_size_row-1):
        for j in  range(grid_size_col-1):
                if word[pos]=="-1":
                    break
                value_placement,x,y,new_x,new_y = select_pos(i,j,word[pos],grid_size_row,grid_size_col,puzzle)
                print("x "+str(x)+" y "+str(y)+" new_x "+str(new_x)+" new_y "+str(new_y))
                if value_placement==True:
                    total_word+=len(word[pos])-1
                    dic.append(word[pos])
                    # ssss+= len(word[pos])-1
                    pos+=1
    
    final_word = []
    for i in range(len(word_list)):
            x = word_list[i] in dic
            if x == True:
                final_word.append(word_list[i])
    return final_word,puzzle


class design4:
    def make_pdf(pdf,rand,font,word_font_size,word_left_right,word_up_down,word_u_d_s,word_l_r_s,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,row, col,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,puzzle_up_down,right_puzzle,total_problem,test):
        # rand = random.randint(100000,10000000)
        # pdf  =  canvas.Canvas("./media/wordsearch/%d_inner_design.pdf"%rand)
        pdf.setPageSize((8.5 * inch, 11 * inch))
        path = './media/file'
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        
        
        # wordsearch take save data
        info = wordsearch_inner_page.objects.all().filter(problem_per_page=4).first()
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
        rem_alphabate_left_right = alphabate_left_right
        alphabate_left_right = info.alphabate_left_right+int(alphabate_left_right)*0.05 if alphabate_left_right else info.alphabate_left_right   
        alphabate_up_down = info.alphabate_up_down+int(alphabate_up_down)*0.05 if alphabate_up_down else info.alphabate_up_down
        alphabate_space_l_r = info.alphabate_left_right_space+int(alphabate_space_l_r)*0.002 if alphabate_space_l_r else info.alphabate_left_right_space
        alphabate_space_u_d = info.alphabate_up_down_space+int(alphabate_space_u_d)*0.008 if alphabate_space_u_d else info.alphabate_up_down_space
        right_puzzle = info.right_puzzle+int(right_puzzle)*0.1 if right_puzzle else info.right_puzzle
        
            
        # rectangle section
        rectangle_left_right = info.rectangle_l_r+int(rectangle_left_right)*(0.05) if rectangle_left_right else info.rectangle_l_r
        rectangle_up_down = info.rectangle_u_d+int(rectangle_up_down)*(-0.05) if rectangle_up_down else info.rectangle_u_d
        rectangle_left_right_inc = info.rectangle_l_r_i + int(rectangle_left_right_inc)*(0.5) if rectangle_left_right_inc else info.rectangle_l_r_i
        rectangle_up_down_inc = info.rectangle_u_d_i + int(rectangle_up_down_inc)*(-0.5) if rectangle_up_down_inc else info.rectangle_u_d_i
        
        #numbering section
        
        numbering_font_size = info.numbering_font_size+int(numbering_font_size)*0.5 if numbering_font_size else info.numbering_font_size    
        numbering_left_right = info.numbering_left_right+int(numbering_left_right)*0.07 if numbering_left_right else info.numbering_left_right 
        numbering_up_down = info.numbering_up_down+int(numbering_up_down)*0.07 if numbering_up_down else info.numbering_up_down
        number_show = int(number_show) if int(number_show)>0 else info.number_show 
        line_left_right = info.line_left_right+int(line_left_right)*0.1 if line_left_right else info.line_left_right
        line_up_down = info.line_up_down+int(line_up_down)*0.05 if line_up_down else info.line_up_down
        text_left_right = info.text_left_right+int(text_left_right)*0.1 if text_left_right else info.text_left_right
        text_up_down = info.text_up_down+int(text_up_down)*0.008 if text_up_down else info.text_up_down
        
        if rem_alphabate_left_right:
            rectangle_left_right=alphabate_left_right
        # down puzzle possitioning
        puzzle_up_down = info.puzzle_up_down+int(puzzle_up_down)*0.05 if puzzle_up_down else info.puzzle_up_down
        # problem per page 
        problem_per_page = int(problem_per_page) if int(problem_per_page)>0 else info.problem_per_page
        update_info(info,grid_size_row,grid_size_col,word_font_size,word_left_right,word_up_down,word_u_d_s,word_l_r_s,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,alphabate_font_size,alphabate_left_right,alphabate_up_down,alphabate_space_l_r,alphabate_space_u_d,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,puzzle_up_down,right_puzzle)
            
        final_word_Arr=[]
        puzzle_Arr = []
        pro_cnt=0
        for file in onlyfiles:
            file_path = path+"/"+file;
            f = open(file_path, "r")
            # print(file)
            if(pro_cnt>total_problem):
                break
            word_list = []
            for x in f:
                if x!=None:
                    word_list.append(x)
            f.close()
            # print(len(word_list))
            final_word,puzzle = puzzle_possition_set(word_list,grid_size_row,grid_size_col)
            final_word_Arr.append(final_word)
            puzzle_Arr.append(puzzle)
            pro_cnt+=1
            if pro_cnt%4==0:
                step = pro_cnt-4
                value = 1
                yy=0
                
                # print("puzzle up down ",puzzle_up_down)
                
                xx=puzzle_up_down
                tt=2
                while(tt):
                    tt-=1
                    pdf_make(pdf,yy,word_font_size,word_up_down,word_left_right,word_l_r_s,word_u_d_s,final_word_Arr[step],puzzle_Arr[step],grid_size_row,grid_size_col,value,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,xx,step+1,right_puzzle)   
                    step+=1
                    pdf_make2(pdf,yy,word_font_size,word_up_down,word_left_right,word_l_r_s,word_u_d_s,final_word_Arr[step],puzzle_Arr[step],grid_size_row,grid_size_col,value,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,xx,step+1,right_puzzle)
                    yy+=puzzle_up_down
                    xx-=puzzle_up_down
                    step+=1
                pdf.showPage()
            
                
                
        
        
        pdf.save()
        if test:
            path ="./media/wordsearch/"
            delete_all(path,rand)  
        else:
            path ="./media/wordsearch/solution/"
            delete_all(path,rand)  
            
    def check_path_inner_design():
        paths = os.listdir('./media/wordsearch/')
        file_path =""
        for path in paths:
            if "inner_design" in path:
                file_path = os.path.join('../media/wordsearch/'+path)
        return file_path

