# Generated by Django 5.0.6 on 2024-06-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0003_rename_formed_organization_opened'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='elevator',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='construction',
            name='parkinglot',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='construction',
            name='playground',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
