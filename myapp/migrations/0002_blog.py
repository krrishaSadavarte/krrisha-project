# Generated by Django 4.1.7 on 2023-04-15 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=255)),
                ('file', models.FileField(upload_to='blog_images')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.users')),
            ],
        ),
    ]
