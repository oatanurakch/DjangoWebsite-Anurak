# Generated by Django 3.2 on 2021-10-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
