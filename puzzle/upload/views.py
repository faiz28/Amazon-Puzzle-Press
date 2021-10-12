from django.shortcuts import redirect, render
from .forms import Up_fileForm
from django.utils.datastructures import MultiValueDictKeyError
from .models import Up_file

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
            return redirect('home')
    else:
        form=Up_fileForm()
        pdf_file = Up_file.objects.last()
        return render(request,'upload.html',{'form':form,'pdf_file':pdf_file})  

