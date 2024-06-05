# Generated by Django 4.1.7 on 2023-07-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=20, verbose_name='Ad')),
                ('soyad', models.CharField(max_length=20, verbose_name='Soyad')),
                ('email', models.EmailField(max_length=30, verbose_name='E-mail')),
                ('telefon', models.CharField(max_length=15, verbose_name='Telefon')),
                ('onay', models.FileField(default='', upload_to='docentonay/')),
                ('özgeçmiş', models.FileField(default='', upload_to='docentCV/')),
                ('AYOK', models.FileField(default='', upload_to='docentAYOK/')),
                ('form3', models.FileField(default='', upload_to='docentform3/', verbose_name='FORM-3')),
                ('form4', models.FileField(default='', upload_to='docentform4/', verbose_name='FORM-4')),
                ('tez', models.FileField(default='', upload_to='docenttezler/')),
                ('form7', models.FileField(default='', upload_to='docentform7/', verbose_name='FORM-7(Tez için doldurulması gerekmektedir.)')),
                ('yds', models.FileField(default='', upload_to='docentyds_belge/', verbose_name='YDS Sonuç Belgesi')),
            ],
        ),
    ]