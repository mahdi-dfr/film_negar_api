# Generated by Django 4.2.11 on 2024-05-09 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_alter_movie_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(choices=[('0', 'اکشن'), ('1', 'انیمیشن'), ('2', 'درام'), ('3', 'ماجراجویی'), ('4', 'سایر')], default='4', max_length=1, verbose_name='ژانر فیلم'),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie_genre', to='movie.genre', verbose_name='ژانر'),
        ),
    ]
