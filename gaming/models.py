from django.db import models

# Create your models here.
class MyModel (model.Model):
	id=models.varchar(max_length=50)
	image_name=models.varchar(max_length=50)
        user_id=models.varchar(max_length=50)
