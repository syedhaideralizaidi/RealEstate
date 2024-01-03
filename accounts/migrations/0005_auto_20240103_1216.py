# Generated by Django 3.2.18 on 2024-01-03 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_useraccount_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraccount',
            options={},
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='username',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]