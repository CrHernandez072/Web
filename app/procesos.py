from .models import Autor
import django
import sys

def proceso_context_autor(request):
	get_version_django = django.get_version()
	get_version_python = sys.version

	p = Autor.objects.all()
	diccionario = {"python_version": get_version_python, "django_version": get_version_django, "autores":p}

	#Tambien se puede  mandar formularios
	#formulario = form_registro()
	#diccionario = {"python_version": get_version_python, "django_version": get_version_django, "estatus":p, "formulario": formulario}
	return diccionario