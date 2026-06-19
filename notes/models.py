from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='zafar')
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    img=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):  
        return f'{self.name} -- {self.phone}'