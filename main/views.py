from django.http import response
from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News, Category, Tag, Color_Buttons
    
def categorylist(request):
    news = News.objects.all()
    pagename = "Category"
    category = Category.objects.all()
    tag = Tag.objects.all()
    return render(request, 'categories_grid.html', {'pagename': pagename, 'news': news, 'category': category, 'tag': tag})

def home(request):
    pagename = "Home"
    news = News.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    return render(request, 'index.html', {'pagename': pagename, 'news': news, 'category': category, 'tag': tag})

def home2(request):
    pagename = "Home"
    news = News.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    return render(request, 'categories_grid.html', {'pagename': pagename, 'news': news, 'category': category, 'tag': tag})

def about_us(request):
    pagename = "About us"
    return render(request, 'about-us.html', {'pagename': pagename})

def error404(request):
    pagename = "Error 404: Page not found!"
    return render(request, '404.html', {'pagename': pagename})


def contact_us(request):
    pagename = "Contact us"
    return render(request, 'contact-us.html', {'pagename': pagename})

def author_page(request):
    pagename = "Author page"
    return render(request, 'author.html', {'pagename': pagename})


