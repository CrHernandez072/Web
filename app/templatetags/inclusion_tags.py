from django import template
from app import models

register = template.Library()
@register.inclusion_tag('app/inclusion.html')

def show_autores():
	detalle = models.detalle_libros.objects.all()
	return {'key_detalle': "detalle"}