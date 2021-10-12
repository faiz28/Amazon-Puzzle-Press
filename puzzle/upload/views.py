from django.shortcuts import redirect, render
from .forms import Up_fileForm
from django.utils.datastructures import MultiValueDictKeyError
from .models import Up_file

# Create your views here.
def upload(request):
    if request.method == 'POST' :
        try:
            form = Up_fileForm(request.POST , request.FILES )
            if form.is_valid():
                form.save()
            myfile = request.FILES['file_upload']
            filename =myfile.name
            pdf_file = Up_file.objects.last()
            
            return render(request, 'upload.html', {'form':form,'filename':filename,'pdf_file':pdf_file})
        except MultiValueDictKeyError:
            myfile = False
    else:
        form=Up_fileForm()
        pdf_file = Up_file.objects.last()
        return render(request,'upload.html',{'form':form,'pdf_file':pdf_file})  

