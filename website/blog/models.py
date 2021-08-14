from django.db import models


# Create your models here.
# 字段属性
# https://www.cnblogs.com/lanyinhao/p/9463322.html
class Article(models.Model):
    """
    文章表
    django 之 时间
    auto_now :无论是你添加还是修改对象，时间为你添加或者修改的时间
    auto_now_add：是你当前创建的时间，当你更新对象时时间不会有变法
    create_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    django 之 级联操作
    on_delete=None, # 删除关联表中的数据时,当前表与其关联的field的行为
    on_delete=models.CASCADE, # 删除关联数据,与之关联也删除
    on_delete=models.DO_NOTHING, # 删除关联数据,什么也不做
    on_delete=models.PROTECT, # 删除关联数据,引发错误ProtectedError
    # models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
    on_delete=models.SET_NULL, # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
    # models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
    on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
    on_delete=models.SET, # 删除关联数据,
    a. 与之关联的值设置为指定值,设置：models.SET(值)
    b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)
    django 之 null=true 表示可以为空
    django 之 relate_name 反向查找
    """

    STATUS_PUBLISH = 'publish'
    STATUS_DRAFT = 'draft'

    STATUS_CHOICES = (
        ('draft', '草稿'),
        ('publish', '发表'),
    )

    id = models.AutoField(primary_key=True, help_text='自增主键')
    title = models.CharField(max_length=128, help_text='文章标题')  # null 为 true 表示 可以为空
    status = models.CharField(
        '文章状态',
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft')

    comment_count = models.IntegerField(default=0, verbose_name='评论数')
    up_count = models.IntegerField(default=0, verbose_name='点赞数')
    down_count = models.IntegerField(default=0, verbose_name='踩灭数')
    publish_time = models.DateTimeField(auto_now=True, help_text='发表时间')  # 每次修改对象都会保存当前时间 auto_now = True
    create_time = models.DateTimeField(auto_now_add=True, help_text='草稿创建时间')  # 对象被创建的时候 的 时间
    # user = models.ForeignKey(to='UserInfo', to_field='id', verbose_name='关联作者', on_delete=models.CASCADE)
    article_detail = models.OneToOneField(to='ArticleDetail', to_field='id', help_text="内容详情",
                                          on_delete=models.CASCADE, db_column='article_detail')

    class Meta:
        db_table = 'tb_blog_article'

    def __str__(self):
        return self.title


class ArticleDetail(models.Model):
    id = models.AutoField(primary_key=True, help_text='自增主键')
    content = models.TextField(null=True, help_text='文章内容', )

    class Meta:
        db_table = "tb_blog_article_detail"
