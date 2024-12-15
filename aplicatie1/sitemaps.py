from django.contrib.sitemaps import Sitemap
from .models import Cinemauri, Angajati, Filme, Produse, CustomUser

class CinemaSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Cinemauri.objects.all()

class AngajatiSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Angajati.objects.all()

class FilmeSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.7

    def items(self):
        return Filme.objects.all()

class ProduseSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Produse.objects.all()

class CustomUserSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.4

    def items(self):
        return CustomUser.objects.filter(is_active=True)
