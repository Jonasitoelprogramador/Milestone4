# Generated by Django 3.2 on 2022-01-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20210921_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_category', models.CharField(max_length=100)),
                ('account_type', models.CharField(choices=[('host', 'host'), ('worker', 'worker')], max_length=6)),
            ],
        ),
    ]