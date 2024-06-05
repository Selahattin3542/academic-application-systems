# Generated by Django 4.1.7 on 2023-07-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ondocent', '0005_alter_application_doktora_tezi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='doktora_tezi',
            field=models.FileField(blank=True, null=True, upload_to='tezler1/', verbose_name='tez'),
        ),
        migrations.AlterField(
            model_name='application',
            name='sözlü',
            field=models.FileField(blank=True, null=True, upload_to='sözlüler1/', verbose_name='Sözlü Sınav Sonuç Belgesi'),
        ),
        migrations.AlterField(
            model_name='application',
            name='yds_belge',
            field=models.FileField(blank=True, null=True, upload_to='yds_belgeler1/', verbose_name='YDS Sonuç Belgesi'),
        ),
    ]