# Generated by Django 2.0 on 2017-12-26 10:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='date_added',
            new_name='date_updated',
        ),
        migrations.AddField(
            model_name='entry',
            name='price',
            field=models.DecimalField(decimal_places=2, default=django.utils.timezone.now, max_digits=10),
            preserve_default=False,
        ),
    ]
