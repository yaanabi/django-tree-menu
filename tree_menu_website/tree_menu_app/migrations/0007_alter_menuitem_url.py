# Generated by Django 5.1.1 on 2024-10-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu_app', '0006_alter_menuitem_slug_name_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.URLField(blank=True, max_length=355, null=True, unique=True, verbose_name='Plain URL link to menu item content'),
        ),
    ]
