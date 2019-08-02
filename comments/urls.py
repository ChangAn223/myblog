
from django.conf.urls import url
from comments import views
# 指定视图函数的别名的时候的有效空间
app_name = 'comments'

urlpatterns = [
    url(r'^blog/(?P<id>\d+)$', views.comment, name="comment"),
]