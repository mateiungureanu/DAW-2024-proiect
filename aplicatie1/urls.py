from django.urls import path, re_path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import CinemaSitemap, AngajatiSitemap, FilmeSitemap, ProduseSitemap, CustomUserSitemap

sitemaps = {
    'cinemauri': CinemaSitemap,
    'angajati': AngajatiSitemap,
    'filme': FilmeSitemap,
    'produse': ProduseSitemap,
    'users': CustomUserSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.view.sitemap'),
	path("", views.index, name="index"),
    path('filtrare_filme/', views.filtrare_filme),
    path('mesaj_trimis', views.mesaj_trimis, name='mesaj_trimis'),
    path('contact_view', views.contact_view),
    path('contact', views.contact, name='contact'),
    path('filtrare_filme_2/', views.filtrare_filme_2, name='filtrare_filme_2'),
    path('creare_angajati/', views.creare_angajati, name='creare_angajati'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('confirm_email/<str:cod>/', views.confirm_email, name='confirm_email'),
    path('adauga_vizualizare/', views.adauga_vizualizare),
    path('promotii/', views.pagina_promotii, name='promotii'),
    path('promotie_lansata/', views.promotie_lansata, name='promotie_lansata'),
    path('ofera_permisiune/', views.ofera_permisiune, name='ofera_permisiune'),
    path('oferta/', views.oferta, name='oferta'),
    path('cinema/<int:id>/', views.cinema_detail, name='cinema_detail'),
    path('angajat/<int:id>/', views.angajat_detail, name='angajat_detail'),
    path('film/<int:id>/', views.film_detail, name='film_detail'),
    path('produs/<int:id>/', views.produs_detail, name='produs_detail'),
    path('utilizator/<int:id>/', views.utilizator_detail, name='utilizator_detail'),
    path('lista_cinemauri/', views.lista_cinemauri, name='lista_cinemauri'),
    path('lista_angajati/', views.lista_angajati, name='lista_angajati'),
    path('lista_filme/', views.lista_filme, name='lista_filme'),
    path('lista_produse/', views.lista_produse, name='lista_produse'),
    path('lista_utilizatori/', views.lista_utilizatori, name='lista_utilizatori'),
    path('block_user/<int:user_id>/', views.block_user, name='block_user'),
    path('unblock_user/<int:user_id>/', views.unblock_user, name='unblock_user'),
    path('cos_virtual/', views.cos_virtual, name='cos_virtual'),
    path('cumpara_cos/', views.cumpara_cos, name='cumpara_cos'),
]