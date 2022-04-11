from django.contrib import admin

# Register your models here.
from .models import Category, Comment, News, Tag, Color_Buttons

admin.site.register(Color_Buttons)
admin.site.register(Category)
admin.site.register(Tag)

class AdminNews(admin.ModelAdmin):
    list_display=('title', 'category', 'add_time')
admin.site.register(News, AdminNews)
class AdminComment(admin.ModelAdmin):
    list_display=('news', 'email', 'comment')
admin.site.register(Comment, AdminComment)
