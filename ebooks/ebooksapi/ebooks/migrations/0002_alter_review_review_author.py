# Generated by Django 5.1.2 on 2024-10-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_author',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]