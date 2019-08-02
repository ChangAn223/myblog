from django.conf.urls import url
from blog import views as blog_views


# 指定视图函数的别名的时候的有效空间
app_name = 'blog'

urlpatterns = [
    # name 别名，反向获取url时用到
    url(r'^blog/(?P<id>\d+)$', blog_views.detail, name="detail"),
    url(r'^login', blog_views.login),
    url(r'^category$', blog_views.category, name="category_index"),
    url(r'^category/(?P<id>\d+)$', blog_views.category, name="category"),
    url(r'^tag/(?P<id>\d+)$', blog_views.tag, name="tag"),
    url(r'^archives/(?P<year>\d{4})/(?P<month>\d{1,2})$', blog_views.archives, name="archives"),
    url(r'^like/(?P<id>\d+)$', blog_views.like)
]

