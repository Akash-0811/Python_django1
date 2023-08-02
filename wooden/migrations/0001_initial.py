# Generated by Django 3.2.20 on 2023-08-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=50)),
                ('description', models.TextField(default='Its too yummy')),
                ('image', models.ImageField(upload_to='images')),
                ('order_status', models.BooleanField(default=False)),
                ('items', models.IntegerField(default=0)),
            ],
        ),
    ]