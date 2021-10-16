from django.shortcuts import redirect, render
from .forms import Up_fileForm
from django.utils.datastructures import MultiValueDictKeyError
from .models import Up_file
import PyPDF2
import os


def make_file(str_p):
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
    for i in range(26,pages):
    # Creating a page object
            pageObj = pdfReader.getPage(i)
            print("page number ",i)
            # Extracting text from page
            # And splitting it into chunks of lines
            text = pageObj.extractText().split("  ")

            # file open 
            
            for i in range(len(text)):
                    word=""
                    for single_char in text[i]:
                        #make upper case
                        if ((single_char>='a' and single_char <='z') or (single_char>='A' and single_char<='Z')):
                                word += single_char.upper() 
                        else: 
                            wordlist[word]=1
                            if wordlist[word]==2: 
                                continue
                            else: 
                                wordlist[word] = 2
                                if(len(word) >= 6 and len(word)<=12):
                                    f.write(word)
                                    f.write('\n')
                                    # print(word,end="\n")
                                    cnt+=1
                                    if(cnt == 26):
                                        cnt = 0
                                        f.close()
                                        pdf_num += 1
                                        if pdf_num>500:
                                            break
                                        f = open('./media/file/file'+str(pdf_num)+'.txt', 'w')
                            word=""
                    
            # For Seprating the Pages
            print()
    # closing the pdf file object
    pdfFileObj.close()

# Create your views here.
def upload(request):
    if request.method == 'POST' :
        if request.POST.get("form_type") == 'formOne':
            form = Up_fileForm(request.POST , request.FILES )
            if form.is_valid():
                form.save()
            myfile = request.FILES['file_upload']
            filename =myfile.name
            pdf_file = Up_file.objects.last()
            
            return render(request, 'upload.html', {'form':form,'filename':filename,'pdf_file':pdf_file})
        elif request.POST.get("form_type") == 'formTwo':
            # read pdf file
            pdf_file = Up_file.objects.last()

            # for i in pdf_file:
            #     print(i.file_upload)
            str_p = str(pdf_file.file_upload)
            str_p = "./media/"+str_p
            make_file(str_p)

            

            return redirect('home')
    else:
        form=Up_fileForm()
        pdf_file = Up_file.objects.last()
        return render(request,'upload.html',{'form':form,'pdf_file':pdf_file})  

