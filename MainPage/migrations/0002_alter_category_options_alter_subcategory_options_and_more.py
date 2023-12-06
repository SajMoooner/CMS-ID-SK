# Generated by Django 4.0 on 2023-11-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['category__name', 'name'], 'verbose_name': 'Subcategory', 'verbose_name_plural': 'Subcategories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
