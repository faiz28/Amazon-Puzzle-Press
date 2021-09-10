import  sys
N = 9
Garbage =9999999

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
        # print(grid[row][col],end=" ")
        if grid[row][col]==num:
            return True
    
    print()
    return False

def UsedInCol(grid,col,num):
    for row in range(N):
        # print(grid[row][col],end=" ")
        if grid[row][col] == num:
            return True
    print()
    return False

def UsedInBox(grid,boxStartRow,boxStartCol,num):
    for row in range(3):
        for col in range(3):
            # print(grid[row+boxStartRow][col+boxStartCol],end=" ")
            if grid[row+boxStartRow][col+boxStartCol] == num:
                return True
    print()
    return False
 
def isSafe(grid,row,col,number):
    # print("row = ")
    # print(UsedInRow(grid,row,number))
    # print("col")
    # print(UsedInCol(grid,col,number))
    # print("box")
    # print(UsedInBox(grid,row- row % 3,col-col%3,number))
    if UsedInRow(grid,row,number)==False and UsedInCol(grid,col,number)==False and UsedInBox(grid,row- row % 3,col-col%3,number)==False and grid[row][col] == 0:
        return True
    else:
        return False
    # return !UsedInRow(grid, row, num)
	# 	&& !UsedInCol(grid, col, num)
	# 	&& !UsedInBox(grid, row - row % 3,
	# 					col - col % 3, num)
	# 	&& ;

def SolveSudoku(grid):
    row = Garbage
    col = Garbage

    row,col = FindUnassignedLocation(grid,row,col)
    if row==Garbage and col==Garbage:
        return True
    
    
    
    for num in range(1,N+1):
        print("\nFUCKKKKKKKKKKKKKKKKK")
        sys.stdout.write("row = "+ str(row)+" col = "+ str(col) +" number = "+ str(num)  + '\n')
        print("FUCKKKKKKKKKKKKKKKKK")
        print(isSafe(grid,row,col,num))
        if isSafe(grid,row,col,num)==True:
            grid[row][col] = num
            print(grid[row][col] )
            if SolveSudoku(grid):
                return True
            grid[row,col] = 0
    print("DONE")
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
            xx = SolveSudoku(grid)
            print("i am theree")
            if xx == True:
                printGrid(grid)
                print()
            else:
                print("there is no solution")
                
            MakeGridZero(grid)
            if j==0: return True
        
    

if __name__ == "__main__":
    # for i in range(0,9):
    #      print(i,end = " ")
    # print()
    w, h = N, N
    matrix = [[0]*N for i in range(N)]
    MakeGridZero(matrix)
    
    # for i in range(N):
	#      check(i,matrix)
	
    check(1,matrix)
    print()

    main()