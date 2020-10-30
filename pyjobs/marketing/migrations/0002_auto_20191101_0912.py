# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-01 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketing", "0001_initial"),
    ]

    state_operations = [
        migrations.CreateModel(
            name="Messages",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "message_title",
                    models.CharField(
                        default="", max_length=100, verbose_name="Título da Mensagem"
                    ),
                ),
                (
                    "message_type",
                    models.CharField(
                        default="offer",
                        max_length=200,
                        verbose_name="Ticker usado no backend para ID da msg",
                    ),
                ),
                (
                    "message_content",
                    models.TextField(default="", verbose_name="Texto do E-mail"),
                ),
            ],
            options={
                "verbose_name": "Mensagem",
                "verbose_name_plural": "Mensagens",
                "db_table": "marketing_messages",
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name="contact",
            options={
                "verbose_name": "Resposta de Contato",
                "verbose_name_plural": "Respostas de contatos",
            },
        ),
        migrations.AlterModelOptions(
            name="mailinglist",
            options={
                "verbose_name": "Lista de e-mail",
                "verbose_name_plural": "Listas de e-mail",
            },
        ),
        migrations.AlterModelTable(
            name="contact",
            table=None,
        ),
        migrations.AlterModelTable(
            name="mailinglist",
            table=None,
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
