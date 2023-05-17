from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import Profileform


# Create your views here.
@login_required(login_url='login')
def U_form(request):

    # form = Profileform()
    if request.method == "POST":
        p_form = Profileform(request.POST, request.FILES)
        if p_form.is_valid():
            data = p_form.save(commit=False)
            data.user = request.user
            print(data.user)
            data.save()
            messages.success(
                request, f'Data added sucessfully to {data.user}')
            return redirect('r')
        else:
            return HttpResponse("<h1>not going throuhg</h1>")

    else:
        context = {'form': Profileform}
        return render(request, 'profile/profileform.html', context)


@login_required(login_url='login')
def Home(requests):
    return render(requests, 'index.html')


def Signup(request):
    length = 8
    v = 9

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exist')
                return redirect('r')

            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already exist')
                return redirect('r')

            elif password.isdigit():
                messages.info(request, "password shouldn't be digit only")
                return redirect('r')

            elif len(password and c_password) < length:
                messages.info(request, "passowrd is too short!")
                return redirect('r')

            else:
                save_user = User.objects.create_user(
                    username=username, email=email, password=c_password)
                save_user.save()
                return redirect('l')

        else:
            messages.error(request, 'passwords do no match')

            return render('r')

    return render(request, 'registration/register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        auth_user = auth.authenticate(username=username, password=password)

        if auth_user is not None:
            auth.login(request, auth_user)
            return redirect('h')
        else:
            messages.error(request, "invalid credentials")

            return redirect('l')
    return render(request, 'registration/login.html')


@login_required(login_url='login')
def Logout(request):
    auth.logout(request)
    return redirect('r')


def Profile(request):
    return render(request, 'profile/user_profile.html')
