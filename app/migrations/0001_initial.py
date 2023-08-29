# Generated by Django 4.2.4 on 2023-08-16 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('doctorName', models.TextField()),
                ('dob', models.DateField()),
            ],
            options={
                'db_table': 'Patient',
                'unique_together': {('firstName', 'lastName', 'doctorName', 'dob')},
            },
        ),
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcv', models.FloatField()),
                ('mch', models.FloatField()),
                ('mchc', models.FloatField()),
                ('rdw', models.FloatField()),
                ('mcv_prediction', models.TextField()),
                ('mch_prediction', models.TextField()),
                ('mchc_prediction', models.TextField()),
                ('rdw_prediction', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
            options={
                'db_table': 'Predictions',
            },
        ),
    ]