# Generated by Django 3.1 on 2020-09-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupchatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmessage',
            name='message_text',
            field=models.CharField(max_length=500),
        ),
    ]