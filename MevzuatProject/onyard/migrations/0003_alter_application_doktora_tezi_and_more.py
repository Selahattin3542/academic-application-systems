# Generated by Django 4.1.7 on 2023-06-06 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onyard', '0002_alter_application_doktora_tezi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='doktora_tezi',
            field=models.FileField(blank=True, null=True, upload_to='tezler/', verbose_name='Doktora Tezi'),
        ),
        migrations.AlterField(
            model_name='application',
            name='eser',
            field=models.FileField(blank=True, null=True, upload_to='eserler/', verbose_name='Başlıca Eser'),
        ),
        migrations.AlterField(
            model_name='application',
            name='makale',
            field=models.FileField(blank=True, null=True, upload_to='makaleler/', verbose_name='Makale'),
        ),
        migrations.AlterField(
            model_name='application',
            name='yds_belge',
            field=models.FileField(blank=True, null=True, upload_to='yds_belgeler/', verbose_name='YDS sınav sonuç belgesi'),
        ),
    ]