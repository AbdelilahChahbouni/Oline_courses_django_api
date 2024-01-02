from .models import Course , Reviews , Categories
from rest_framework import serializers



class CourseListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'
    categorie = serializers.StringRelatedField()

class CategoriesListSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Categories
        fields = "__all__"

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(source="course_review" , many=True)
    categorie = serializers.StringRelatedField()
    class Meta:
        model = Course
        fields = ['name' , 'categorie' , 'reviews']


