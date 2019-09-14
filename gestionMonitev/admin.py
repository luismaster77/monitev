# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from gestionMonitev.models import Usuario,Empresa,Pasarela,Variable,Medidor

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Pasarela)
admin.site.register(Variable)
admin.site.register(Medidor)

