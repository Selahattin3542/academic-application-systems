# Generated by Django 4.1.7 on 2023-07-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onprof', '0004_alter_application_doktora_tezi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='eser1',
            field=models.FileField(blank=True, null=True, upload_to='eserler/'),
        ),
        migrations.AlterField(
            model_name='application',
            name='eser2',
            field=models.FileField(blank=True, null=True, upload_to='eserler2/'),
        ),
        migrations.AlterField(
            model_name='application',
            name='eser3',
            field=models.FileField(blank=True, null=True, upload_to='eserler3/'),
        ),
        migrations.AlterField(
            model_name='application',
            name='eser_türü1',
            field=models.CharField(choices=[('A-1a', 'A-1a'), ('A-1b', 'A-1b'), ('A-2a', 'A-2a'), ('C-1', 'C-1')], default='A1-a', max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='eser_türü2',
            field=models.CharField(choices=[('A-1a', 'A-1a'), ('A-1b', 'A-1b'), ('A-2a', 'A-2a'), ('C-1', 'C-1')], default='A2-a', max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='eser_türü3',
            field=models.CharField(choices=[('A-1a', 'A-1a'), ('A-1b', 'A-1b'), ('A-2a', 'A-2a'), ('C-1', 'C-1')], default='A3-a', max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='makale',
            field=models.FileField(blank=True, null=True, upload_to='makaleler/'),
        ),
    ]