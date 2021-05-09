# Generated by Django 3.0.7 on 2021-05-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('score', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
