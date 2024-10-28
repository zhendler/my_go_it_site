from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # автоматично вхід після реєстрації
            return redirect('home')  # змініть 'home' на ваш основний шлях
    else:
        form = UserRegistrationForm()
    return render(request, 'blogs/register.html', {'form': form})
