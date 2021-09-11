# Generated by Django 3.2.3 on 2021-05-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meno', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('sluzby', models.CharField(choices=[('Služby', 'Služby'), ('Django', 'Django'), ('React', 'React'), ('Html/CSS', 'Html/CSS')], default='Služby', max_length=20)),
                ('sprava', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Koment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meno', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(blank=True, max_length=20)),
                ('sprava', models.TextField()),
                ('avatar', models.ImageField(default='avatar.png', upload_to='')),
                ('blog_no', models.CharField(choices=[('Blog_1', 'Blog_1'), ('Blog_2', 'Blog_2'), ('Blog_3', 'Blog_3')], max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Kontakt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meno', models.CharField(max_length=20)),
                ('priezvisko', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('tema', models.CharField(max_length=20)),
                ('sprava', models.TextField()),
            ],
        ),
    ]
