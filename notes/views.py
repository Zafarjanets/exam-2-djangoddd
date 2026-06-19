from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Contact

@login_required
def contact(request):
    contact=Contact.objects.filter(user=request.user)
    return render(request, 'contact.html',{'contact':contact})

def create_notes(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        img = request.FILES.get('img')
        
        if not name or not phone or not img:
            return render(request, 'create.html', {'error':'all fields necessary'})
        
        note = Contact.objects.create(
            name=name,
            phone=phone,
            img=img
            user = request.user
        )

        return redirect('notes')
    
    return render(request, 'create.html', {'note':'Create Notes'})


@login_required
def update_note(request, pk):
    note = Contact.objects.get(pk=pk)
    if request.user!=note.user:
        return render(request, 'create.html', {'error':'You dont have permession'})

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        img = request.FILES.get('img')
        if not name or not phone or not img:
            return render(request, 'create.html', {'error':'all fields necessary'})
        
        if request.user==note.user:
            note.name = name
            note.phone = phone
            note.img=img
            note.save()

            return redirect('notes')
    
    return render(request, 'create.html', {'name':'Update Notes', 'note':note})

        

@login_required
def delete_note(request, pk):
    
    note = Contact.objects.get(pk=pk)
    if request.user!=note.user:
        return render(request, 'delete.html', {'error':'You dont have permession'})

    if request.method=='POST':
        if request.user == note.user:
            note.delete()
            return redirect('notes')
    
    return render(request, 'delete.html', {'note': note})
        
        