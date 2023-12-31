# Generated by Django 4.2.7 on 2023-12-08 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ais', '0002_remove_reject_1_command'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='REJECT_1',
            new_name='Hod_Reject',
        ),
        migrations.RenameField(
            model_name='ais',
            old_name='reject',
            new_name='RejectdByHod',
        ),
        migrations.RenameField(
            model_name='hod_reject',
            old_name='product_part_number_01',
            new_name='product_part_number',
        ),
        migrations.AddField(
            model_name='ais',
            name='ApprovedByped',
            field=models.BooleanField(default=False, verbose_name='Approved by ped'),
        ),
        migrations.AddField(
            model_name='ais',
            name='RejectByPed',
            field=models.BooleanField(default=False, verbose_name='Approved by ped'),
        ),
        migrations.AddField(
            model_name='ais',
            name='RejectdByProduction',
            field=models.BooleanField(default=False, verbose_name='Approved by production'),
        ),
        migrations.AddField(
            model_name='ais',
            name='RejectdByQUA',
            field=models.BooleanField(default=False, verbose_name='Approved by Quality'),
        ),
        migrations.AddField(
            model_name='ais',
            name='revision_num',
            field=models.CharField(default='1', max_length=1000),
        ),
        migrations.CreateModel(
            name='QUALITY_Reject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_part_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ais.ais')),
            ],
        ),
        migrations.CreateModel(
            name='production_Reject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_part_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ais.ais')),
            ],
        ),
        migrations.CreateModel(
            name='production_Approve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_part_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ais.ais')),
            ],
        ),
        migrations.CreateModel(
            name='PED_Reject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_part_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ais.ais')),
            ],
        ),
    ]
