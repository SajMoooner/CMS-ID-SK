# Generated by Django 4.0 on 2023-11-12 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MainPage', '0002_alter_category_options_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('main_message', models.CharField(max_length=255)),
                ('target_audience', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='article_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainPage.category')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='subtitle_images/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtitles', to='ArticlePage.article')),
            ],
            options={
                'verbose_name': 'Subtitle',
                'verbose_name_plural': 'Subtitles',
            },
        ),
    ]
