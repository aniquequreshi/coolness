# Generated by Django 3.0.4 on 2020-03-14 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial', '0002_auto_20200314_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='bypass_admin_contact_directly_answer',
        ),
        migrations.RemoveField(
            model_name='person',
            name='permission_share_answer',
        ),
        migrations.RemoveField(
            model_name='person',
            name='preferred_method_of_contact_by_admin',
        ),
        migrations.RemoveField(
            model_name='person',
            name='preferred_method_of_contact_by_admin_answer',
        ),
        migrations.RemoveField(
            model_name='person',
            name='provide_contact_if_yes',
        ),
        migrations.RemoveField(
            model_name='person',
            name='provide_contact_if_yes_answer',
        ),
        migrations.AlterField(
            model_name='person',
            name='bypass_admin_contact_directly',
            field=models.CharField(blank=True, choices=[('NO', 'No'), ('YES', 'Yes')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='children_from_previous_marriage',
            field=models.CharField(blank=True, choices=[('NO', 'No'), ('YES', 'Yes')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='permission_share',
            field=models.CharField(blank=True, choices=[('NO', 'No'), ('YES', 'Yes')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='significant_health_issues',
            field=models.CharField(blank=True, choices=[('NO', 'No'), ('YES', 'Yes')], max_length=50, null=True),
        ),
    ]
