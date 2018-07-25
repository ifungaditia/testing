# Generated by Django 2.0.7 on 2018-07-25 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0006_auto_20180723_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perizinan',
            name='category',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, related_name='perizinan', to='permission.Category'),
        ),
        migrations.AlterField(
            model_name='perizinan',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perizinan', to=settings.AUTH_USER_MODEL),
        ),
    ]