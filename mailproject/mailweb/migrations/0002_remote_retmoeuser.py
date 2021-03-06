# Generated by Django 3.0.1 on 2020-01-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remote',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('local_ip', models.CharField(blank=True, max_length=50, null=True)),
                ('system_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'remote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RetmoeUser',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('user_ip', models.CharField(max_length=50, unique=True)),
                ('user_name', models.CharField(max_length=200)),
                ('user_system', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'retmoe_user',
                'managed': False,
            },
        ),
    ]
