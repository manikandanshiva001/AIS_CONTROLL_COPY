# Generated by Django 4.2.7 on 2023-12-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ais', '0016_ais_approvedbyhoddate_ais_approvedbyproductiondate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ais',
            name='ApprovedByHoddate',
            field=models.DateTimeField(default='18ates', verbose_name='date time '),
        ),
        migrations.AlterField(
            model_name='ais',
            name='ApprovedByProductiondate',
            field=models.DateTimeField(default='18ates', verbose_name='date time '),
        ),
        migrations.AlterField(
            model_name='ais',
            name='ApprovedByQUAdate',
            field=models.DateTimeField(default='18ates', verbose_name='date time '),
        ),
        migrations.AlterField(
            model_name='ais',
            name='ApprovedBypeddate',
            field=models.DateTimeField(default='18ates', verbose_name='date time '),
        ),
    ]
