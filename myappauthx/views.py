from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def home(request):
    return render(request, "myappauthx/home.html") 

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        #next we have to authenticate the user
        user = authenticate(username = username, password = pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request,"myappauthx/home.html",{'fname': fname})
        else:
            messages.error(request, "bad credentials")
            return render(request, 'myappauthx/signup.html')




    return render(request, "myappauthx/signin.html")

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname  = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #below is for creating a user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your account has been successfully created")
        return redirect('signin')

    return render(request, "myappauthx/signup.html")

def signout(request):
    pass
