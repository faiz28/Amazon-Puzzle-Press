# !/usr/bin/python
import sys
from Sudoku.Generator import *
from fpdf import FPDF
from PIL import Image, ImageDraw
import turtle




# setting difficulties and their cutoffs for each solve method
difficulties = {
    'easy': (35, 0), 
    'medium': (81, 5), 
    'hard': (81, 10), 
    'extreme': (81, 15)
}

# getting desired difficulty from command line
difficulty = difficulties['easy']

# constructing generator object from puzzle file (space delimited columns, line delimited rows)
for i in range(2):
    gen = Generator('base.txt')

    # applying 100 random transformations to puzzle
    gen.randomize(100)

    # getting a copy before slots are removed
    initial = gen.board.copy()

    # applying logical reduction with corresponding difficulty cutoff
    # print(difficulty[0],end= "   difficulty 0\n")

    gen.reduce_via_logical(difficulty[0])
    # catching zero case
    if difficulty[1] != 0:
        # applying random reduction with corresponding difficulty cutoff
        gen.reduce_via_random(difficulty[1])

    # getting copy after reductions are completed
    final = gen.board.copy()

    print(i+1)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = "GeeksforGeeks", ln = 1, align = 'C')
    pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",ln = 2, align = 'C')
   
 
    t = turtle.Turtle()
    t.fillcolor('blue')
    t.begin_fill()
    for i in range(4):
        pdf = t.forward(150)
        pdf = t.right(90)
    t.end_fill()
    pdf.output("GFG.pdf")   

   

    # printing out complete board (solution)
    print("The initial board before removals was: \r\n\r\n{0}".format(initial))

    # printing out board after reduction
    print("The generated board after removals was: \r\n\r\n{0}".format(final))
