from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

from blog.models import Article, ArticleDetail
from blog.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]

    # lookup_url_kwarg = 'id'

    def create(self, request, *args, **kwargs):
        """create posts"""
        # https: // blog.csdn.net / weixin_37989267 / article / details / 85328079
        # data = request.data
        # data._mutable = True
        title = request.data.get("title")
        content = request.data.get("content", "")
        article_detail = ArticleDetail.objects.create(**{"content": content})
        instance = Article.objects.create(**{
            "title": title,
            "article_detail": article_detail
        })
        # 如果被序列化的对象是包含多条的数据的查询集可以通过添加many=True不愁
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """更新文章内容"""
        title = request.data.get("title")
        content = request.data.get("content", "")
        instance = self.get_object()
        instance.title = title
        instance.article_detail.content = content
        instance.article_detail.save()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=["get"], detail=True)
    def publish(self, request, *args, **kwargs):
        """发布文章"""
        instance = self.get_object()
        instance.update(status='publish')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # detail为True，表示路径名格式应该为 book/{pk}/read/
    # detail为False 表示路径名格式应该为 book/latest/
    @action(methods=['GET'], detail=False, )
    def draft(self, request, *args, **kwargs):
        """
        默认创建文章 post 创建文章
        """
        queryset = self.filter_queryset(self.get_queryset().filter(status='draft'))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


"""
  992  echo 1 > /proc/sys/vm/drop_caches
  993  echo 2 > /proc/sys/vm/drop_caches
  994  echo 3 > /proc/sys/vm/drop_caches
"""
