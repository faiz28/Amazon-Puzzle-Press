
import  sys
import  random
N = 9
Garbage =9999999
vl=0

def main():
    print("Hello World!")

def FindUnassignedLocation(grid,row,col):
    
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:
                return row,col
    
    return Garbage,Garbage

def UsedInRow(grid,row,num):
    
    for col in range(N):
        if grid[row][col]==num:
            return True
    
    return False

def UsedInCol(grid,col,num):
    for row in range(N):
        # print(grid[row][col],end=" ")
        if grid[row][col] == num:
            return True
    return False

def UsedInBox(grid,boxStartRow,boxStartCol,num):
    for row in range(3):
        for col in range(3):
            if grid[row+boxStartRow][col+boxStartCol] == num:
                return True
    return False
 
def isSafe(grid,row,col,number):
  
    if UsedInRow(grid,row,number)==False and UsedInCol(grid,col,number)==False and UsedInBox(grid,row- row % 3,col-col%3,number)==False and grid[row][col] == 0:
        return True
    else:
        return False
  

def SolveSudoku(grid):
    global vl
    row = Garbage
    col = Garbage

    row,col = FindUnassignedLocation(grid,row,col)
    if row==Garbage and col==Garbage:
        return True
    
    
    
    for num in range(1,N+1):
        
        if isSafe(grid,row,col,num)==True:
            grid[row][col] = num
            if SolveSudoku(grid):
                return True
            grid[row,col] = 0
    vl =vl+1
    # sys.stdout.write("value = "+vl)
    print("Value = ")
    print(vl)
    if vl<9: SolveSudoku(grid)
    return True


def printGrid(grid):
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end = " ")
        print()

def MakeGridZero(grid):
    for i in range(N):
        for j in range(N):
            grid[i][j] = 0

def check(value,grid):

    for i in range(N):
        for j in range(N):
            grid[i][j] = value
            # xx = 
            print("i am theree")
            # if xx == True:
            #     printGrid(grid)
            #     print()
            # else:
            #     print("there is no solution")
                
            # MakeGridZero(grid)
            # if j==0: return True
        
    

if __name__ == "__main__":
    
    w, h = N, N
    matrix = [[0]*N for i in range(N)]
    MakeGridZero(matrix)
    value = [1,2,3,4,5,6,7,8,9]
    random.shuffle(value)
    for i in range(N):
        matrix[0][i] = value[i]
        print(value[i])
    SolveSudoku(matrix)
    printGrid(matrix)
	
    # check(1,matrix)
    print()

    main()