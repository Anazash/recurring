# Generated by Django 4.1.7 on 2023-05-11 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("zohoapp", "0010_alter_expense_vendor"),
    ]

    operations = [
        migrations.DeleteModel(name="vendor_table",),
    ]
