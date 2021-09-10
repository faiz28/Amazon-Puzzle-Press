import PyPDF2
pdfFileObj = open('./Proust-1.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages
print("number of pages",pages)


f = open('./worddd/fileee1.txt', 'w')
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
                                    f = open('./worddd/fileee'+str(pdf_num)+'.txt', 'w')
                                    
                                
                        word=""
                print("pdf number",pdf_num)
                
        # For Seprating the Pages
        print()
# closing the pdf file object
pdfFileObj.close()
