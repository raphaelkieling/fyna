# Generated by Django 2.0.9 on 2018-11-22 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('value', models.FloatField()),
                ('initial_date', models.DateField()),
                ('final_date', models.DateField()),
                ('is_renda', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tag'),
        ),
    ]
