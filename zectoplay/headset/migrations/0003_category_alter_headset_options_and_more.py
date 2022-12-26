# Generated by Django 4.1.3 on 2022-12-05 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('headset', '0002_headset_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='headset',
            options={'ordering': ['-price', 'name'], 'verbose_name': 'Игровая гарнитура', 'verbose_name_plural': 'Игровая гарнитура'},
        ),
        migrations.AlterField(
            model_name='headset',
            name='is_placed',
            field=models.BooleanField(default=True, verbose_name='Размещено'),
        ),
        migrations.AlterField(
            model_name='headset',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='headset',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='headset',
            name='price',
            field=models.IntegerField(default=None, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='headset',
            name='time_add',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='headset',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='headset',
            name='type',
            field=models.CharField(max_length=50, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='headset',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='headset.category'),
        ),
    ]