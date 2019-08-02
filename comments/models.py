
from django.contrib.auth.models import User
from django.db import models
from blog.models import Article
# Create your models here.


class Comment(models.Model):
    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
    nickname = models.CharField(max_length=30, verbose_name="用户名")
    content = models.TextField(verbose_name="评论")
    email = models.EmailField(verbose_name="邮箱")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    # auto_now_add=True
    # 如果修改了内容，自动把字段值更新为修改时的时间
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="文章")

    def __str__(self):
        return '%s' %(self.content[:30])
