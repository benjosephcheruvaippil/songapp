# Generated by Django 4.0.3 on 2022-04-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_song_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songdetail',
            name='song_text',
            field=models.TextField(default=''),
        ),
    ]