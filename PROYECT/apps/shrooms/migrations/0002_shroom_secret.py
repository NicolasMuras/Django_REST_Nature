# Generated by Django 3.1.6 on 2021-02-09 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shroom',
            name='secret',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
