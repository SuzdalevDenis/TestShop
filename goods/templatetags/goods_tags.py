from django import template

from goods.models import Categories


register = template.library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()
