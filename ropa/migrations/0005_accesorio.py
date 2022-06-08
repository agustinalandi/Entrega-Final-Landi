# Generated by Django 4.0.4 on 2022-06-08 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ropa', '0004_alter_pedido_options_alter_prenda_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('talle_accesorio', models.IntegerField()),
                ('color_accesorio', models.CharField(max_length=70)),
                ('para_regalo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Accesorio',
                'verbose_name_plural': 'Accesorios',
            },
        ),
    ]
