from django.shortcuts import redirect, render
from .forms import Up_fileForm
from django.utils.datastructures import MultiValueDictKeyError
from .models import Up_file
import PyPDF2,random,os,glob


def make_file(str_p):
    pdfFileObj = open(str_p,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages = pdfReader.numPages
    print("number of pages",pages)

    dirspot = os.getcwd()
    print("Current Directiory................")
    print(dirspot)
    

    # f = open('./media/file/file1.txt', 'w')
    # wordlist = {}
    # cnt = 0
    # pdf_num = 1
    # for i in range(3,pages):
    # # Creating a page object
    #         pageObj = pdfReader.getPage(i)
    #         # print("page number ",i)
    #         # Extracting text from page
    #         # And splitting it into chunks of lines
    #         text = pageObj.extractText().split("  ")

    #         # file open 
            
    #         for i in range(len(text)):
    #                 word=""
    #                 for single_char in text[i]:
    #                     #make upper case
    #                     if ((single_char>='a' and single_char <='z') or (single_char>='A' and single_char<='Z')):
    #                             word += single_char.upper() 
    #                     else: 
    #                         wordlist[word]=1
    #                         if wordlist[word]==2: 
    #                             continue
    #                         else: 
    #                             wordlist[word] = 2
    #                             if(len(word) >= 6 and len(word)<=12):
    #                                 f.write(word)
    #                                 f.write('\n')
    #                                 # print(word,end="\n")
    #                                 cnt+=1
    #                                 if(cnt == 26):
    #                                     cnt = 0
    #                                     f.close()
    #                                     pdf_num += 1
    #                                     if pdf_num>500:
    #                                         break
    #                                     f = open('./media/file/file'+str(pdf_num)+'.txt', 'w')
    #                         word=""
    # pdfFileObj.close()
    # f.close()


    f = open('./media/file/file1.txt', 'w')
    wordlist = {}
    cnt = 0
    pdf_num = 1
    value = []
    file_on_off=1
    for i in range(1,3):
            # Creating a page object
            pageObj = pdfReader.getPage(i)
            print("page number ",i)
            text = pageObj.extractText().split(" ")
            print(text)
        
            
            for i in range(len(text)):
                    
                    word=""
                    upper_case = text[i].upper()
                    # if str("\n") in upper_case:
                    #     print(upper_case)
                    # upper_case = ''.join(char for char in upper_case if char.isalnum())
                    # print(upper_case)

                    # 

                    
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
                        print(upper_case)
                        if len(upper_case) >= 3 and  len(upper_case) <= 12:
                            if wordlist.get(upper_case)==None:
                                # print(upper_case)
                                f.write(upper_case)
                                f.write('\n')

                                value.append(upper_case)
                                wordlist[upper_case] = 1
                                cnt+=1

                                if(cnt == 26):
                                    cnt = 0
                                    f.close()
                                    pdf_num += 1
                                    if pdf_num>500:
                                        file_on_off = 0
                                        break
                                    else:
                                        file_on_off = 1
                                        f = open('./media/file/file'+str(pdf_num)+'.txt', 'w')



    if pdf_num<500: 
        pdf_num -=1
        f.close()
        f = open('./media/file/file'+str(pdf_num)+'.txt', 'w')

    cnt = 0 
    while(pdf_num<=500):
        ran = random.randint(1,len(value)-1)
        print(ran)
        f.write(value[ran])
        f.write('\n')
        cnt+=1

        if cnt==26:
            cnt = 0
            f.close()
            pdf_num += 1
            if pdf_num<=500: 
                f = open('./media/file/file'+str(pdf_num)+'.txt', 'w')
def  clear_file(str_p):
    # str_p = str_p+"/*.txt"
    for file in glob.glob(str_p):
        print(file)

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
            # clear_file(str_p)
            make_file(str_p)


            

            return redirect('home')
    else:
        form=Up_fileForm()
        pdf_file = Up_file.objects.last()
        return render(request,'upload.html',{'form':form,'pdf_file':pdf_file})  

