# Generated by Django 5.1.3 on 2025-01-15 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_rename_type_docs_tipe_alter_docs_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docs',
            old_name='year',
            new_name='date',
        ),
    ]
