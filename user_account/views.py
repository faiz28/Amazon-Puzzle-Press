from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q



# Create your views here.
def register(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                username=request.POST['username']
                user=User.objects.filter(Q(username=username))
                useremail = request.POST['email']
                email=User.objects.filter(Q(email=useremail))
                if user.count()==1:
                    return render(request,'signup.html',{'error':'Username Already Exists'})
                else:
                    if email.count()==1:
                        return render(request,'signup.html',{'error':'Email Already Exists'})
                    else:
                        user=User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'], first_name=request.POST['first_name'])
                        user.save()
                        usersss=userinfo.objects.create(username=request.POST['username'],fullname=request.POST['first_name'])
                        usersss.save()
                        socialsss=student_data.objects.create(username=request.POST['username'])
                        socialsss.save()
                        auth.login(request,user)
                        return redirect('home')
                    
                
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'], first_name=request.POST['first_name'])
                user.save()
                usersss=userinfo.objects.create(username=request.POST['username'],fullname=request.POST['first_name'])
                usersss.save()
                socialsss=student_data.objects.create(username=request.POST['username'])
                socialsss.save()
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'signup.html',{'error':'Password Does not match'})
    else:
        return render(request,'signup.html')
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

