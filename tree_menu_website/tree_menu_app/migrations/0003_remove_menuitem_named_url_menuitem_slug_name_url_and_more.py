# Generated by Django 5.1.1 on 2024-09-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu_app', '0002_remove_menuitem_parent_menuitem_parent_menu_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='named_url',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='slug_name_url',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', unique=True, verbose_name='Slug url name to menu item detail'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.URLField(blank=True, max_length=355, null=True, verbose_name='Plain URL link to menu item content'),
        ),
    ]
