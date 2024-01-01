# Generated by Django 5.0 on 2024-01-01 20:35

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=2000)),
                ('price', models.FloatField()),
                ('categorie', models.CharField(choices=[('development', 'development'), ('Design', 'Design'), ('It', 'It'), ('Marketing', 'Marketing')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Reviwes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(default=datetime.timezone)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_review', to='course.course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]