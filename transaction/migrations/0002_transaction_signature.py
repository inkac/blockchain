# Generated by Django 2.2b1 on 2019-03-13 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='signature',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
