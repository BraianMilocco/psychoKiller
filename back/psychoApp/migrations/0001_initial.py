# Generated by Django 3.1.2 on 2020-10-08 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Terapist",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "email",
                    models.CharField(max_length=50, unique=True, verbose_name="Mail"),
                ),
                ("username", models.CharField(max_length=30, verbose_name="Nombre")),
                ("last_name", models.CharField(max_length=30, verbose_name="Apellido")),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Telefono"
                    ),
                ),
                (
                    "professional_registration",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="Matricula"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "last_login",
                    models.DateField(auto_now=True, verbose_name="ultimo logueo"),
                ),
                (
                    "is_admin",
                    models.BooleanField(default=False, verbose_name="es admin"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="está activo"),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name=" es personal"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="es super usuario"),
                ),
            ],
            options={
                "verbose_name": "Terapista",
                "verbose_name_plural": "Terapistas",
            },
        ),
        migrations.CreateModel(
            name="Patient",
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
                ("first_name", models.CharField(max_length=30, verbose_name="Nombre")),
                ("last_name", models.CharField(max_length=30, verbose_name="Apellido")),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Numero de Telefono",
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        unique=True,
                        verbose_name="Mail",
                    ),
                ),
                (
                    "terapist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TemplateTest",
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
                ("name", models.CharField(max_length=30, verbose_name="Nombre")),
            ],
        ),
        migrations.CreateModel(
            name="Test",
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
                ("link", models.CharField(max_length=30, verbose_name="Link")),
                (
                    "result",
                    models.TextField(blank=True, null=True, verbose_name="Resultado"),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="psychoApp.patient",
                    ),
                ),
                (
                    "tenplate_test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="psychoApp.templatetest",
                    ),
                ),
                (
                    "terapist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
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
                ("query", models.TextField(verbose_name="Enunciado")),
                (
                    "question_type",
                    models.CharField(
                        choices=[("CL", "Cerrada"), ("OP", "Abierta")],
                        default="OP",
                        max_length=2,
                        verbose_name="Tipo de Pregunta",
                    ),
                ),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="psychoApp.templatetest",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Option",
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
                ("choise", models.TextField(verbose_name="Opcion")),
                (
                    "point",
                    models.IntegerField(blank=True, null=True, verbose_name="Puntos"),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="psychoApp.question",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("response", models.TextField(verbose_name="Respuesta")),
                (
                    "option",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="psychoApp.option",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="psychoApp.question",
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="psychoApp.test"
                    ),
                ),
            ],
        ),
    ]
