# Generated by Django 3.2.6 on 2021-08-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturlsapp', '0002_alter_shortlinks_redirect_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlinks',
            name='rnd_key',
            field=models.CharField(max_length=15),
        ),
    ]
