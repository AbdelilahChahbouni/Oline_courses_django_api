from django.urls import path , include
from .api import CourseListAPI ,  CategorieListAPI , CourseDetailAPI

urlpatterns = [
   
    path('api/list' ,CourseListAPI.as_view()),
    path('api/details/<int:pk>' , CourseDetailAPI.as_view()),
    path('api/cat/', CategorieListAPI.as_view()),

    
]
