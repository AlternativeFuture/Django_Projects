# Generated by Django 3.0.5 on 2020-04-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20200424_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='Category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='car',
            name='picture',
            field=models.ImageField(null=True, upload_to='Pictures/'),
        ),
    ]
