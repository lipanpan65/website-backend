from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


# https://www.cnblogs.com/thinkingtouch/articles/13758109.html

# class UserInfo(AbstractBaseUser):
class UserInfo(models.Model):
    STATUS_DISABLE = 0
    STATUS_ENABLE = 1
    STATUS = (
        (STATUS_DISABLE, u'禁用'),
        (STATUS_ENABLE, u'可用'),
    )
    ROLE_RD = 0
    ROLE_DBA = 1

    ROLE = (
        (ROLE_RD, u'普通用户'),
        (ROLE_DBA, u'管理员'),
    )

    id = models.AutoField('id', primary_key=True, help_text='自增主键')
    username = models.CharField('username', max_length=50, unique=True, help_text='用户名')
    name = models.CharField('name', max_length=50, null=True, default=None, help_text='姓名')
    email = models.CharField('email', max_length=50, null=True, default=None, help_text='邮箱')
    phone = models.CharField('phone', max_length=50, null=True, default=None, help_text='联系电话')
    last_login = None
    backend = 'django.contrib.auth.backends.ModelBackend'

    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = username.verbose_name
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'tb_userinfo'

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
