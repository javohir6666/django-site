# Generated by Django 3.2.7 on 2021-09-12 13:02

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category_image', models.ImageField(upload_to='img/')),
                ('slug', models.SlugField(blank=True, default=models.CharField(max_length=200))),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Color_Buttons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, default=models.CharField(max_length=50))),
            ],
            options={
                'verbose_name_plural': 'Color Buttons',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=35)),
                ('slug', models.SlugField(blank=True, default=models.CharField(max_length=35), max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image_image', models.ImageField(blank=True, upload_to='uploads/img/')),
                ('detail', ckeditor.fields.RichTextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('post_viewcount', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('tags', models.ManyToManyField(blank=True, to='news.Tag')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('comment', ckeditor.fields.RichTextField()),
                ('status', models.BooleanField(default=False)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='rang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.color_buttons'),
        ),
    ]
