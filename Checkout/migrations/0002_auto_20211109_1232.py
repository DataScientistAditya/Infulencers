# Generated by Django 3.2.8 on 2021-11-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification_data',
            name='Gig_Id',
            field=models.IntegerField(blank=True, default=999999999),
        ),
        migrations.AddField(
            model_name='notification_data',
            name='Type',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AlterField(
            model_name='notification_data',
            name='Receiver_id',
            field=models.IntegerField(blank=True, default=999999999),
        ),
    ]