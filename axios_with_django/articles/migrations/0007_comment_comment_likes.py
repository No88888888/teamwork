# Generated by Django 3.2.13 on 2022-10-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_likes',
            field=models.ManyToManyField(related_name='comment_likes', to='articles.Article'),
        ),
    ]
