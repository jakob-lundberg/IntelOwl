# Generated by Django 4.2.16 on 2024-11-29 09:06

from django.db import migrations

import api_app.data_model_manager.fields


class Migration(migrations.Migration):

    dependencies = [
        ("data_model_manager", "0003_remove_ipdatamodel_ietf_report_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="domaindatamodel",
            name="evaluation",
            field=api_app.data_model_manager.fields.LowercaseCharField(
                blank=True,
                choices=[
                    ("trusted", "Trusted"),
                    ("clean", "Clean"),
                    ("suspicious", "Suspicious"),
                    ("malicious", "Malicious"),
                ],
                default=None,
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="filedatamodel",
            name="evaluation",
            field=api_app.data_model_manager.fields.LowercaseCharField(
                blank=True,
                choices=[
                    ("trusted", "Trusted"),
                    ("clean", "Clean"),
                    ("suspicious", "Suspicious"),
                    ("malicious", "Malicious"),
                ],
                default=None,
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="ipdatamodel",
            name="evaluation",
            field=api_app.data_model_manager.fields.LowercaseCharField(
                blank=True,
                choices=[
                    ("trusted", "Trusted"),
                    ("clean", "Clean"),
                    ("suspicious", "Suspicious"),
                    ("malicious", "Malicious"),
                ],
                default=None,
                max_length=100,
                null=True,
            ),
        ),
    ]
