# Generated by Django 4.1 on 2022-09-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarangWishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=50)),
                ('harga_barang', models.IntegerField()),
                ('deskripsi', models.TextField()),
            ],
        ),
    ]
