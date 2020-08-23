from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from django.http import HttpResponse
from django.contrib import messages
from authenticate.forms import SignUpForm,EditProfileForm

# Create your views here.

def home(request):
    return render(request,'authenticate/base2.html',{})

def showbase(request):
    return render(request, 'authenticate/base2.html',{'samurai':'is a garbage car'})

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
             login(request, user)
             fname=user.first_name
             msg='You have been logged In successfully '
             messages.success(request,(msg+fname))
             return redirect('auth:home')
             # return render(request,'authenticate/base2.html',{})

        # Redirect to a success page.

        else:
            messages.success(request,('Error Loggin In!'))
            # Return an 'invalid login' error message.
            return redirect('auth:login')
            ...



    else:
        return render(request,'authenticate/login.html')

def logout_user(request):
    "Logging in a user"
    logout(request)
    messages.success(request,('You have been logged out..'))
    return redirect('auth:home')

def register_user(request):
    "Registerign a user"
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            msg='You have been registered successfully '
            messages.success(request,(msg))
            return redirect ('auth:home')

    else:
        form=SignUpForm()

    context={'form': form}
    return render(request,'authenticate/register.html',context)

def edit_profile(request):
    if request.method=='POST':
        form=EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            msg='Your credentials changed successfully '
            messages.success(request,(msg))
            return redirect ('auth:home')
    else:
        form=EditProfileForm(instance = request.user)
        context={'form':form}

    return render(request,'authenticate/edit_profile.html',context)
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            msg='Your password changed successfully '
            messages.success(request,(msg))
            return redirect ('auth:home')
    else:
        form=PasswordChangeForm(user = request.user)
        context={'form':form}

    return render(request,'authenticate/change_password.html',context)
