# Generated by Django 3.0.2 on 2020-02-02 10:48

import blog.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last time modified')),
                ('author', models.ForeignKey(on_delete=models.SET(blog.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
