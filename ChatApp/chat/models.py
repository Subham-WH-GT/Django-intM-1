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


# class privateChat(models.Model):
    
#     content=models.CharField(max_length=10000)
#     timestamp=models.DateTimeField(auto_now=True)
#     user=models.ForeignKey('private',on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.user.user


# class private(models.Model):
#     user=models.CharField(max_length=30)
    
#     def __str__(self):
#         return self.user
    

