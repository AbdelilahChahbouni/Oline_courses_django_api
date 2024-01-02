from .models import Course , Reviews , Categories
from .serializers import CourseListSerializer , CourseDetailSerializer , ReviewsSerializer , CategoriesListSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view








class CourseListAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer


class CourseDetailAPI(generics.RetrieveAPIView):
     queryset = Course.objects.all()
     serializer_class = CourseDetailSerializer

class CategorieListAPI(generics.ListAPIView):
      queryset = Categories.objects.all() 
      serializer_class = CategoriesListSerializer