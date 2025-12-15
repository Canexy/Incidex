from django import template

register = template.Library()

# Humaniza el estado de las incidencias en las vistas de detalle.
@register.filter
def humanize_estado(value):
    if not value:
        return ""
    return value.replace("_", " ").capitalize()
