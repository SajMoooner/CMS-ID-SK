# Generated by Django 4.0 on 2023-11-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlePage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtitle',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
