from django import template
from django.db.models import Count

from NewsApp.models import Category

register = template.Library()


@register.simple_tag(name='get_cat')
def get_categories():
    return Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)


@register.inclusion_tag('NewsApp/list_cat.html')
def show_categories():
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {'categories': categories}
