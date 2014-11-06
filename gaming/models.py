from django.db import models

# Create your models here.

class MyModel (model.Model):
	id=models.varchar(max_length=50)
	name=models.varchar(max_length=50)
        #user_id=models.varchar(max_length=50)
        class Meta:
             db_table = 'Users'

class GameAttempt(meodel.Model):
       id=models.varchar(max_length=50)
       user_id=models.varchar(max_length=50)
       game_id=models.varchar(max_length=50)
       attempt_date=models.datetime(max_length=50)
       score=models.varchar(max_length=50)
       
class User_Images(model.Model):
       id=models.varchar(max_length=50)
       user_id=models.varchar(max_length=50)
       image_path=models.varchar(max_length=50)

class Game(model.Model):
       id=models.varchar(max_length=50)
       game_name=models.varchar(max_length=50)
