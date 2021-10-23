# Generated by Django 3.2 on 2021-09-21 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
        ('users', '0011_auto_20210921_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminuser',
            name='role',
        ),
        migrations.AddField(
            model_name='adminuser',
            name='branch',
            field=models.ForeignKey(default='سیرجان', on_delete=django.db.models.deletion.CASCADE, to='branches.branch', verbose_name='شعبه'),
            preserve_default=False,
        ),
    ]
