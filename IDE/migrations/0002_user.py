# Generated by Django 3.1.6 on 2021-07-21 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IDE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('position', models.CharField(max_length=20)),
            ],
        ),
    ]