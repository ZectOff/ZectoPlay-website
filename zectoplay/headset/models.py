from django.db import models


class Headset(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    type = models.CharField(max_length=50, verbose_name='Тип')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото')
    price = models.IntegerField(default=None, verbose_name='Цена')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_placed = models.BooleanField(default=True, verbose_name='Размещено')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игровая гарнитура'
        verbose_name_plural = 'Игровая гарнитура'
        ordering = ['-price', 'name']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
