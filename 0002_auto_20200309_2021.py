# Generated by Django 3.0.4 on 2020-03-09 22:01

from django.db import migrations

def populate_data(apps, schema_editor):
    Person = apps.get_model('matrimonial', 'Person')
    person1 = Person(last_name='Jim', status ='1')
    person1.save()
    person2 = Person(last_name='John', status ='2')
    person2.save()

class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_data),
    ]
