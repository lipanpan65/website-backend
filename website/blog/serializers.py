# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 2:38 下午
# @Author  : lipanpan03
# @Email  : lipanpan03@58.com
# @File  : serializers.py


from rest_framework.serializers import ModelSerializer

from blog.models import Article, ArticleDetail


class ArticleDetailSerializer(ModelSerializer):
    class Meta:
        model = ArticleDetail
        fields = '__all__'


class ArticleSerializer(ModelSerializer):
    # 如果不添加 read_only=True "This field is required."
    article_detail = ArticleDetailSerializer(read_only=True)
    # article_detail = ArticleDetailSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
