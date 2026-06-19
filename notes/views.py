from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Contact

@login_required
def contact(request):
    contact=Contact.objects.filter(user=request.user)
    return render(request, 'contact.html',{'contact':contact})
@login_required
def create_note(request,pk):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        img=request.FILET.get('img')
        
        if not name or not phone or not img:
            return render(request,'create.html')
        
        note=Contact.objects.create(
            name=name,
            phone=phone,
            img=img,
            user=request.user
        )
        return  redirect('notes')
    
    return render(request, 'create.html', {'title':'Create Notes'})
        
        
        
        