from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm,RegisterForm
from django.http import HttpResponseForbidden

# Create your views here.

def home(request):
   return render(request,'home.html')


#TO login without creating a django form 
# def login_view(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
    
#    # Check if a user with provided with username exists
#         if not User.objects.filter(username=username).exists():
#           messages.error(request,' Username Already Exists!')
#           return redirect('login')
    
#         user= authenticate(username=username,password=password)
 
#         if user is None:
#          # Display an error message if authentication fails (invalid password)
#             messages.error(request,'Invalid Password')
#             return redirect('login')
#         else:
#             login(request,user)
#             return redirect('home')

#     return render(request,'login.html')   

# def register_view(request):
#     if request.method=='POST':
#         first_name= request.POST.get('first_name')
#         last_name=request.POST.get('last_name')
#         username=request.POST.get('username')
#         password=request.POST.get('password')

#         # TO check user exists
#         user = User.objects.filter(username=username)

#         if user.exists():
#              messages.info(request,'User already exists')
#         else:
#             user=User.objects.create_user(
#                 first_name=first_name,
#                 last_name=last_name,
#                 username=username,
#             )

#             user.set_password(password)
#             user.save()
#             messages.info(request,'Account created')
#             return redirect('register')
#     return render(request,'register.html')

# @login_required
# def logout_view(request):
#         logout(request)
#         messages.info(request,'You have been logout')
#         return redirect('login')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():  # form validates that username and password are present
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()  # excutes this if method is Get request and return empty fields

    return render(request, 'login.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                messages.error(request, 'Passwords do not match')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                messages.success(request, 'Account created successfully')
                return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def protected_view(request):
    if not request.user.has_perm('EmailApps.can_view_protected'):
        return HttpResponseForbidden("You are not authorized")
    return render(request, 'protected.html')


# from django.contrib.auth.decorators import permission_required
# It is strict
# @permission_required('EmailApps.can_view_protected', raise_exception=True)
# def protected_view(request):
#     if not request.user.is_authenticated: 
#         return redirect('login')  
#     user = User.objects.all() 
#     return render(request, 'protected.html', {'user': user})


@login_required
def logout_view(request):
    logout(request) # clears the session 
    messages.success(request, "You have been logged out successfully.") 
    return redirect('login') # redirect to your login page



from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render

@login_required
def user_list_view(request):
    users = User.objects.all().order_by('-date_joined') # newest first 
    return render(request, 'list.html', {'users': users})


