from django.db import models
from django.contrib.auth.models import User
from datetime import timezone
# Create your models here.



categories_name = (
    ("development","development"),
    ("Design","Design"),
    ("It","It"),
    ("Marketing","Marketing"),
)

class Course(models.Model):
    name = models.CharField(max_lenght=100)
    subtitle = models.CharField(max_lenght=500)
    description = models.TextField(max_lenght=2000)
    price = models.FloatField()
    categorie = models.CharField(choices=categories_name)

    def __str__(self):
        return self.name
    

    



class Reviwes(models.Model):
    user = models.ForeignKey(User ,related_name="review_user" , on_delete=models.SET_NULL , null= True)
    course = models.ForeignKey(Course , related_name="course_review" , on_delete=models.CASCADE)
    review = models.CharField(max_lenght=200)
    create_at = models.DateTimeField(default=timezone())



