# Generated by Django 3.2 on 2022-07-29 12:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0002_auto_20220729_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='day',
            field=models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THUR', 'Thursday'), ('FRI', 'Friday')], max_length=10),
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('rating', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=10, validators=[django.core.validators.MaxValueValidator(10)])),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_ratings', to='restaurant.menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]