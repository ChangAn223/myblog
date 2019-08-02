
# Register your models here.
from django.contrib import admin
from blog.models import Category, Tag, Article
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'article_count')

    def article_count(self,obj):
        return obj.article_set.count()

    def __str__(self):
        return self.name

    article_count.short_description = "文章数量"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def __str__(self):
        return self.name


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 后台列表展示文章时在列表里显示文章的那些属性
    list_display = ('title', 'author', 'category', 'status', 'like_count', 'create_time')
    # 配置那些字段可以作为链接，点击就可进入编辑页面
    list_display_link = ()
    # 过滤，对数据进行筛选，如下设置后可以通过category、author的值来对数据过滤
    list_filter = ('category', 'author')
    # 动作相关配置 是否展示在顶部/底部
    actions_on_bottom = True
    actions_on_top = True
    # 保存、编辑、新建按钮是否在顶部展示
    save_on_top = True

    def __str__(self):
        return self.name

