# Generated by Django 4.0 on 2023-12-27 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlePage', '0013_remove_article_article_type_delete_articletype'),
    ]

    operations = [
        migrations.CreateModel(
            name='LifeSituation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('icon_text', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Life Situation',
                'verbose_name_plural': 'Life Situations',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='life_situation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ArticlePage.lifesituation'),
        ),
    ]