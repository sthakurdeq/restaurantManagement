# Generated by Django 3.2 on 2022-07-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='day',
            field=models.CharField(choices=[('MON', 'Monday'), ('TUE', 'South Indian'), ('WED', 'Wednesday'), ('THUR', 'Thursday'), ('FRI', 'Friday')], max_length=10),
        ),
        migrations.AlterField(
            model_name='menu',
            name='vote',
            field=models.IntegerField(choices=[(-1, 'Dislike'), (0, 'Neutral'), (1, 'Like')]),
        ),
    ]