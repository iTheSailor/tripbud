# Generated by Django 4.2.3 on 2023-08-22 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_post_dislikes_alter_post_text_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='dashboard.comment'),
        ),
    ]