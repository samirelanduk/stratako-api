# Generated by Django 2.2.14 on 2020-12-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.IntegerField(default=None, null=True)),
                ('creation_time', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
                'ordering': ['creation_time'],
            },
        ),
    ]
