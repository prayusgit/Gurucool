from django.shortcuts import render, redirect

# forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# others
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('accounts:register')
    context = {
        'form': form,

    }
    return render(request, 'accounts/register.html', context)


def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.user.is_authenticated:
        return redirect('accounts:logout')
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('library:library-view')
    context = {
        'form': form,
        'label': 'Login',
        'form_name': 'Login'
    }
    return render(request, 'accounts/auth-form.html', context)


@login_required
def logout_view(request, *args, **kwargs):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
    context = {
        'label': 'Yes, Sure',
        'form_name': 'Logout'
    }
    return render(request, 'accounts/auth-form.html', context)
