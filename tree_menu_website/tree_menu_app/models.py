from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return f"'{self.name}' menu"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent_menu = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='submenus',
    )
    url = models.URLField(verbose_name='Plain URL link to menu item content',
                          max_length=355,
                          null=True,
                          blank=True)
    # named_url = models.CharField(
    #     verbose_name='Named URL link to menu item content',
    #     max_length=100,
    #     unique=True)
    slug_name_url = models.SlugField(
        verbose_name='Slug url name to menu item detail',
        unique=True,
        blank=True,
        max_length=50)

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    # def get_url(self):
    #     if self.named_url:
    #         return reverse(self.named_url)
    #     return self.url

    def save(self, *args, **kwargs):
        if not self.slug_name_url:
            self.slug_name_url = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"'{self.name}' menu item for '{self.menu.name}' with parent '{getattr(self.parent_menu, 'name', None)}'"
