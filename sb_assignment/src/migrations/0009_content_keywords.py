# Generated by Django 3.2.4 on 2021-06-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0008_alter_content_posted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='keywords',
            field=models.CharField(default=[], max_length=255),
            preserve_default=False,
        ),
    ]
