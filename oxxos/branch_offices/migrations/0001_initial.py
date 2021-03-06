# Generated by Django 2.1.7 on 2019-03-18 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Oxxo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=50)),
                ('lng', models.CharField(max_length=50)),
                ('allday', models.BooleanField(default=False)),
                ('beer', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('colony', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch_offices.Colony')),
            ],
        ),
    ]
