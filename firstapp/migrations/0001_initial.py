# Generated by Django 2.0.1 on 2019-04-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('nick_name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
