# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 2:38 下午
# @Author  : lipanpan03
# @Email  : lipanpan03@58.com
# @File  : serializers.py


from rest_framework.serializers import ModelSerializer

from blog.models import Article, ArticleDetail


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
