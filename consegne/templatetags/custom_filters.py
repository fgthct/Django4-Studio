# templatetags/s.custom_filterpy

from django import template

register = template.Library()


@register.filter
def format_coordinates(point):
    if isinstance(point, float):
        return f"{point:.6f}"
    else:
        return f"{point.x:.6f}, {point.y:.6f}"
