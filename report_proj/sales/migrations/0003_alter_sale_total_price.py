# Generated by Django 4.0.1 on 2022-02-01 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_csv_created_alter_csv_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]