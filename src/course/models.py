from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



# categories_name = (
#     ("development","development"),
#     ("Design","Design"),
#     ("It","It"),
#     ("Marketing","Marketing"),
# )


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    


class Course(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500)
    description = models.TextField(max_length=2000)
    price = models.FloatField()
    categorie = models.ForeignKey(Categories , related_name="course_categorie" , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    





class Reviews(models.Model):
    user = models.ForeignKey(User ,related_name="review_user" , on_delete=models.SET_NULL , null= True)
    course = models.ForeignKey(Course , related_name="course_review" , on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    create_at = models.DateTimeField(default=timezone.now)



