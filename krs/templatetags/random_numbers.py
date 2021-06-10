import random
from django import template

register = template.Library()


@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)


@register.simple_tag
def plus_im_10er():
    task = dict()
    while True:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        res = a + b
        if res <= 10:
            task['a'] = a
            task['b'] = b
            task['res'] = res
            break

    return task


@register.simple_tag
def list_of_ints():
    ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return ints
