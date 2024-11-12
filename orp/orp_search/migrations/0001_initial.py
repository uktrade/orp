# Generated by Django 5.1.2 on 2024-11-10 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataResponseModel",
            fields=[
                ("search_terms", models.CharField(max_length=2048)),
                ("title", models.CharField(max_length=2048)),
                ("identifier", models.URLField(unique=True)),
                (
                    "publisher",
                    models.CharField(default="Legislation", max_length=2048),
                ),
                ("language", models.CharField(default="eng", max_length=3)),
                ("format", models.CharField(default="HTML", max_length=50)),
                ("description", models.TextField()),
                ("date_issued", models.DateField(blank=True, null=True)),
                ("date_modified", models.DateField()),
                ("date_valid", models.DateField(blank=True, null=True)),
                (
                    "audience",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                ("coverage", models.CharField(default="gb", max_length=2)),
                (
                    "subject",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                ("type", models.CharField(max_length=50)),
                (
                    "license",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "regulatory_topics",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                ("status", models.CharField(default="Active", max_length=50)),
                (
                    "date_uploaded_to_orp",
                    models.DateField(blank=True, null=True),
                ),
                (
                    "has_format",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "is_format_of",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "has_version",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "is_version_of",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "references",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "is_referenced_by",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "has_part",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "is_part_of",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "is_replaced_by",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "replaces",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "related_legislation",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                ("id", models.URLField(primary_key=True, serialize=False)),
                (
                    "score",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
            ],
        ),
    ]
