# Generated by Django 4.0.3 on 2022-09-18 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0006_fileupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fileupload',
            name='create_date',
            field=models.DateTimeField(null=True),
        ),
    ]