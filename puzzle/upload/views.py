from django.shortcuts import redirect, render
from .forms import Up_fileForm
from django.utils.datastructures import MultiValueDictKeyError
from .models import Up_file
import PyPDF2,random,os,glob
from django.contrib.auth.decorators import login_required
from os import listdir
from os.path import isfile, join
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


def make_file(str_p ,min_char,max_char,start_page,end_page,Num_of_word,Num_of_file):
    pdfFileObj = open(str_p,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages = pdfReader.numPages

    
    print("number of pages",pages)

    dirspot = os.getcwd()
    print("Current Directiory................")
    print(dirspot)

    f = open('./media/file/file1.txt', 'w')
    wordlist = {}
    cnt = 0
    pdf_num = 1
    value = []
    file_control=1
    for i in range(start_page,end_page):
            # Creating a page object
            pageObj = pdfReader.getPage(i)
            # print("page number ",i)
            text = pageObj.extractText().split(" ")
        
            
            for i in range(len(text)):
                    
                    word=""
                    upper_case = text[i].upper()
                    

                    
                    check = 0
                    local_word = ''
                    for char in upper_case:
                        if char.isalpha():
                            check = 1
                            local_word += char
                        else:
                            # print("char = %s ,index = %s"%(char,upper_case.index(char)))
                            if check==1 or (char=='\n' and upper_case.index(char)!=0) :
                            
                                # print("dfdfdfdfd %s"%local_word)
                                upper_case = local_word
                                break
                    

                    upper_case=upper_case.replace('\n','')
                    if upper_case.isalpha():
                        if len(upper_case) >= min_char and  len(upper_case) <= max_char:
                            if wordlist.get(upper_case)==None:
                                if file_control==1:
                                    f.write(upper_case)
                                    f.write('\n')

                                value.append(upper_case)
                                wordlist[upper_case] = 1
                                cnt+=1

                                if(cnt == Num_of_word):
                                    cnt = 0
                                    f.close()
                                    pdf_num += 1
                                    if pdf_num>Num_of_file:
                                        file_control = 0
                                        break
                                    else:
                                        file_control = 1
                                        f = open('./media/file/file'+str(pdf_num)+'.txt', 'a')



    if pdf_num<Num_of_file: 
        pdf_num -=1
        f.close()
        f = open('./media/file/file'+str(pdf_num)+'.txt', 'a')

    cnt = 0 
    while(pdf_num<=Num_of_file):
        ran = random.randint(1,len(value)-1)
        f.write(value[ran])
        f.write('\n')
        cnt+=1

        if cnt==26:
            cnt = 0
            f.close()
            pdf_num += 1
            if pdf_num<=Num_of_file: 
                f = open('./media/file/file'+str(pdf_num)+'.txt', 'a')


    pdfFileObj.close()
    


# Create your views here.
def upload(request):
    form=Up_fileForm()
    if request.method == 'POST' :
        
        if request.POST.get("form_type") == 'formOne':
            form = Up_fileForm(request.POST , request.FILES )
            if form.is_valid():
                form.save()
            myfile = request.FILES['file_upload']
            
            pdf_file = Up_file.objects.last()
            
            return render(request, 'upload.html', {'form':form,'pdf_file':pdf_file})

        elif request.POST.get("form_type") == 'formTwo':
            # remove older file
            path = os.path.join(BASE_DIR, 'media/file')
            onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
            for filename in onlyfiles:
                # print(filename  )
                total = path+"/"+filename;
                print(total)
                os.remove(total)
            


            # pdf file location red
            pdf_file = Up_file.objects.last()
            str_p = str(pdf_file.file_upload)
            str_p = "./media/"+str_p
            pdfFileObj = open(str_p,'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            pages = pdfReader.numPages
            # produce file 
            

            # check all position value
          
            end_page = -1
            min_char = int(request.POST.get('mi_c'))
            max_char = int(request.POST.get('mx_c')) 
            start_page = int(request.POST.get('start_pg'))
            end_page = request.POST.get('end_pg')
            Num_of_word = int(request.POST.get('npw'))
            Num_of_file = int(request.POST.get('num_file'))

            if end_page.isalnum():
                end_page = int(end_page)
                if end_page>pages:
                        end_page = pages
            else:
                end_page = pages
            
            pdfFileObj = open(str_p,'rb')
          
            make_file(str_p ,min_char,max_char,start_page,end_page,Num_of_word,Num_of_file)
           

            return render(request, 'upload.html', {'form':form,'pdf_file':pdf_file})
    else:
        
        pdf_file = Up_file.objects.last()
        return render(request,'upload.html',{'form':form,'pdf_file':pdf_file})  

