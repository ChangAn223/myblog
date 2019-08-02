from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Article, Category


def get_recent_article(num=4):
    # 返回的是列表， 所以通过切片获取前4篇博客;
    return Article.objects.order_by('-create_time')[:num]


def get_archives():
    # dates方法或i返回一个列表， 列表中的元素为每篇文章的创建时间， 精确到月， 并且是降序显示
    return Article.objects.dates(field_name='create_time', kind='month', order='DESC')


def index(request):
    # articles = Article.objects.all().order_by('create_time')
    # show = articles[:8]
    # return render(request,'blog/music.html',context={"articles": show, })
    paginator = Paginator(Article.objects.all(), 8)
    page = request.GET.get('page')
    try:
        paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        articles = paginator.page(1)
    else:
        articles = paginator.page(page)
    recent = get_recent_article()
    python = Article.objects.filter(category=1).order_by('-create_time')[:6]
    linux = Article.objects.filter(category=5).order_by('-create_time')[:6]
    suanfa = Article.objects.filter(category=9).order_by('-create_time')[:6]
    database = Article.objects.filter(category=8).order_by('-create_time')[:6]
    net = Article.objects.filter(category=4).order_by('-create_time')[:6]
    return render(request, 'blog/index.html', context={"articles": articles, "recent": recent, "python": python, "linux": linux,
                                                       "suanfa": suanfa, "database": database, "net": net})


def day(request):
    return render(request, 'day/index.html', context={})


def about(request):
    return render(request, 'about.html')


def music(request):
    return render(request, 'music.html')


def search(request):
    key = request.POST.get("keyboard")
    articles = Article.objects.filter(title__icontains=key).all()
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        articles = paginator.page(1)
    else:
        articles = paginator.page(page)
    recent = get_recent_article()
    return render(request, 'search.html', context={"articles": articles, "key": key, "recent": recent})

