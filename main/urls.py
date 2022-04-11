from django.conf.urls import include, url
from . import views
from django.urls import path
from news.views import PostDetail


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('about/', views.about_us, name='about'),
    url('error404/', views.error404, name='home'),
    url('contacts/', views.contact_us, name='contacts'),
    url('author/', views.author_page, name='author'),
    url('category/', views.home2, name='category'),
    # path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),

]