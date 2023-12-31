# Generated by Django 5.0 on 2023-12-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uaerId', models.CharField(max_length=30)),
                ('userPassword', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=10)),
                ('birthday', models.CharField(max_length=8)),
                ('gender', models.CharField(max_length=2)),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=11)),
            ],
        ),
    ]
