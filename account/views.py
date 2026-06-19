from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate
from notes.models import Contact

User=get_user_model()

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1!= password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        elif User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        elif not username or not first_name or not last_name or not password1:
            return render(request, 'register.html', {'error': 'All fields are required'})
        else:
            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password1
            )
            return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username, password=password)
        
        if not user:
            return render(request, 'login.html', {'errore':'такого ползователя нету '})
        
        login(request,user=user)
        return redirect('notes')
    return render(request,'login.html')
        
def logout_view(request):
    logout(request)
    return redirect('login')