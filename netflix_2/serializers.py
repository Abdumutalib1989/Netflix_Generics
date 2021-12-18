from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import Movie, Actor, Comment

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    def validate_imdb(self, qiymat):
        if qiymat < 2.0:
            raise ValidationError(detail="Bunaqa reytingda kino yo'q")
        return qiymat

class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'movie', 'text']