# Generated by Django 3.2.9 on 2022-04-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]