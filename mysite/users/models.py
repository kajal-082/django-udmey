from django.db import models
from django.contrib.auth.models import User
# Create your models here

#we are not inherting from the user model we are creating profile model and link it with user model 
# whenever we make models we have to do migrations and also you have to register the model inside admin.py
class Profile(models.Model):
    #one to one relationship btw profile and user
    # this feild will build one to one rel btw user and profile , we want to connect user feild of profile model with User model 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #on deleting a user a related profile is also deleted 
    image = models.ImageField(default='profile.jpg',upload_to='profile_pictures')
    # wheever your are using an image feild you have to use third party lib called pillow
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username