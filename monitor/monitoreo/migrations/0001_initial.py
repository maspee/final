# Generated by Django 4.0.5 on 2022-07-02 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('rut', models.CharField(max_length=12, verbose_name='Rut')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('correo', models.CharField(max_length=50, verbose_name='Email')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Receta')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripción')),
            ],
        ),
    ]
