# Generated by Django 3.2.4 on 2021-06-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_rename_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='author',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
    ]
