# Generated by Django 3.0.2 on 2020-01-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.BooleanField()),
            ],
        ),
    ]
