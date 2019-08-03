from django.db import models

# Create your models here.
class UserGroup(models.Model):
    title = models.CharField(max_length=32)


class Userinfo(models.Model):
    user_type_choices = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP'),
    )
    # 注意,这里有一个 choices
    # choice Foreignkey 都可以通过　source 来指定
    user_type = models.IntegerField(choices=user_type_choices)
    group = models.ForeignKey('UserGroup', on_delete=models.CASCADE)

    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)

    roles = models.ManyToManyField('Role')

class UserToken(models.Model):
    user = models.OneToOneField(to='Userinfo', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

class Role(models.Model):
    title = models.CharField(max_length=32)