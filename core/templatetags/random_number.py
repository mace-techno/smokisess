import random
from django import template

register = template.Library()


@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)


@register.filter
def split(splitable, split_at):
    # split with max limit
    if len(split_at.split("||||")) == 2:
        return splitable.split(split_at.split("||||")[0], int(split_at.split("||||")[1]))

    # normal split without max limitation
    return splitable.split(split_at)


@register.filter
def index(indexable, i):
    return indexable[i]
