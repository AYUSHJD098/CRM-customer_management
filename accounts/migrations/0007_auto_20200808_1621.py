# Generated by Django 3.1 on 2020-08-08 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200808_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catrgory',
            new_name='category',
        ),
    ]
