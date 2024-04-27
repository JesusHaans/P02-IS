from django.contrib import admin
from .models import Cuenta, Solicitud, Usuario
# Register your models here.

admin.site.register(Cuenta)
admin.site.register(Solicitud)
admin.site.register(Usuario)