# Generated by Django 3.0 on 2021-05-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210509_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
