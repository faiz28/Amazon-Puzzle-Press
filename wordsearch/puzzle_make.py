import random
import string

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
# class wordsearch_puzzle:
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
    kk=-99
    for i in range(rand,rand+8):
        i = i % 8
        
        if i==0:
            new_x = x - len(word)
            new_y = y + len(word)
            kk = i
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,-1,1)
        if i==1:
            new_x = x + len(word)
            new_y = y + len(word)
            kk = i
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,1,1)
        if i==2:
            new_x = x + len(word)
            new_y = y - len(word)
            kk = i
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,1,-1)
        if i==3:
            new_x = x - len(word)
            new_y = y - len(word)
            kk = i
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,-1,-1)
        if i==4:
            new_x = x - len(word)
            new_y = y
            kk = i
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,-1,0)
        if i==5:
            new_x = x 
            new_y = y + len(word)
            kk = i
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,0,1)
        if i==6:
            new_x = x + len(word)
            new_y = y 
            kk = i
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,1,0)
        if i==7:
            new_x = x 
            new_y = y - len(word)
            kk = i
            Check_validity = take_pos(x,y,i,word,puzzle,grid_size_row,grid_size_col,new_x,new_y,0,-1)
        
        if Check_validity == True:
            return True,x,y,new_x,new_y,kk
    return False,x,y,new_x,new_y,kk


# import random
# import string

# def select_direction(x):
#     if x==0:
#         return "DUR"
#     if x==1:
#         return "R"
#     if x==2:
#         return "DDR"
#     if x==3:
#         return "L"
#     if x==4:
#         return "DUL"
#     if x==5:
#         return "D"
#     if x==6:
#         return "U"
#     if x==7:
#         return "DDL"
    
    
    
# def select_pos(x,y,word,grid_size_row,grid_size_col,puzzle):
#     new_x=-1;new_y=-1
#     choose_option =select_direction(random.randint(0,100000000000000)%8)
#     if choose_option == "DUR":
#         rem_x = x
#         rem_y = y
        
#     return False,x,y,new_x,new_y
def choose_func(value):
    if value == 0:
        return 1,1,"DR"
    elif value == 1:
        return 0,1,"R"
    elif value == 2:
        return 1,-1,"DL"
    elif value == 3:
        return -1,-1,"UL"    
    elif value == 4:
        return -1,1,"UR"
    elif value == 5:
        return -1,0,"U"
    elif value == 6:
        return 1,0,"D"
    elif value == 7:
        return -1,0,"L"


class wordsearch_puzzle:
    def puzzle_possition_set(word_list,grid_size_row,grid_size_col):
        s_word = sorted(word_list,key=len)
        Dir_count ={"DR":0,"DL":0,"UL":0,"UR":0,"U":0,"D":0,"L":0,"R":0}
        rows,cols = grid_size_row+5, grid_size_col+5
        puzzle = [['#' for i in range(cols)] for j in range(rows)] 
        dic=[]
        total_word=0
        store_all = {}
        for i in range( len(s_word)):
            cnt = 0
            while cnt<10:

                x = random.randint(0, grid_size_row-1)
                y = random.randint(0, grid_size_col-1)
                list=[]
                value_placement,x,y,new_x,new_y,kk = select_pos(x,y,s_word[i],grid_size_row,grid_size_col,puzzle)
                
                cnt+=1
                if value_placement==True:
                    # list=[s_word[i],x,y,new_x,new_y]
                    total_word +=len(s_word[i])-1
                    store_all[s_word[i]] = [x,y,new_x,new_y]
                    dic.append(s_word[i])
                    m,n,dd = choose_func(kk)
                    Dir_count[dd]+=1
                    break
        word = []

        for i in range(len(s_word)):
                x = s_word[i] in dic
                if x==False:
                    word.append(s_word[i])
        
        word.append("-1")
        pos=0
        print("grid")
        for i in  range(grid_size_row):
            for j in  range(grid_size_col):
                # print("j --> ",j)
                if word[pos]=="-1":
                    break
                value_placement,x,y,new_x,new_y,kk = select_pos(i,j,word[pos],grid_size_row,grid_size_col,puzzle)
                if value_placement==True:
                    total_word+=len(word[pos])-1
                    dic.append(word[pos])
                    store_all[s_word[i]] = [x,y,new_x,new_y]
                    # ssss+= len(word[pos])-1
                    pos+=1
        
        final_word = []
        for i in range(len(word_list)):
                x = word_list[i] in dic
                if x == True:
                    final_word.append(word_list[i])

        for i in range(grid_size_row):
            for j in  range(grid_size_col):
                if puzzle[i][j]=='#':
                    puzzle[i][j]=random.choice(string.ascii_letters).upper()
        
        print("DR -> ",Dir_count["DR"],"DL -> ",Dir_count["DL"],"UL -> ",Dir_count["UL"],"UR -> ",Dir_count["UR"],"U -> ",Dir_count["U"],"D -> ",Dir_count["D"],"L -> ",Dir_count["L"],"R -> ",Dir_count["R"])
        # print(puzzle) 
        return final_word,puzzle,store_all
