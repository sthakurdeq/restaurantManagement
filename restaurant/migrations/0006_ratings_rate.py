# Generated by Django 3.2 on 2022-08-01 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0005_remove_ratings_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="ratings",
            name="rate",
            field=models.JSONField(null=True),
        ),
    ]
