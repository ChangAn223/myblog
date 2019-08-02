# Create your views here.
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from markdown import markdown
from blog.models import Category, Tag, Article, LikeIp
from comments.forms import *
from django.http import HttpResponse
# Create your views here.


def get_recent_article(num=4):
    # 返回的是列表， 所以通过切片获取前4篇博客;
    return Article.objects.all().order_by('-create_time')[:num]


def detail(request, id):
    article = Article.objects.get(id=id)
    article.content = markdown(article.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',    # markdown语法高亮显示
            'markdown.extensions.toc',   # 允许在文章中自动生成目录
        ],
        output_format="html",)
    article.add_read()  #增加访问量

    comms = article.comment_set.all().order_by('create_time')
    cats = Category.objects.all()
    recent = get_recent_article()
    return render(request, 'blog/detail.html', context={"article": article, "cats": cats,
                                                        "comms": comms, "recent": recent})


def like(request, id):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip,没有真实ip时去获取代理ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    ar = Article.objects.get(id=id)
    like_ip = LikeIp.objects.get_or_create(ip=ip)
    is_like_article = like_ip[0].like_article.filter(id=id)
    print(is_like_article)
    if is_like_article:
        ar.sub_like()
        like_ip[0].like_article.remove(id)
    else:
        like_ip[0].like_article.add(id)
        ar.add_like()
    return HttpResponse(str(ar.like_count))


def login(request):
    if request.method == "GET":
        loginForm = LoginForm()
        loginForm.initial = {"user":'123',"pwd":'www'}
        return render(request, 'login.html', context={"form": loginForm, })
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.user == '123' and form.pwd == '123456':
                return redirect('/')
            else:
                raise ValidationError("帐号或密码错误")
        else:
            return render(request, 'login.html', context={"form": form})


def category(request, id=0):
    if not id:
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(category=id).all()
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        articles = paginator.page(1)
    else:
        articles = paginator.page(page)
    cats = Category.objects.all()
    recent = get_recent_article()
    return render(request, 'category/index.html', context={"articles": articles, "cats": cats, "category_id": id,
                                                           "recent": recent})


def tag(request, id):
    articles = Article.objects.filter(tags=id).all()
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        articles = paginator.page(1)
    else:
        articles = paginator.page(page)
    return render(request, 'blog/index.html', context={"articles": articles})


def archives(request, year, month):
    if int(month) < 10:
        month = '0'+month
    data = year+'-'+month
    articles = Article.objects.filter(
        create_time__startswith=data,
    ).order_by('-create_time')
    return render(request, 'archives/index.html', context={"articles": articles})
