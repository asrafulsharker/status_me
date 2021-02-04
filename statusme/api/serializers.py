from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Article
        fields = ['id', 'title', 'description']
  