import random
import  sys

# word sorting
def word_sorting(word):
	lst = sorted(word,key=len)
	return lst

def take_pos(x,y,direction,word,puzzle,grid_size,new_x,new_y,xx,yy):
	# sys.stdout.write(str(new_x)+" new_x "+ str(new_y) +" new_y "+word+"\n")
	if new_x<0 or new_x>=grid_size or new_y<0 or new_y>=grid_size: 
		return False
	store = []
	x = x 
	y = y 
	store_x = x
	store_y = y
	pos = -999

	for i in range(len(word)-1):
		# sys.stdout.write(puzzle[x][y]+" "+ word[i] +"\n")
		if puzzle[x][y] == '#' or puzzle[x][y] == word[i]:
			if word[i] == puzzle[x][y]:
				store.append(i)
			puzzle[x][y] = word[i]
			# sys.stdout.write(str(x)+" x "+ str(y) +" y = "+puzzle[x][y]+"\n")

			x = x+xx 
			y = y+yy
			# print_puzzle(puzzle,grid_size)
		else:
			pos = i
			break
		# sys.stdout.write(str(x)+" x "+ str(y) +" y "+word+"\n")
		# print(word[i])
	
	if pos > 0 :
		check_similar_alphabate = 0
		
		store.append(-1)
			

		for i in range(pos):
			if i == store[check_similar_alphabate]:
				check_similar_alphabate += 1
			else:
				puzzle[store_x][store_y] = '#'
			store_x += xx
			store_y += yy
			
		return False
		
	if pos==0: return False
	else: return True


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
		i = i%8
		
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
			return True
	return False
		

# make puzzle with null string
def print_puzzle(puzzle,grid_size):
	for i in range(grid_size):
		for j in range(grid_size):
			print(puzzle[i][j],end = ' ')
		print()

if __name__ == "__main__":
		number = 0
		while number<10:
			number += 1
			f = open("./worddd/fileee1.txt", "r")
			word = []
			for x in f:
				word.append(x)

			# word sorting
			grid_size = 20
			s_word = word_sorting(word)
			
			
			# make puzzle with null string
			rows, cols = (grid_size+5, grid_size+5)
			puzzle = [['#' for i in range(cols)] for j in range(rows)] 

			
			# print_puzzle(puzzle,grid_size)

			# set in puzzle
			dic=[]
			for i in range( len(s_word)):
				cnt = 0
				while cnt<10:
					x = random.randint(0, grid_size-1)
					y = random.randint(0, grid_size-1)
					value_placement = select_pos(x,y,s_word[i],grid_size,puzzle)
					# print(word[i])
					# print(value_placement)
					cnt+=1
					if value_placement==True:
						dic.append(word[i])
						break

			again_check = []
			for i in range(len(s_word)):
					x = s_word[i] in dic
					if x==False:
						again_check.append(s_word[i])
						
			for i in  range(grid_size-1):
				for j in  range(grid_size-1):
					for z in range(len(again_check)-1):
							
						value_placement = select_pos(i,j,again_check[z],grid_size,puzzle)
						if value_placement==True:
							again_check.remove(again_check[z])
							print(len(again_check))
							dic.append(again_check[z])

			for i in range(len(s_word)):
					x = s_word[i] in dic
					if x==False:
						again_check.append(s_word[i])
					print(x,end = " ")
			print_puzzle(puzzle,grid_size)
			print()
			print()