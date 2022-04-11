from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
#from django.conf import settings
# Create your models here.
#Category posts
class Color_Buttons(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    created_at  = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, default=title, blank=True)

    class Meta:
        verbose_name_plural='Color Buttons'

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='img/')
    slug = models.SlugField(max_length=50, default=title, blank=True)
    #rang = models.CharField(max_length=50, default ='danger')
    rang = models.ForeignKey(Color_Buttons, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title

#TAG
class Tag(models.Model):
    word        = models.CharField(max_length=35)
    slug        = models.SlugField(max_length=250, default=word, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

# Post [News]
class News(models.Model):
    id = models.AutoField
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    image_image = models.ImageField(upload_to='uploads/img/', blank=True)
    detail = RichTextField()
    add_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    post_viewcount = models.PositiveIntegerField(default=0,)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def publish(self):
        self.add_time = timezone.now()
        self.save()

    class Meta:
        verbose_name_plural='News'
        ordering = ['-add_time',]

    def __str__(self):
        return self.title

#COMMENTS
class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    comment = RichTextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment


