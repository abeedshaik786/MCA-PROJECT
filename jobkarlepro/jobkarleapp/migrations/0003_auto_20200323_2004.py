# Generated by Django 2.2.2 on 2020-03-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobkarleapp', '0002_auto_20200323_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fresherqualification',
            name='Range1',
            field=models.CharField(blank=True, choices=[('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'), ('50', '50'), ('60', '60'), ('70', '70'), ('80', '80'), ('90', '90'), ('100', '100')], max_length=100),
        ),
        migrations.AlterField(
            model_name='fresherqualification',
            name='Range2',
            field=models.CharField(blank=True, choices=[('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'), ('50', '50'), ('60', '60'), ('70', '70'), ('80', '80'), ('90', '90'), ('100', '100')], max_length=100),
        ),
        migrations.AlterField(
            model_name='fresherqualification',
            name='Range3',
            field=models.CharField(blank=True, choices=[('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'), ('50', '50'), ('60', '60'), ('70', '70'), ('80', '80'), ('90', '90'), ('100', '100')], max_length=100),
        ),
        migrations.AlterField(
            model_name='fresherqualification',
            name='Range4',
            field=models.CharField(blank=True, choices=[('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'), ('50', '50'), ('60', '60'), ('70', '70'), ('80', '80'), ('90', '90'), ('100', '100')], max_length=100),
        ),
        migrations.AlterField(
            model_name='fresherqualification',
            name='Range5',
            field=models.CharField(blank=True, choices=[('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'), ('50', '50'), ('60', '60'), ('70', '70'), ('80', '80'), ('90', '90'), ('100', '100')], max_length=100),
        ),
        migrations.AlterField(
            model_name='fresherqualification',
            name='Range6',
            field=models.CharField(blank=True, choices=[('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'), ('50', '50'), ('60', '60'), ('70', '70'), ('80', '80'), ('90', '90'), ('100', '100')], max_length=100),
        ),
    ]