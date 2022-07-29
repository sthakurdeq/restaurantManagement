# Generated by Django 3.2 on 2022-07-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='item',
            field=models.ManyToManyField(blank=True, null=True, to='restaurant.Item'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='vote',
            field=models.CharField(choices=[(-1, 'Dislike'), (0, 'Neutral'), (1, 'Like')], default='Dislike', max_length=10),
        ),
    ]