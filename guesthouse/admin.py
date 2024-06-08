from django.contrib import admin
from .models import Role, GuestHouseEvent, Hebergement, Historique, Reshebergement, Ressalle, Salle
from django.utils.translation import gettext_lazy as _

class RoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_directeur', 'is_chefreception', 'is_admin', 'is_financier')
    search_fields = ('user__username',)
    list_filter = ('is_directeur', 'is_chefreception', 'is_admin', 'is_financier')
admin.site.register(Role, RoleAdmin)

class GuestHouseEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_time', 'end_time')
    search_fields = ('title',)
    list_filter = ('start_time', 'end_time')
admin.site.register(GuestHouseEvent, GuestHouseEventAdmin)
class HebergementAdmin(admin.ModelAdmin):
    list_display = ('idchambre', 'numero', 'type', 'description', 'prix', 'maison', 'chambre', 'etage', 'local')
    search_fields = ('numero', 'type', 'maison')
admin.site.register(Hebergement, HebergementAdmin)


class ReshebergementAdmin(admin.ModelAdmin):
    list_display = ('idhebergement', 'Courrier', 'etablissement', 'Demandeur', 'Capacite', 'DateEntre', 'DateSortie', 'PriseenCharge', 'Moyen', 'Statut', 'Type')  # Removed 'hebergement'
    search_fields = ('Etablissement', 'Demandeur', 'Statut', 'Type')
    list_filter = ('DateEntre', 'DateSortie', 'hebergement', 'Statut')

admin.site.register(Reshebergement, ReshebergementAdmin)
class RessalleAdmin(admin.ModelAdmin):
    list_display = (
        'idressalle', 'etablissement', 'demandeur', 'dateEntrée', 'dateSortie', 
        'Salle', 'nombrePersonne', 'sujet', 'dejeuner', 'pauseCafe', 
        'courrier', 'moyen', 'priseEnCharge', 'statut'
    )
    search_fields = ('etablissement', 'demandeur', 'sujet', 'statut')
    list_filter = ('dateEntrée', 'dateSortie', 'Salle', 'statut')

admin.site.register(Ressalle, RessalleAdmin)
class SalleAdmin(admin.ModelAdmin):
    list_display = ('idsalle', 'type', 'prix', 'local')
    search_fields = ('type', 'local')
admin.site.register(Salle, SalleAdmin)
admin.site.register(Historique)


admin.site.site_title = _("Guesthouse")
admin.site.site_header = _("Guesthouse")
admin.site.home_title = _("Guesthouse")

