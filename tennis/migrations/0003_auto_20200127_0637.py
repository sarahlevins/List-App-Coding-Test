# Generated by Django 3.0.2 on 2020-01-27 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0002_pageviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageviews',
            name='count',
            field=models.IntegerField(),
        ),
    ]
