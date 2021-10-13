# Generated by Django 3.2.4 on 2021-10-05 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_blog_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='core.comment'),
        ),
    ]
