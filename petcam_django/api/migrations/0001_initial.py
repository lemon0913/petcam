# Generated by Django 3.2.6 on 2021-10-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('reg_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='등록일')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='수정일')),
            ],
        ),
    ]
