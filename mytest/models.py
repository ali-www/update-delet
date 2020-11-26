from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Po(models.Model):
   
    name = models.CharField(max_length=255)

    photo = models.ImageField(upload_to='cars')
    created_dt = models.DateTimeField(auto_now_add=True,null=1)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=1,blank=1)
    
    def __str__(self):
        return self.name
  
