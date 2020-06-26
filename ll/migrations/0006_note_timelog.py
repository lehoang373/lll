# Generated by Django 3.0.4 on 2020-06-26 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ll', '0005_auto_20200625_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_spent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('notes', models.ManyToManyField(blank=True, to='ll.Note')),
            ],
        ),
    ]