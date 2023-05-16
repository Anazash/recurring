# Generated by Django 4.1.7 on 2023-05-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zohoapp", "0005_expense_customername_expense_destination_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor_table",
            name="name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="expense",
            name="customername",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="expense",
            name="destination",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="expense",
            name="notes",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="expense",
            name="tax",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
