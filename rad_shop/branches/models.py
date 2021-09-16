from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False, primary_key=True, verbose_name='نام شعبه')
    address = models.TextField(null=False, blank=False, verbose_name='آدرس')

    class Meta:
        verbose_name = 'شعبه'
        verbose_name_plural = 'شعبات'

    def __str__(self):
        return 'شعبه {}'.format(self.name)
