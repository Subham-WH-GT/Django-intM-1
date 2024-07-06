from django.db import models

# Create your models here.
class Chat(models.Model):
    user=models.CharField(max_length=50,default='Unknown')
    content=models.CharField(max_length=10000)
    timestamp=models.DateTimeField(auto_now=True)
    group=models.ForeignKey('Group',on_delete=models.CASCADE)

class Group(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name    