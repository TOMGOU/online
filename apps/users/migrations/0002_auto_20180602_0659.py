# Generated by Django 2.0.5 on 2018-06-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='users/%Y/%m', verbose_name='用户头像'),
        ),
    ]