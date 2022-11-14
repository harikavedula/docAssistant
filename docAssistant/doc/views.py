from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def login(request):
    if request.method=="POST":
        user_email=request.POST['mail']
        user_pwd=request.POST['pswd']
        lo=Login.objects.all()
        h=0
        # print(user_email)
        # print(user_pwd)
        # print(len(l0))
        for x in lo:
            # print(x.email)
            # print(x.pswd)
            if x.email==user_email and x.pswd==user_pwd:
                # print(1)
                request.session['email']=user_email
                if x.doc=="1":
                    
                    h=1
                else:
                    h=2
        if h==1:
            # print(1)
            print("Hii")
            return redirect('profile/')
        if h==2:
            return redirect('vitals/')
        else:
            return redirect('login/')
    return render(request,'login.html')

def profile(request):
    
    return render(request,'profile.html')

def vitals(request):
    return render(request,'table.html')