# Generated by Django 4.1.4 on 2022-12-13 06:02

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_image_productimage_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='path',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 600], upload_to='', verbose_name='Изображение'),
        ),
    ]
