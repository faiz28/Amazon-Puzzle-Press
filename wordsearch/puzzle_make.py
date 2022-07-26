import random





# def print_puzzle(puzzle,rows,cols):
#     for i in range(rows):
#         for j in range(cols):
#             print(puzzle[i][j],end=" ")
#         print()
# def clear_puzzle(puzzle,rows,cols):
#     for i in range(rows):
#         for j in range(cols):
#             puzzle[i][j]='#'

def choose_func(value):
    # print(value)
    if value == 0:
        return 1,1,"DR"
    elif value == 1:
        return 1,0,"R"
    elif value == 2:
        return 1,-1,"DL"
    elif value == 3:
        return -1,-1,"UL"    
    elif value == 4:
        return -1,1,"UR"
    elif value == 5:
        return 0,-1,"U"
    elif value == 6:
        return 0,1,"D"
    elif value == 7:
        return -1,0,"L"

def generate_location(rows,cols):
    x = random.randint(0,rows-1)
    y = random.randint(0,cols-1)
    return x,y 

def update_location(x,y,update_x,update_y,rows,cols):
    # print(str(x)+ " l "+str(y)+" --------->"+str(update_x)+ " u  "+str(update_y))
    
    
    if update_x<0:
        dif = 0 - update_x
        update_x = x+dif
    elif update_x>=rows:
        dif = (rows-1) - update_x
        update_x = x+dif
    else:
        update_x = x
        
    if update_y<0:
        dif = 0 - update_y
        update_y = y+dif
    elif update_y>=cols-1:
        dif = (cols-1) - update_y
        update_y = y+dif
    else:
        update_y = y
    if x>=0 and x<rows and cols>=0 and y<cols:
        
        return True,x,y,update_x,update_y
    
    return False,x,y

def safe(x,y,rows,cols):
    if x>=0 and x<rows and y>=0 and y<cols:
        return True
    else:
        return False

def is_another_word(word,puzzle,x,y,add_x,add_y,rows,cols):
    rem_x =x;rem_y =y
    cnt=0
    for i in range(len(word)):
        # print("in")
        # print(x,y,rows,cols)
        if safe(x,y,rows,cols):
            if (puzzle[x][y] =='#' or puzzle[x][y]==word[i]) :
                cnt+=1            
            x+=add_x
            y+=add_y
        # print(str(x)+" here "+str(y)+" "+str(word[i]))
    if cnt == len(word):
        return True
    else:
        return False

def is_possible_to_set(word,puzzle,x,y,add_x,add_y,rows,cols):
    update_x = x+add_x*len(word); update_y = y+add_y*len(word)
    is_safe,x,y,old_x,old_y =  update_location(x,y,update_x,update_y,rows,cols) #update location if not possible to set
    if is_safe:
        # if(add_x==-1 and add_y==1):
            # print('x -> '+str(x)+' y -> '+str(y)+' update_x -> '+str(old_x)+' update_y -> '+str(old_y)+" word "+word)
        return x,y,is_another_word(word,puzzle,x,y,add_x,add_y,rows,cols)
    
    return x,y,is_safe
    
    
def set_puzzle(word,puzzle,x,y,add_x,add_y,rows,cols):
    # print("set wor d ",word)
    for i in range(len(word)):
        puzzle[x][y] = word[i]
        x+=add_x
        y+=add_y
        # print(puzzle[x][y])
    # print_puzzle(puzzle)


def is_possible_to_check(word,puzzle,X,Y,key,rows,cols):
    length = len(word)
    if key=="DR":
        x,y,Dir = choose_func(0)
    elif key=="R":
        x,y,Dir = choose_func(1)
    elif key=="DL":
        x,y,Dir = choose_func(2)
    elif key=="UL":
        x,y,Dir = choose_func(3)
    elif key=="UR":
        x,y,Dir = choose_func(4)
    elif key=="U":
        x,y,Dir = choose_func(5)
    elif key=="D":
        x,y,Dir = choose_func(6)
    elif key=="L":
        x,y,Dir = choose_func(7)
    else:
        x,y,Dir = 50,50
    
    update_X=X+length*x
    update_Y = Y+length*y
    if update_X>=0 and update_X<rows and update_Y>=0 and update_Y<cols:
        return X,Y,x,y,update_X,update_Y,is_another_word(word,puzzle,X,Y,x,y,rows,cols)
    
    return X,Y,x,y,update_X,update_Y,False   
    
        
class Solution:         
    def create_puzzle(words,puzzle,rows,cols):
        Dir_count ={"DR":0,"DL":0,"UL":0,"UR":0,"U":0,"D":0,"L":0,"R":0}
        cnt=0
        unsolve_word = []
        set_word = []
        # print(len(words))
        # words =  sorted(words, key=len,reverse=True)

        all_info = {}
        
        inc = 0
        for i in range(len(words)):
            
            tt=50
            while(tt):
                tt-=1        
                while True:
                    # add_x,add_y,direction = choose_func(2)
                    add_x,add_y,direction = choose_func(random.randint(0,7))
                    if Dir_count[direction]<6:
                        break
                    
                # print(add_x,add_y,direction)
                if (inc>=len(words)):
                    break
                word = words[inc]
                x,y = generate_location(rows,cols)
                x,y,is_safe = is_possible_to_set(word,puzzle,x,y,add_x,add_y,rows,cols)
                # print("x "+str(x)+" y "+str(y)+" is_safe "+str(direction))
                if(is_safe):
                    inc+=1
                    # print(direction)
                    if direction=='R':
                        new_x,new_y,new_add_x,new_add_y = x+len(word)-1,y,-1,0
                        new_x,new_y,is_safe = is_possible_to_set(word,puzzle,new_x,new_y,new_add_x,new_add_y,rows,cols)
                        set_word.append(word)
                        cnt+=1
                        if is_safe and Dir_count[direction]>Dir_count['L']:
                            Dir_count['L'] +=1
                            all_info[word] = [new_x,new_y,x,y,"L"]
                            set_puzzle(word,puzzle,new_x,new_y,new_add_x,new_add_y,rows,cols)
                        else:
                            Dir_count[direction] +=1
                            all_info[word] = [x,y,new_x,new_y,direction]
                            set_puzzle(word,puzzle,x,y,add_x,add_y,rows,cols)
                            
                    if direction=='L':
                        new_x,new_y,new_add_x,new_add_y = x-(len(word))+1,y,1,0
                        # print(x,y," new  ",new_x,new_y," len -> ",len(word)," word -> ",word)
                        set_word.append(word)
                        cnt+=1
                        if is_safe and Dir_count[direction]>Dir_count['R']:
                            Dir_count['R'] +=1
                            all_info[word] = [new_x,new_y,x,y,"R"]
                            set_puzzle(word,puzzle,new_x,new_y,new_add_x,new_add_y,rows,cols)
                        else:
                            Dir_count[direction] +=1
                            all_info[word] = [x,y,new_x,new_y,direction]
                            set_puzzle(word,puzzle,x,y,add_x,add_y,rows,cols)
                    if direction=='U':
                        new_x,new_y,new_add_x,new_add_y = x,y-len(word)+1,0,1
                        # print(x,y," new  ",new_x,new_y," len -> ",len(word)," word -> ",word)
                        set_word.append(word)
                        cnt+=1
                        if is_safe and Dir_count[direction]>Dir_count['D']:
                            Dir_count['D'] +=1
                            all_info[word] = [new_x,new_y,x,y,"D"]
                            set_puzzle(word,puzzle,new_x,new_y,new_add_x,new_add_y,rows,cols)
                        else:
                            Dir_count[direction] +=1
                            all_info[word] = [x,y,new_x,new_y,direction]
                            set_puzzle(word,puzzle,x,y,add_x,add_y,rows,cols)
                    if direction=='D':
                        new_x,new_y,new_add_x,new_add_y = x,y+(len(word))-1,0,-1
                        # print(x,y," new  ",new_x,new_y," len -> ",len(word)," word -> ",word)
                        set_word.append(word)
                        cnt+=1
                        if is_safe and Dir_count[direction]>Dir_count['U']:
                            Dir_count['U'] +=1
                            all_info[word] = [new_x,new_y,x,y,"U"]
                            set_puzzle(word,puzzle,new_x,new_y,new_add_x,new_add_y,rows,cols)
                        else:
                            Dir_count[direction] +=1
                            all_info[word] = [x,y,new_x,new_y,direction]
                            set_puzzle(word,puzzle,x,y,add_x,add_y,rows,cols)
                    if direction=='UR':
                        new_x,new_y,new_add_x,new_add_y = x-len(word)+1,y+len(word)-1,1,-1
                        # print(x,y," new  ",new_x,new_y," len -> ",len(word)," word -> ",word)
                        set_word.append(word)
                        cnt+=1
                        if is_safe and Dir_count[direction]>Dir_count['DL']:
                            Dir_count['DL'] +=1
                            all_info[word] = [new_x,new_y,x,y,"DL"]
                            set_puzzle(word,puzzle,new_x,new_y,new_add_x,new_add_y,rows,cols)
                        else:
                            Dir_count[direction] +=1
                            all_info[word] = [x,y,new_x,new_y,direction]
                            set_puzzle(word,puzzle,x,y,add_x,add_y,rows,cols)
                    if direction=='UL':
                        new_x,new_y,new_add_x,new_add_y = x-(len(word))+1,y-len(word)+1,1,1
                        # print(x,y," new  ",new_x,new_y," len -> ",len(word)," word -> ",word)
                        set_word.append(word)
                        cnt+=1
                        if is_safe and Dir_count[direction]>Dir_count['DR']:
                            Dir_count['DR'] +=1
                            all_info[word] = [new_x,new_y,x,y,"DR"]
                            set_puzzle(word,puzzle,new_x,new_y,new_add_x,new_add_y,rows,cols)
                        else:
                            Dir_count[direction] +=1
                            all_info[word] = [x,y,new_x,new_y,direction]
                            set_puzzle(word,puzzle,x,y,add_x,add_y,rows,cols)
                            
                    if direction=='DR':
                        new_x,new_y,new_add_x,new_add_y = x+(len(word))-1,y+len(word)-1,-1,-1
                        # print(x,y," new  ",new_x,new_y," len -> ",len(word)," word -> ",word)
                        set_word.append(word)
                        cnt+=1
                        if is_safe and Dir_count[direction]>Dir_count["UL"]:
                            Dir_count['UL'] +=1
                            all_info[word] = [new_x,new_y,x,y,"UL"]
                            set_puzzle(word,puzzle,new_x,new_y,new_add_x,new_add_y,rows,cols)
                        else:
                            Dir_count[direction] +=1
                            all_info[word] = [x,y,new_x,new_y,direction]
                            set_puzzle(word,puzzle,x,y,add_x,add_y,rows,cols)
                    if direction=='DL':
                        new_x,new_y,new_add_x,new_add_y = x+(len(word))-1,y-len(word)+1,-1,1
                        # print(x,y," new  ",new_x,new_y," len -> ",len(word)," word -> ",word)
                        set_word.append(word)
                        cnt+=1
                        if is_safe and Dir_count[direction]>Dir_count["UR"]:
                            Dir_count['UR'] +=1
                            all_info[word] = [new_x,new_y,x,y,"UR"]
                            set_puzzle(word,puzzle,new_x,new_y,new_add_x,new_add_y,rows,cols)
                        else:
                            Dir_count[direction] +=1
                            all_info[word] = [x,y,new_x,new_y,direction]
                            set_puzzle(word,puzzle,x,y,add_x,add_y,rows,cols)


                    # print(word,all_info[word])
                    # cnt+=1
                    # # print(word)
                    # Dir_count[direction] +=1
                    # set_puzzle(word,puzzle,x,y,add_x,add_y)
                    # all_info[word] = [x,y,add_x,add_y,direction]
                    # set_word.append(word)
                    # # print(word)
                    # break
        # print(cnt)
        # print(len(all_info))
        # print((all_info))
        
        for word in words:
            if word not in set_word:
                unsolve_word.append(word)
                # print(word)
        unsolve_word = sorted(unsolve_word, key=len)
        to_un_word = len(unsolve_word)
        un_cnt=0
        # print(to_un_word)
        
        for i in range(rows):
            for j in range(cols):
                if to_un_word>un_cnt:
                    if puzzle[i][j]=='#' or (puzzle[i][j]==unsolve_word[un_cnt][0] and un_cnt<to_un_word):
                        for key in Dir_count.keys():
                            if  to_un_word>un_cnt:
                                x,y,add_x,add_y,update_X,update_Y,is_safe = is_possible_to_check(unsolve_word[un_cnt],puzzle,i,j,key,rows,cols)
                                # print("done")
                                if is_safe: 
                                    # print(unsolve_word[un_cnt])
                                    all_info[unsolve_word[un_cnt]] = [x,y,update_X,update_Y,direction]
                                    set_puzzle(unsolve_word[un_cnt],puzzle,x,y,add_x,add_y,rows,cols)
                                    set_word.append(unsolve_word[un_cnt])
                                    Dir_count[direction] +=1
                                    un_cnt+=1
                                    cnt+=1
        
        
        # for xx in unsolve_word:
        #     print(xx)
        # print(cnt)
        # print('DR ',Dir_count["DR"]," DL ",Dir_count["DL"]," UL ",Dir_count["UL"]," UR ",Dir_count["UR"]," U ",Dir_count["U"]," D ",Dir_count["D"]," L ",Dir_count["L"]," R ",Dir_count["R"])
        return cnt,set_word,puzzle,all_info
        
    

               