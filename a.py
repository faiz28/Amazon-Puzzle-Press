import PyPDF2
import random
pdfFileObj = open('./Clean Code.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages
print("number of pages",pages)


f = open('./worddd/file1.txt', 'w')
wordlist = {}
cnt = 0
pdf_num = 1
value = []
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

                upper_case=upper_case.replace('\n','')

                
                check = 0
                local_word = ''
                for char in upper_case:
                    if char.isalpha():
                        check = 1
                        local_word += char
                    else:
                        if check==1 :
                            upper_case = local_word
                            break
                

    
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
                                    break
                                f = open('./worddd/file'+str(pdf_num)+'.txt', 'w')


pdfFileObj.close()
