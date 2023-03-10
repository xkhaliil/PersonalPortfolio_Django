from django.contrib import admin
from django.urls import reverse
from configuration.models import Diplome
from configuration.models import Stage
from configuration.models import Competence
from configuration.models import Genre

class DiplomeAdmin(admin.ModelAdmin):
    #heritage= admin.ModelAdmin
    list_display = ('nomDiplome','gen', 'lieuDiplome')
    list_filter = ('nomDiplome', 'lieuDiplome')
    date_hierarchy = 'dateDiplome'
    ordering = ('dateDiplome',)
    search_fields = ('nomDiplome', 'gen')

class StageAdmin(admin.ModelAdmin):
    #heritage= admin.ModelAdmin
    list_display = ('natureStage', 'lieuStage','dureeStage')
    list_filter = ('natureStage', 'lieuStage')
    search_fields = ('natureStage', 'dureeStage')

class CompetenceAdmin(admin.ModelAdmin):
    #heritage= admin.ModelAdmin
    list_display = ('nomCompetence', 'niveauCompetence','genre')
    list_filter = ('nomCompetence', 'niveauCompetence')
    search_fields = ('nomCompetence', 'genre')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('nomGenre', 'apercu')
    list_filter = ('nomGenre','id')
    search_fields = ('nomDiplome', 'lieuDiplome') 
    def apercu (self, gen):
     text = gen.descriptionGenre[:40]
     if len(gen.descriptionGenre) > 40:
        return '{}...'.format(text)
     else:
         return text
    def typ_link(self, dip):
        return mark_safe('<a href="{}">{}</a>'.format(reverse("admin:configuration_type_change", args=(dip.gen.pk,)),dip.gen.nomGenre
        ))  




admin.site.register(Diplome,DiplomeAdmin)
admin.site.register(Stage,StageAdmin)
admin.site.register(Competence,CompetenceAdmin)
admin.site.register(Genre,GenreAdmin)