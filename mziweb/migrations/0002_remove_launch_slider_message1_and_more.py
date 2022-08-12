# Generated by Django 4.0.6 on 2022-08-11 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mziweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='launch',
            name='slider_message1',
        ),
        migrations.RemoveField(
            model_name='launch',
            name='slider_message2',
        ),
        migrations.AddField(
            model_name='launch',
            name='slider1_message',
            field=models.TextField(default='first launch date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='launch',
            name='slider2_message',
            field=models.TextField(default='slider 2 message'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='launch',
            name='launch_date',
            field=models.DateField(),
        ),
    ]