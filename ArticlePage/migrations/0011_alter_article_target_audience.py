# Generated by Django 4.0 on 2023-11-30 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlePage', '0010_targetaudience_alter_article_target_audience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='target_audience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArticlePage.targetaudience'),
        ),
    ]
