# Generated by Django 5.1 on 2024-08-17 18:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.SmallIntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Expert')], default=0)),
                ('free_time_per_week', models.PositiveSmallIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('reg_number', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('age_limit_from', models.IntegerField(blank=True, null=True)),
                ('age_limit_to', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('gender_limit', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('state', models.CharField(choices=[('P', 'Pending'), ('W', 'Waiting'), ('A', 'Assigned'), ('D', 'Done')], default='P', max_length=1)),
                ('title', models.CharField(max_length=60)),
                ('assigned_benefactor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='charities.benefactor')),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charities.charity')),
            ],
        ),
    ]
