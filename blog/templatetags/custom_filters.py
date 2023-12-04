from django import template
from django.template.defaultfilters import stringfilter
from django.utils.dateparse import parse_duration


# Formatting and Displaying Django's DurationField in Templates
# https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/#writing-custom-template-filters
# https://copyprogramming.com/howto/display-and-format-django-durationfield-in-template#durationfield-format
register = template.Library()


@register.filter(name='duration')
@stringfilter
def duration_format(value):
    duration = parse_duration(value)
    total_seconds = duration.total_seconds()
    minutes, seconds = divmod(total_seconds, 60)
    return f"{int(minutes):02d}:{int(seconds):02d}"
