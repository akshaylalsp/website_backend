from django.shortcuts import render,redirect,HttpResponse
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate the user with the provided credentials
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # If authentication is successful, log the user in
                login(request, user)
                print("login sucess")
                return redirect('home')  # Redirect to a specific page after login
            else:
                print("login error")
                form.add_error(None, "Invalid username or password.")  # Add an error if authentication fails
    else:
        print("not post method")

    return render(request, 'login.html')



def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to a login page or a success page
        else:
            print('registration not success')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html') 

def logout_view(request):
    pass