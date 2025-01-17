from django.shortcuts import render, HttpResponse, redirect
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
# Create your views here.
def index(requests):
    return render(requests, "index.html")

def about(request):
    return render(request, "about.html")

def dashboard(request):
    articles = Article.objects.filter(author= request.user)
    context = {
        "articles" : articles
    }
    return render(request, "dashboard.html", context)
def addArticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():

        article=form.save(commit=False)
        article.author = request.user

        article.save()
        messages.success(request, "Makale sisteme yüklenmiştir")
        return redirect("index")

    return render(request, "addarticle.html", {"form": form})