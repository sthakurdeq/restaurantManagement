# Generated by Django 3.2 on 2022-07-30 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0004_auto_20220729_1730"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ratings",
            name="rating",
        ),
    ]
