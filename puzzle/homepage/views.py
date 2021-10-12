from django.shortcuts import render
import sys
from Sudoku.Generator import *

# Create your views here.
def home(request):
    # SUDOKU GENERATOR ...........................................
    # difficulties = {
    #     'easy': (35, 0), 
    #     'medium': (81, 5), 
    #     'hard': (81, 10), 
    #     'extreme': (81, 15)
    # }
    # difficulty = difficulties['easy']
    # for i in range(200):
    #     gen = Generator('./homepage/base.txt')
    #     gen.randomize(100)

    #     # getting a copy before slots are removed
    #     initial = gen.board.copy()

    #     # applying logical reduction with corresponding difficulty cutoff
    #     # print(difficulty[0],end= "   difficulty 0\n")

    #     gen.reduce_via_logical(difficulty[0])
    #     # catching zero case
    #     if difficulty[1] != 0:
    #         # applying random reduction with corresponding difficulty cutoff
    #         gen.reduce_via_random(difficulty[1])

    #     # getting copy after reductions are completed
    #     final = gen.board.copy()

    #     print(i+1)

    #     # printing out complete board (solution)
    #     print("The initial board before removals was: \r\n\r\n{0}".format(initial))

    #     # printing out board after reduction
    #     print("The generated board after removals was: \r\n\r\n{0}".format(final))

    
    return render(request,'index.html')  
