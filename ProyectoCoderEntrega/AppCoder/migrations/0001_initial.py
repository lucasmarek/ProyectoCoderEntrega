# Generated by Django 3.2.13 on 2022-08-14 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('fechaIngreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Platos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precioArg', models.IntegerField()),
                ('aptoCeliaco', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=50)),
                ('fechaApertura', models.DateField()),
                ('calificacion', models.DecimalField(decimal_places=0, max_digits=1)),
            ],
        ),
    ]
