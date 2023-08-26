# Generated by Django 4.1.7 on 2023-05-17 01:37

from django.db import migrations, models
import django.utils.timezone
import social.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=social.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=500)),
                ('creat', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.CharField(max_length=50000)),
            ],
            options={
                'ordering': ['-creat'],
            },
        ),
        migrations.CreateModel(
            name='SocialComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='SocialPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.CharField(choices=[('NoPublicado', 'NoPublicado'), ('NoRevisado', 'NoRevisado'), ('Publicado', 'Publicado')], default='NoRevisado', max_length=100)),
                ('body', models.TextField(default='')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]