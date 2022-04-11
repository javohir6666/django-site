from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import News, Category, Tag
# Create your views here.
def index(request):
    first_news = News.objects.first()
    three_news = News.objects.all()[1:3]
    return render(request, 'index.html', {
        'first_news' : first_news,
        'three_news' : three_news,
    })

class PostDetail(DetailView):
    model = News
    template_name = 'blog_post.html'