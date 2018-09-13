from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(Galeria)
admin.site.register(Participante)
admin.site.register(ParticipanteEvento)