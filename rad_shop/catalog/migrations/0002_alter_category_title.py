# Generated by Django 3.2.4 on 2021-07-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='عنوان دسته بندی'),
        ),
    ]
