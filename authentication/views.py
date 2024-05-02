from django.shortcuts import render,redirect,HttpResponse
from .forms import UserRegistrationForm

# Create your views here.
def login_view(request):
    return HttpResponse("hello world")


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

    return render(request, 'register_test.html', {'form': form}) 

def logout_view(request):
    pass