import re
from django.shortcuts import render
from wordsearch.wordsearch_design import *
from wordsearch.wordsearch_design_2 import *
from wordsearch.wordsearch_design_4 import *
from wordsearch.old_puzzle_make import *
from wordsearch.models import puzzleoption
import random
# Create your views here.
def wordsearch(request):
    if request.method == 'POST':
        number_puzzle = request.POST.get('number_puzzle')
        problem_per_page = request.POST.get('problem_per_page')
        one_side = request.POST.get('one_side')
        answer_show = request.POST.get('answer_show')
        
        problem_per_page = design.update_current(problem_per_page)
        rand = random.randint(100000,10000000)
        pdf  =  canvas.Canvas("./media/wordsearch/solution/%d_inner_design.pdf"%rand)   
        solution  =  canvas.Canvas("./media/wordsearch/solution/solution.pdf")
        number_puzzle = int(number_puzzle)
            
        if problem_per_page !=4:
            design2.make_pdf(pdf,rand,solution,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,problem_per_page,0,0,0,0,0,number_puzzle,0)
        else:
            design4.make_pdf(pdf,rand,solution,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,problem_per_page,0,0,0,0,0,0,number_puzzle,0)

    
    inner_design = design2.check_solution()
    # inner_design = ""
    return render(request,'wordsearch.html',{'inner_design':inner_design})

def wordsearch_design(request):
    if request.method == 'POST':
        font = request.POST.get('fonts')
        # Word section
        word_font_size = request.POST.get('word_font_size')
        word_left_right = request.POST.get('word_left_right')
        word_up_down = request.POST.get('word_up_down')
        word_u_d_s = request.POST.get('word_u_d_s')
        word_l_r_s = request.POST.get('word_l_r_s')
        
        # alphabate sections
        alphabate_font_size = request.POST.get('alphabate_font_size')
        alphabate_space_l_r = request.POST.get('alphabate_space_l_r')
        alphabate_space_u_d = request.POST.get('alphabate_space_u_d')
        alphabate_up_down = request.POST.get('position_up_down')
        alphabate_left_right = request.POST.get('position_left_right')
        alphabate_up_down = request.POST.get('position_up_down')
        row = request.POST.get('row')
        col = request.POST.get('col')
        
        # Rectangle section
        rectangle_left_right = request.POST.get('rectangle_left_right')
        rectangle_up_down = request.POST.get('rectangle_up_down')
        rectangle_left_right_inc = request.POST.get('rectangle_left_right_inc')
        rectangle_up_down_inc = request.POST.get('rectangle_up_down_inc')
        
        # numbering section
        numbering_font_size = request.POST.get('numbering_font_size')
        numbering_left_right = request.POST.get('numbering_left_right') 
        numbering_up_down = request.POST.get('numbering_up_down') 
        number_show = request.POST.get('number_show')
        text_left_right = request.POST.get('text_left_right')
        text_up_down = request.POST.get('text_up_down')
        line_left_right = request.POST.get('line_left_right')
        line_up_down = request.POST.get('line_up_down')
        problem_per_page = request.POST.get('problem_per_page')
        # down puzzle option
        puzzle_up_down = request.POST.get('puzzle_up_down')
        # right puzzle 
        right_puzzle =request.POST.get('right_puzzle')
        
        problem_per_page = design.update_current(problem_per_page)
        
        
        # make pdf file
        rand = random.randint(100000,10000000)
        pdf  =  canvas.Canvas("./media/wordsearch/%d_inner_design.pdf"%rand)   
        if problem_per_page == 2 or problem_per_page==1:
            design2.make_pdf(pdf,rand,"",font,word_font_size,word_left_right,word_up_down,word_u_d_s,word_l_r_s,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,row, col,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,puzzle_up_down,2,1)
        elif problem_per_page == 4:
            design4.make_pdf(pdf,rand,"",font,word_font_size,word_left_right,word_up_down,word_u_d_s,word_l_r_s,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,alphabate_up_down,alphabate_left_right,row, col,rectangle_left_right,rectangle_up_down,rectangle_left_right_inc,rectangle_up_down_inc,numbering_font_size,numbering_left_right,numbering_up_down,number_show,problem_per_page,line_left_right,line_up_down,text_left_right,text_up_down,puzzle_up_down,right_puzzle,4,1)

        
        # problem per page
             
    # pdf  = "./media/wordsearch/inner_design.pdf"
    # font,word_font_size,word_left_right,word_up_down,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,position_up_down,position_left_right,row, col
    inner_design = design2.check_path_inner_design()
    
    return render(request,'design.html',{'inner_design':inner_design})