from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class MyModel(models.Model):
# 	#id=models.CharField(max_length=200)
# 	name=models.CharField(max_length=200)
#         #user_id=models.CharField(max_length=50)
#         class Meta:
#              db_table = 'Users'


class Game(models.Model):
       game_name=models.CharField(max_length=50)


class GameAttempt(models.Model):
       user_id=models.ForeignKey(User)
       game_id=models.ForeignKey(Game)
       attempt_date=models.DateTimeField(auto_now=True)
       score=models.IntegerField(default=0)

       
class User_Images(models.Model):
       user_id=models.ForeignKey(User)
       image_path=models.ImageField(upload_to='static')


