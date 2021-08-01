from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.

from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
