# Generated by Django 4.2.7 on 2023-11-30 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcd_render', '0002_rename_discomfort_form_desconforto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='Nome Completo',
            new_name='name',
        ),
    ]