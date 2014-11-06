from django.db import models

# Create your models here.

class MyModel (models.Model):
	#id=models.CharField(max_length=200)
	name=models.CharField(max_length=200)
        #user_id=models.CharField(max_length=50)
        class Meta:
             db_table = 'Users'

class GameAttempt(models.Model):
       #id=models.CharField(max_length=200)
       user_id=models.CharField(max_length=50)
       game_id=models.CharField(max_length=50)
       #attempt_date=models.DateTime(max_length=50)
       score=models.CharField(max_length=50)
       
class User_Images(models.Model):
       #id=models.CharField(max_length=50)
       user_id=models.CharField(max_length=50)
       image_path=models.CharField(max_length=50)

class Game(models.Model):
       #id=models.CharField(max_length=50)
       game_name=models.CharField(max_length=50)
