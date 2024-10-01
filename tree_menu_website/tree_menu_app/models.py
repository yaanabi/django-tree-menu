from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from urllib import parse


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

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
                          unique=True,
                          null=True,
                          blank=True)
    # named_url = models.CharField(
    #     verbose_name='Named URL link to menu item content',
    #     max_length=100,
    #     unique=True)
    named_url = models.SlugField(
        verbose_name='Slug url name to menu item detail',
        unique=True,
        blank=True,
        max_length=50)

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def get_url(self):
        """
        If url is set, convert it to relative and return it . Otherwise, return a slug url that would lead to
        the view that shows details of the menu item.
        """

        if self.url:
            relative_url = parse.urlparse(self.url)
            print(relative_url)
            return relative_url.path
        return reverse(
            'menu_item_detail',
            kwargs={'menu_item_slug': self.named_url},
        )
    def get_url_slug(self):
        """
        If url is set, convert it to relative and return it . Otherwise, return a slug url that would lead to
        the view that shows details of the menu item.
        """

        if self.url:
            relative_url = parse.urlparse(self.url).path
            return relative_url.replace('/', '')
        return self.named_url

    def save(self, *args, **kwargs):
        if not self.named_url:
            self.named_url = slugify(f'{self.menu.name} {self.name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"'{self.name}' menu item for '{self.menu.name}' with parent '{getattr(self.parent_menu, 'name', None)}'"
