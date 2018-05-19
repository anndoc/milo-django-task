import datetime

from django import template
from django.conf import settings
from django.utils.translation import ugettext as _

register = template.Library()


@register.simple_tag
def is_allowed(user):
    if datetime.date.today().year - user.birthday.year > settings.USER_ALLOWED_AGE:
        return _('allowed')
    return _('blocked')


@register.simple_tag
def bizzfuzz(user):
    random_number = user.random_number
    if random_number % 3 == 0 and random_number % 5 == 0:
        return _('BizzFuzz')
    if random_number % 3 == 0:
        return _('Bizz')
    if random_number % 5 == 0:
        return _('Fuzz')
    return random_number
