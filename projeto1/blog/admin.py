from django.contrib import admin
from .models import Post, Comentario # Importe seus modelos

admin.site.register(Post)
admin.site.register(Comentario)