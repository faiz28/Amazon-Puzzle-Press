from django.shortcuts import render
from wordsearch.wordsearch_design import *
# Create your views here.
def wordsearch(request):
    return render(request,'wordsearch.html')

def wordsearch_design(request):
    design.make_pdf()
    print("Hell")
    return render(request,'design.html')