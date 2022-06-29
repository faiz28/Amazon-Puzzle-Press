import re
from django.shortcuts import render
from wordsearch.wordsearch_design import *
# Create your views here.
def wordsearch(request):
    return render(request,'wordsearch.html')

def wordsearch_design(request):
    if request.method == 'POST':
        font = request.POST.get('fonts')
        # Word section
        word_font_size = request.POST.get('word_font_size')
        word_left_right = request.POST.get('word_left_right')
        word_up_down = request.POST.get('word_up_down')
        
        # alphabate sections
        alphabate_font_size = request.POST.get('alphabate_font_size')
        alphabate_space_l_r = request.POST.get('alphabate_space_l_r')
        alphabate_space_u_d = request.POST.get('alphabate_space_u_d')
        position_up_down = request.POST.get('position_up_down')
        position_left_right = request.POST.get('position_left_right')
        position_up_down = request.POST.get('position_up_down')
        row = request.POST.get('row')
        col = request.POST.get('col')
        
        design.make_pdf(font,word_font_size,word_left_right,word_up_down,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,position_up_down,position_left_right,row, col)
    # pdf  = "./media/wordsearch/inner_design.pdf"
    # font,word_font_size,word_left_right,word_up_down,alphabate_font_size,alphabate_space_l_r,alphabate_space_u_d,position_up_down,position_left_right,row, col
    inner_design = design.check_path_inner_design()
    return render(request,'design.html',{'inner_design':inner_design})