# Generated by Django 5.0.6 on 2024-06-05 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specific_value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specific_value', models.CharField(max_length=20)),
                ('specific', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='app.specific')),
            ],
        ),
        migrations.DeleteModel(
            name='SpecificValue',
        ),
    ]
