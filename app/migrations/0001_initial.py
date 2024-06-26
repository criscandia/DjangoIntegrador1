# Generated by Django 3.2 on 2024-06-20 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remeras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('talle', models.IntegerField(choices=[('1', ' Extra Small'), ('2', 'Small'), ('3', 'Medium'), ('4', 'Large'), ('5', 'Extra Large'), ('6', 'Super Extra Large')], default=1)),
                ('color', models.CharField(max_length=100)),
                ('lisa', models.BooleanField(null=True)),
                ('genero', models.IntegerField(choices=[('1', 'Hombre'), ('2', 'Mujer'), ('3', 'Unisex')], default=1)),
            ],
        ),
    ]
