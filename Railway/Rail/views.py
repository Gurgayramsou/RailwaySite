from ast import Return
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate,login,decorators
from django.contrib.auth.models import User
import random
from django.contrib import sessions
# Create your views here.
#Login authentication view
def index(request):
    if request.method=='POST':
        name = request.POST["uname"]
        pw = request.POST['pw']
        capt = int(request.POST['capt'])
        user = authenticate(request,username = name , password = pw)
        # if False:
        #     errorMsg = 'Captcha doesnt match, please try again!!'
        #     content={'errorMsg':errorMsg}
        #     return render(request,'loginError.html',content)
        
        if user is not None:
            login(request,user)
            return redirect('/home/')
        else:
            errorMsg = "User doesn't exist!!"
            content={'errorMsg':errorMsg}
            return render(request,'loginError.html',content)
    if request.method=='GET':
       num= random.randint(1000,10000)
       content = {'num':num}
       templateName = 'index.html'
       return render(request,templateName,content)


@decorators.login_required
def Home(request):
    return HttpResponse('welcome')


def login_errors(request):
    content = {}
    templateName = 'loginError.html'
    return render(request,templateName)

def registerUser(request):
    if request.method=='POST':
        name = request.POST['uname']
        email = request.POST['email']
        pw = request.POST['pw']
        rpw = request.POST['rpw']
        accepted = request.POST.get('accepted',False)
        if pw!=rpw and accepted=='on':
           errorMsg = 'password did not match!!'
        else:
           try:
               user = User.objects.create_user(username=name,
                                 email=email,
                                 password=pw)
               errorMsg ='Registration successful!!'
           except:
               errorMsg = "Coudn't create user, Try again!"
        content={'errorMsg':errorMsg}
        return render(request,'loginError.html',content)
    content = {}
    templateName = 'registerUser.html'
    return render(request,templateName,content)