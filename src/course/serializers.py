from .models import Course , Reviews
from rest_framework import serializers



class CourseListSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields = '__all__'


class ReviewsSerializer(serializers.Serializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class CourseDetailSerializer(serializers.Serializer):
    reviews = ReviewsSerializer(source="course_review" , many=True)
    class Meta:
        model = Course
        fields = ['name' , 'categorie' , 'reviews']


