from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import Cinemauri, Angajati, Sali, Filme, Difuzari, Achizitii, Bilete
from .models import CustomUser, Produse, Categorii, Vizualizari, Promotii

class CinemauriAdmin(admin.ModelAdmin):
    list_display = ('nume_cinema', 'oras')
    list_filter = ('oras',)
    search_fields = ('nume_cinema', 'oras')
    ordering = ('oras', 'nume_cinema')

class AngajatiAdmin(admin.ModelAdmin):
    list_display = ('nume', 'prenume', 'email', 'nr_telefon', 'salariu', 'pct_comision', 'data_angajarii', 'id_sef')
    list_filter = ('salariu', 'pct_comision', 'data_angajarii')
    search_fields = ('nume', 'prenume')
    ordering = ('id', 'nume',  'prenume')
    fieldsets = (
        ('Informatii generale', {
            'fields': ('nume', 'prenume')
        }),
        ('Date de contact', {
            'fields': ('email', 'nr_telefon'),
            'classes': ('collapse',),
        }),
        ('Datele companiei', {
            'fields': ('salariu', 'pct_comision', 'data_angajarii', 'id_sef'),
            'classes': ('collapse',),
        }),
    )

class SaliAdmin(admin.ModelAdmin):
    list_display = ('cinema',)
    list_filter = ('cinema',)
    search_fields = ('cinema',)
    ordering = ('cinema', 'id')

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nume_film', 'durata', 'rating', 'regizor', 'anul_lansarii')
    list_filter = ('durata', 'rating', 'anul_lansarii')
    search_fields = ('nume_film', 'regizor', 'anul_lansarii')
    ordering = ('anul_lansarii', 'nume_film')

class DifuzariAdmin(admin.ModelAdmin):
    list_display = ('data_ora', 'sala', 'film')
    list_filter = ('data_ora',)
    search_fields = ('data_ora', 'sala', 'film')
    ordering = ('data_ora',)

class AchizitiiAdmin(admin.ModelAdmin):
    list_display = ('email', 'nr_telefon')
    list_filter = ('email', 'nr_telefon')
    search_fields = ('email', 'nr_telefon')
    ordering = ('id',)

class BileteAdmin(admin.ModelAdmin):
    list_display = ('rand', 'coloana', 'difuzare', 'achizitie', 'angajat')
    list_filter = ('difuzare',)
    search_fields = ('difuzare', 'achizitie', 'angajat')
    ordering = ('difuzare', 'achizitie')

admin.site.register(Cinemauri, CinemauriAdmin)
admin.site.register(Angajati, AngajatiAdmin)
admin.site.register(Sali, SaliAdmin)
admin.site.register(Filme, FilmeAdmin)
admin.site.register(Difuzari, DifuzariAdmin)
admin.site.register(Achizitii, AchizitiiAdmin)
admin.site.register(Bilete, BileteAdmin)

admin.site.site_header = "Panou de Administrare Site"
admin.site.site_title = "Admin Site"
admin.site.index_title = "Bine ai venit in panoul de administrare"

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'nume', 'prenume', 'telefon', 'adresa', 'data_nasterii', 'gen', 'ocupatie', 
                    'email_confirmat', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'gen', 'email_confirmat')
    search_fields = ('username', 'email', 'telefon', 'ocupatie')
    ordering = ('username',)
    fieldsets = UserAdmin.fieldsets + (
        ('Informații suplimentare', {
            'fields': ('nume', 'prenume', 'telefon', 'adresa', 'data_nasterii', 'gen', 'ocupatie', 'email_confirmat'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informații suplimentare', {
            'fields': ('nume', 'prenume', 'telefon', 'adresa', 'data_nasterii', 'gen', 'ocupatie', 'email_confirmat'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Produse)
class ProduseAdmin(admin.ModelAdmin):
    list_display = ('nume', 'categorie', 'pret')
    search_fields = ('nume', 'categorie')
    list_filter = ('categorie',)

@admin.register(Categorii)
class CategoriiAdmin(admin.ModelAdmin):
    list_display = ('nume',)
    search_fields = ('nume',)

@admin.register(Vizualizari)
class VizualizariAdmin(admin.ModelAdmin):
    list_display = ('utilizator', 'produs', 'data_vizualizare')
    search_fields = ('utilizator__username', 'produs__nume')
    list_filter = ('data_vizualizare',)

@admin.register(Promotii)
class PromotiiAdmin(admin.ModelAdmin):
    list_display = ('nume', 'data_creare', 'data_expirare', 'reducere_procentuala', 'suma_minima_comanda')
    search_fields = ('nume', 'subiect')
    list_filter = ('data_creare', 'data_expirare', 'categorii')
