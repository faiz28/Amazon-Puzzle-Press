from os import listdir
from os.path import isfile, join
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import random
import string
import os


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
                print(puzzle[i][j],end = ' ')
                if (puzzle[i][j]!='#'):
                    cnt+=1
            print()

        print(cnt)

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

def pdf_make(c,final_word,puzzle,grid_size_row,grid_size_col,cnt,alphabate_space_l_r,alphabate_space_u_d):
    # for wordsearch puzzle
    
    print("alphabate_space_l_r = ",alphabate_space_l_r)
    c.setPageSize((8.5 * inch, 11 * inch)) 

    c.setFont("Times-Roman", 23) 

    x="Puzzle # "+str(cnt)
    c.drawString(3.6*inch, 10*inch, x)
    # c_sol.drawString(1.3*inch, 9*inch, x)
    
    
    x = 4.5 -((grid_size_col*0.42)/2)
    y=9.4
    inc=0
    c.roundRect((x-0.25)*inch,(y-(grid_size_row*0.42)+0.4)*inch,(grid_size_col*0.42 - (alphabate_space_l_r*0.4))*inch,(grid_size_row*0.42)*inch, 1, stroke=1, fill=0)
    # c_sol.rect(4.3*inch,5.5*inch,3.56*inch,3.56*inch, fill=0)
    c.setFont("Times-Roman", 20)
    
    

    
    for i in range(grid_size_row):
        for j in range(grid_size_col):
            if puzzle[i][j]!='#':
                c.drawString(x*inch,y*inch,puzzle[i][j])
            else:               
                ran= random.choice(string.ascii_letters).upper()
                c.drawString(x*inch,y*inch,ran )
                
            x+=alphabate_space_l_r
        x=4.5 -((grid_size_col*0.42)/2)
        y-=alphabate_space_u_d


    x=3
    y=9.4 - grid_size_row*0.42
    c.setFont("Helvetica", 14)
    total= len(final_word)

    for i in range(int(total/3)):
        for j in range(3):
            if j==0:
                c.drawString(1.25*inch,y*inch, str(final_word[inc].strip()))
                inc+=1
            if j==1:
                c.drawString(3.5*inch,y*inch, str(final_word[inc].strip()))
                inc+=1
            if j==2:
                c.drawString(5.79*inch,y*inch, str(final_word[inc].strip()))
                inc+=1
        y-=.3
    extra = total%3
    for j in range(extra):
            if j==0:
                c.drawString(1.25*inch,y*inch, str(final_word[inc].strip()))
                inc+=1
            if j==1:
                c.drawString(3.5*inch,y*inch, str(final_word[inc].strip()))
                inc+=1
            if j==2:
                c.drawString(5.79*inch,y*inch, str(final_word[inc].strip()))
                inc+=1

def delete_all(check):
    xx = os.listdir('./media/wordsearch/')
    for path in xx:
        print(path)
        if path!=str("%d_inner_design.pdf"%check) and ("inner_design" in path):
            print(path)
            os.remove("./media/wordsearch/"+path)
            
    
class design:
    def make_pdf(fonts,word_font_size,word_left_right,word_up_down,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,position_up_down,position_left_right,row, col):
        rand = random.randint(100000,10000000)
        pdf  =  canvas.Canvas("./media/wordsearch/%d_inner_design.pdf"%rand)
        pdf.setPageSize((8.5 * inch, 11 * inch))
        path = './media/file'
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        for file in onlyfiles:
            file_path = path+"/"+file;
            f = open(file_path, "r")
            # print(file)
            word_list = []
        for x in f:
            if x!=None:
                word_list.append(x)
        
        print("row -> ",row)
        if row:
            grid_size_row = int(row)
        else: 
            grid_size_row = 10
        if col:
            grid_size_col  = int(col)
        else:
            grid_size_col = 10
        if alphabate_space_l_r:
            alphabate_space_l_r = int(alphabate_space_l_r)*0.1
        else: 
            alphabate_space_l_r = 0.4
        if alphabate_space_u_d:
            alphabate_space_u_d = int(alphabate_space_u_d)*0.1
        else:
            alphabate_space_u_d = 0.4
        
            
        
            
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
        
        print_puzzle(puzzle,grid_size_row,grid_size_col)
        print("total word : ")
        print(total_word)
        value = 1
        pdf_make(pdf,final_word,puzzle,grid_size_row,grid_size_col,value,alphabate_space_l_r,alphabate_space_u_d)
        pdf.showPage()
        pdf.save()
        delete_all(rand)    
            
    def check_path_inner_design():
        paths = os.listdir('./media/wordsearch/')
        file_path =""
        for path in paths:
            if "inner_design" in path:
                file_path = os.path.join('../media/wordsearch/'+path)
        return file_path