from django import template
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('tree_menu_app/menu.html')
def draw_menu(menu_name: str):
    menu = MenuItem.objects.filter(menu__name==menu_name).select_related # type: ignore
