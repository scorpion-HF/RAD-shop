# Generated by Django 3.2 on 2021-09-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('2', 'مدیر سیرجان'), ('3', 'مدیر بندرعباس'), ('4', 'مدیر تهران'), ('5', 'مدیر رشت'), ('0', 'مدیر کشور'), ('1', 'مشتری')], default='1', max_length=1, verbose_name='نقش'),
        ),
    ]
