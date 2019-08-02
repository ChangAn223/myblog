
# Create your models here.
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mdeditor.fields import MDTextField# 富文本编辑器

# Create your models here.


class Category(models.Model):
    # Meta 配置Model 属性，在后台这个属性展示的名字
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"
    name = models.CharField(max_length=100, unique=True, verbose_name="分类名")

    def __str__(self):
        return "%s" %(self.name)

    def get_category_url(self):
        return reverse("blog:category", kwargs={"id": self.id})


class Tag(models.Model):
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"
    name = models.CharField(max_length=100, unique=True, verbose_name="标签名")

    def __str__(self):
        return '%s' %(self.name)


class Article(models.Model):
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
        ordering = ['-id']  # 按文章ID排序

    STATUS_ITEMS = (
        (1, '发布'),
        (0, '草稿'),
    )
    title = models.CharField(max_length=100, verbose_name="文章名")
    content = MDTextField(verbose_name="内容", help_text="正文支持MarkDown格式")
    create_time = models.DateTimeField(default=datetime.now(), verbose_name="创建时间")
    status = models.PositiveSmallIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey(Category, null=True,blank=True, on_delete=models.CASCADE, verbose_name="分类名")
    tags = models.ManyToManyField(Tag, null=True, blank=True, verbose_name="标签名")
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE, verbose_name="作者")
    read = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    like_count = models.SmallIntegerField(default=0, verbose_name="点赞数")
    comment_count = models.SmallIntegerField(default=0, verbose_name="评论数")

    def __str__(self):
        return "%s" %(self.title)

    # 构造到当前文章的url
    def get_article_url(self):
        return reverse("blog:detail", kwargs={"id": self.id})

    # 增加浏览量
    def add_read(self):
        self.read += 1
        self.save(update_fields=['read'])   # 只更新read字段

    # 增加点赞数
    def add_like(self):
        self.like_count += 1
        self.save(update_fields=['like_count'])

    # 取消点赞数
    def sub_like(self):
        self.like_count -= 1
        self.save(update_fields=['like_count'])

    # 增加评论数
    def add_comment(self):
        self.comment_count += 1
        self.save(update_fields=['like_count'])


class LikeIp(models.Model):
    class Meta:
        verbose_name = "点赞IP库"
        verbose_name_plural = "点赞IP库"
    ip = models.CharField(max_length=15, verbose_name="点赞IP")
    like_article = models.ManyToManyField(Article, verbose_name="点赞文章")
