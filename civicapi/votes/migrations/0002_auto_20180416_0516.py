# Generated by Django 2.0.4 on 2018-04-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='ayes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='nays',
            field=models.IntegerField(blank=True),
        ),
    ]
