# Generated by Django 5.0.1 on 2024-02-07 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("listings", "0002_alter_listing_listing_for"),
    ]

    operations = [
        migrations.CreateModel(
            name="ListingFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "short_description",
                    models.CharField(max_length=255, verbose_name="Short description"),
                ),
                (
                    "file",
                    models.FileField(
                        default=None, upload_to="listings/files/", verbose_name="File"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Updated"
                    ),
                ),
                (
                    "for_customer",
                    models.BooleanField(default=True, verbose_name="For customers"),
                ),
                (
                    "listing",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="listings.listing",
                        verbose_name="Listing",
                    ),
                ),
            ],
        ),
    ]
