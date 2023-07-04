# Generated by Django 4.1.4 on 2023-02-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0020_person_code_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='seed',
            field=models.PositiveIntegerField(blank=True, help_text='Used as initial ranking to power-pair the first round', null=True, verbose_name='seed'),
        ),
    ]