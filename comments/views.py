from django.shortcuts import render, redirect
from comments.models import *


# Create your views here.


def comment(request, id):
    ar = Article.objects.get(id=id)
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        email = request.POST.get("email")
        content = request.POST.get("content")
        print(nickname,email,content)
        comm = Comment(nickname=nickname, content=content, email=email, article=ar)
        comm.save()
        ar.add_comment()
        return redirect('/blog/%s' % id)
    else:
        return redirect('/blog/%s' % id)
