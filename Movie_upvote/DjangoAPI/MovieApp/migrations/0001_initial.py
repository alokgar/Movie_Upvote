# Generated by Django 3.1.2 on 2020-10-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('MovieId', models.AutoField(primary_key=True, serialize=False)),
                ('MovieTitle', models.CharField(max_length=100)),
                ('ReleaseDate', models.DateField()),
                ('Upvotes', models.IntegerField(default=0)),
            ],
        ),
    ]
