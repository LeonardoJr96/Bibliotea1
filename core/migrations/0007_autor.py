# Generated by Django 5.1.1 on 2024-10-31 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_editora"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
    ]
