# Generated by Django 3.1.2 on 2020-10-04 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=30, verbose_name='Apellido')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Numero de Telefono')),
                ('email', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Mail')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Terapist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=30, verbose_name='Apellido')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Telefono')),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='Mail')),
                ('professional_registration', models.CharField(max_length=30, unique=True, verbose_name='Matricula')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=30, verbose_name='Link')),
                ('result', models.TextField(blank=True, null=True, verbose_name='Resultado')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychoApp.patient')),
                ('tenplate_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychoApp.templatetest')),
                ('terapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychoApp.terapist')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField(verbose_name='Enunciado')),
                ('question_type', models.CharField(choices=[('CL', 'Cerrada'), ('OP', 'Abierta')], default='OP', max_length=2, verbose_name='Tipo de Pregunta')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychoApp.templatetest')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='terapist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychoApp.terapist'),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choise', models.TextField(verbose_name='Opcion')),
                ('point', models.IntegerField(blank=True, null=True, verbose_name='Puntos')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychoApp.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(verbose_name='Respuesta')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='psychoApp.option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychoApp.question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychoApp.test')),
            ],
        ),
    ]
