# Generated by Django 4.1.7 on 2023-05-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zohoapp", "0009_rename_name_expense_vendor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense", name="vendor", field=models.CharField(max_length=200),
        ),
    ]