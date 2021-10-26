from django.shortcuts import render
from os import listdir
from os.path import isfile, join
import os,sys,queue,string,random
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from django.core.files.storage import default_storage



def take_pos(x,y,direction,word,puzzle,grid_size,new_x,new_y,dir_x,dir_y):
	if new_x<0 or new_x>=grid_size or new_y<0 or new_y>=grid_size: 
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
def print_puzzle(puzzle,grid_size):
    cnt=0
    for i in range(grid_size):
        for j in range(grid_size):
            print(puzzle[i][j],end = ' ')
            if (puzzle[i][j]!='#'):
                cnt+=1
        print()

    print(cnt)

# Create your views here.
def select_pos(x,y,word,grid_size,puzzle):
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
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size,new_x,new_y,-1,1)
        if i==1:
            new_x = x + len(word)
            new_y = y + len(word)
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size,new_x,new_y,1,1)
        if i==2:
            new_x = x + len(word)
            new_y = y - len(word)
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size,new_x,new_y,1,-1)
        if i==3:
            new_x = x - len(word)
            new_y = y - len(word)
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size,new_x,new_y,-1,-1)
        if i==4:
            new_x = x - len(word)
            new_y = y
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size,new_x,new_y,-1,0)
        if i==5:
            new_x = x 
            new_y = y + len(word)
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size,new_x,new_y,0,1)
        if i==6:
            new_x = x + len(word)
            new_y = y 
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size,new_x,new_y,1,0)
        if i==7:
            new_x = x 
            new_y = y - len(word)
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size,new_x,new_y,0,-1)
        
        if Check_validity == True:
            return True,x,y,new_x,new_y
    return False,x,y,new_x,new_y
		

def pdf_make(c,c_sol,final_word,puzzle,gridsize,cnt):
    # for wordsearch puzzle
    
    c.setPageSize((8.5 * inch, 11 * inch)) 
    c_sol.setPageSize((8.5 * inch, 11 * inch)) 

    c.setFont("Times-Roman", 23)
    c_sol.setFont("Times-Roman", 18)

    x="Puzzle # "+str(cnt)
    c.drawString(3.6*inch, 10*inch, x)
    # c_sol.drawString(1.3*inch, 9*inch, x)
    x = 1.4
    y=9.4
    inc=0
    


    c.rect(1.25*inch,3.6*inch,6.05*inch,6.15*inch, fill=0)
    # c_sol.rect(4.3*inch,5.5*inch,3.56*inch,3.56*inch, fill=0)
    c.setFont("Times-Roman", 20)
    c_sol.setFont("Times-Roman", 25)
    
    
   
    if cnt%4 == 1:
        c_x = 0.69
        c_y = 5.8
        store_x = c_x
        store_y = c_y
        
        # c_sol.drawString(c_x*inch, c_y*inch,'1')
        for i in range(16):
            c_sol.line(c_x*inch,c_y*inch,c_x*inch,(c_y+3.458)*inch)
            c_x += 0.23
        for i in range(16):
            c_sol.line(store_x*inch,store_y*inch,(store_x+3.458)*inch,store_y*inch)
            store_y += 0.23
        c_x = 0.74
        c_y = 5.8+3.27

        puzzle_num="Puzzle # "+str(cnt)
        c_sol.drawString(c_x*inch, (c_y+.35)*inch, puzzle_num)
    if cnt%4 == 2:
        c_x = 4.37
        c_y = 5.8
        store_x = c_x
        store_y = c_y
        for i in range(16):
            c_sol.line(c_x*inch,c_y*inch,c_x*inch,(c_y+3.458)*inch)
            c_x += 0.23
        for i in range(16):
            c_sol.line(store_x*inch,store_y*inch,(store_x+3.458)*inch,store_y*inch)
            store_y += 0.23
        c_x = 4.41
        c_y = 5.8+3.27
        puzzle_num="Puzzle # "+str(cnt)
        c_sol.drawString(c_x*inch, (c_y+.35)*inch, puzzle_num)
    if cnt%4 == 3:
        c_x = 0.69
        c_y = 1
        store_x = c_x
        store_y = c_y

        # c_sol.drawString(c_x*inch, c_y*inch,'1')
        for i in range(16):
            c_sol.line(c_x*inch,c_y*inch,c_x*inch,(c_y+3.458)*inch)
            c_x += 0.23
        for i in range(16):
            c_sol.line(store_x*inch,store_y*inch,(store_x+3.458)*inch,store_y*inch)
            store_y += 0.23
        c_x = 0.74
        c_y = 1+3.27
        puzzle_num="Puzzle # "+str(cnt)
        c_sol.drawString(c_x*inch, (c_y+.35)*inch, puzzle_num)
    if cnt%4 == 0:
        c_x = 4.37
        c_y = 1
        store_x = c_x
        store_y = c_y
        for i in range(16):
            c_sol.line(c_x*inch,c_y*inch,c_x*inch,(c_y+3.458)*inch)
            c_x += 0.23
        for i in range(16):
            c_sol.line(store_x*inch,store_y*inch,(store_x+3.458)*inch,store_y*inch)
            store_y += 0.23
        c_x = 4.41
        c_y = 1+3.27
        puzzle_num="Puzzle # "+str(cnt)
        c_sol.drawString(c_x*inch, (c_y+.35)*inch, puzzle_num)
    
    cnttt=0
    c_sol.setFont("Times-Roman", 15)
    for i in range(gridsize):
        for j in range(gridsize):
            if puzzle[i][j]!='#':
                c.drawString(x*inch,y*inch,puzzle[i][j])
                c_sol.drawString(c_x*inch,c_y*inch,puzzle[i][j])
               
                cnttt+=1
            else:               
                ran= random.choice(string.ascii_letters).upper()
                c.drawString(x*inch,y*inch,ran )
                
            x+=.4
            c_x += 0.23
        if cnt%4==1 or cnt%4==3:
            c_x = 0.74
        if cnt%4==2 or cnt%4==0:
            c_x = 4.41
        c_y -= 0.23
        x=1.4
        y-=.4


    x=3
    y=3.1
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

def solution(request):
    # if request.method == 'POST':
    #     file = request.FILES.get('wordsearch')
    #     print(file)
    #     if file:
    #         path = '../wordsearch_front.pdf'
    #         os.remove(path)

    #         file.name = 'wordsearch_front.pdf'
    #         file_name = default_storage.save(file.name, file)

    #         #  Reading file from storage
    #         print(file)
    #         print("dfdfdf")
    #         file = default_storage.open(file_name)
    #         file_url = default_storage.url(file_name)
    #     wordsearch = '../media/wordserch/wordserch.pdf'
    #     solution = '../media/wordserch/solution/solution.pdf'
    #     return render(request,'solution.html',{'wordsearch':wordsearch,'solution':solution})
    # else:
    value = 1
    c_pdf = canvas.Canvas("./media/wordserch/wordserch.pdf")
    c_pdf_sol = canvas.Canvas("./media/wordserch/solution/solution.pdf")
    path = './media/file'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for filename in onlyfiles:
        # print(filename  )
        file_path = path+"/"+filename;
        f = open(file_path, "r")
        word_list = []
        for x in f:
            if x!=None:
                word_list.append(x)
        
        grid_size = 15
        s_word = sorted(word_list,key=len)
        rows,cols = grid_size+5, grid_size+5
        puzzle = [['#' for i in range(cols)] for j in range(rows)] 

        # set in puzzle
        dic=[]
        total_word=0
        for i in range( len(s_word)):
            cnt = 0
            while cnt<10:

                x = random.randint(0, grid_size-1)
                y = random.randint(0, grid_size-1)
                list=[]
                value_placement,x,y,new_x,new_y = select_pos(x,y,s_word[i],grid_size,puzzle)
                
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
        for i in  range(grid_size-1):
            for j in  range(grid_size-1):
                    if word[pos]=="-1":
                        break
                    value_placement,x,y,new_x,new_y = select_pos(i,j,word[pos],grid_size,puzzle)
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
        
        print_puzzle(puzzle,grid_size)
        print("total word : ")
        print(total_word)
        pdf_make(c_pdf,c_pdf_sol,final_word,puzzle,grid_size,value)

        c_pdf.showPage()
        if value%4==0:
            c_pdf_sol.showPage()
        value += 1
            
        # count += 1
    c_pdf.save()
    c_pdf_sol.save()
    

    wordsearch = '../media/wordserch/wordserch.pdf'
    solution = '../media/wordserch/solution/solution.pdf'
    return render(request,'solution.html',{'wordsearch':wordsearch,'solution':solution})