from django import template

from django.db import connection

from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name: str):
    menu = MenuItem.objects.filter(
        menu__name=menu_name).select_related('parent_menu')
    # ----------------------------------------------------------------------
    # using it with prefetch_related('submenus') will make a total of two queries,
    # but it wont render empty ul's in html for menu items without submenus
    # ----------------------------------------------------------------------
    # menu_items_with_children = [item.pk for item in menu if item.submenus.exists()]

    return {
        'menu': menu,
        # 'menu_items_with_children': menu_items_with_children,
        'request_url_slug': context['request'].path.replace('/', ''),
        'parent': None,  # For first iteraton of menu items parent is not set 
        'menu_name': menu_name
    }
