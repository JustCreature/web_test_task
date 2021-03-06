# Generated by Django 3.2.6 on 2021-08-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(default=' 1 ')),
                ('status', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
