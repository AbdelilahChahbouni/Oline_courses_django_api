from .models import Course , Reviews , Categories
from .serializers import CourseListSerializer , CourseDetailSerializer , ReviewsSerializer , CategoriesListSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters








class CourseListAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend ,filters.SearchFilter , filters.OrderingFilter]
    filterset_fields = ['price', 'name' , 'categorie']
    search_fields = ['name', 'price']
    ordering_fields = ['price', 'name' ,'categorie']




class CourseDetailAPI(generics.RetrieveAPIView):
     queryset = Course.objects.all()
     serializer_class = CourseDetailSerializer

class CategorieListAPI(generics.ListAPIView):
      queryset = Categories.objects.all() 
      serializer_class = CategoriesListSerializer