# Generated by Django 5.0.1 on 2024-02-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="listing_for",
            field=models.CharField(
                choices=[("R", "Rent"), ("S", "Sell")],
                default="S",
                max_length=5,
                verbose_name="Listing for",
            ),
        ),
    ]