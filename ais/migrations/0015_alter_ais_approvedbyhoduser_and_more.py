# Generated by Django 4.2.7 on 2023-12-16 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ais', '0014_alter_ais_approvedbyhoduser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ais',
            name='ApprovedByHodUser',
            field=models.CharField(default='HOD', max_length=100),
        ),
        migrations.AlterField(
            model_name='ais',
            name='ApprovedByProductionUser',
            field=models.CharField(default='PRODUCTIO', max_length=100),
        ),
        migrations.AlterField(
            model_name='ais',
            name='ApprovedByQUAUser',
            field=models.CharField(default='QUALITY', max_length=100),
        ),
        migrations.AlterField(
            model_name='ais',
            name='ApprovedBypedUser',
            field=models.CharField(default='PED', max_length=100),
        ),
    ]
