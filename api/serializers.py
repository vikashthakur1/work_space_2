# from rest_framework import serializers
# from .models import Movie


from rest_framework import serializers
from .models import Movie
from .models import Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'