# Generated by Django 3.1.6 on 2021-02-09 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specie', models.CharField(max_length=50)),
                ('days', models.SmallIntegerField()),
                ('cap_color', models.CharField(max_length=20)),
                ('trunk_color', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Specimen',
                'verbose_name_plural': 'Specimens',
            },
        ),
    ]
