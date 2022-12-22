from django.contrib import admin
from .models import Task

# Définition de la classe d'administration pour le modèle Task


class TaskAdmin(admin.ModelAdmin):
    # Définition des champs à afficher dans la liste des tâches
    list_display = ('description', 'completed',)


# Enregistrement du modèle Task dans l'interface d'administration
admin.site.register(Task, TaskAdmin)
