# Generated by Django 2.0.3 on 2018-03-30 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180328_0818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addanimal',
            old_name='name',
            new_name='user',
        ),
    ]