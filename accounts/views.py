from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def register(request):

    if request.method == 'POST':
        firstname= request.POST['first_name']
        secondname = request.POST['second_name']
        email = request.POST['email']
        usernames = request.POST['username']
        password = request.POST['password']
        passwordc = request.POST['passwordc']
        if password == passwordc :
            if User.objects.filter(username=usernames).exists():
                print('user Taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                return render(request,'register.html')
            else :
                user = User.objects.create_user(username=usernames,password=password,email=email,first_name=firstname,last_name=secondname)
                user.save();

                print('user created')
                return redirect('login')
        else:
            print('Passowrd didnt matched')
            return render(request,'register.html')
    else:
            return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print('Login Failed')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
