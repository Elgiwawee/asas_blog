from django.shortcuts import render, redirect
from django.contrib import messages
#from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.utils.translation import activate, gettext_lazy as _

from .form import RegisterUserForm


#def custom_csrf_failure_view(request, reason=""):
    #return HttpResponse(
        #f"CSRF verification failed. Reason: {reason}",
        #status=403
   # )

# register user
@csrf_protect
def register_user(request):
    activate('ar')  # For Arabic language support
    if request.user.is_authenticated:
        messages.info(request, _('You are already registered and logged in.'))
        return redirect('post:index')

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            messages.info(request, _('Thank you for registering. Please log in.'))
            login(request, new_user)
            return redirect('user:login')
        else:
            messages.error(request, _('Please correct the errors below.'))
    else:
        form = RegisterUserForm()
    
    context = {'form': form, 'next': request.GET.get('next', None)}
    return render(request, 'user/register.html', context)


# login user
@csrf_protect
def login_user(request):
    activate('ar')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # authenticate user
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
           # login user
            login(request, user)
            messages.info(request, _('You are now logged in.'))
            next_url = request.GET.get('next', 'post:index')  # Default to 'home' if no 'next' parameter
            return redirect(next_url)
        else:
            messages.error(request, _('Invalid username or password.'))
            return redirect('user:login')
    else:
        return render(request, 'user/login.html', {'next': request.GET.get('post:index')})

# logout user
def logout_user(request):
    activate('ar')
    logout(request)
    messages.info(request, _('You are now logged out, thank you for visiting. We hope to see you again.'))
    return render(request, 'user/logout.html')