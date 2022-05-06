# Generated by Django 4.0.3 on 2022-05-06 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='new_image/'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='new_image/'),
        ),
        migrations.AlterField(
            model_name='headline',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='new_image/'),
        ),
        migrations.AlterField(
            model_name='lifestyle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='new_image/'),
        ),
        migrations.AlterField(
            model_name='post1',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='new_image/'),
        ),
        migrations.AlterField(
            model_name='trending',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='new_image/'),
        ),
    ]
