from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class Cinemauri(models.Model):
    nume_cinema = models.CharField(max_length=255, unique=True)
    oras = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nume_cinema} | oras: {self.oras}"
    
    def get_absolute_url(self):
        return reverse('cinema_detail', kwargs={'id': self.id})

class Angajati(models.Model):
    nume = models.CharField(max_length=255)
    prenume = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    nr_telefon = models.PositiveBigIntegerField(null=True, blank=True)
    salariu = models.PositiveIntegerField()
    pct_comision = models.DecimalField(max_digits=4, decimal_places=2)
    data_angajarii = models.DateField()
    id_sef = models.PositiveSmallIntegerField(null=True, blank=True)

    cinema = models.ForeignKey('Cinemauri', on_delete=models.CASCADE)
    curata = models.ManyToManyField('Sali', related_name='angajati', blank=True)

    def __str__(self):
        return f"{self.nume} {self.prenume} | email: {self.email} | telefon: +40{self.nr_telefon} | salariu: {self.salariu} | puncte comision: {self.pct_comision} | data angajarii: {self.data_angajarii} | id sef: {self.id_sef} | cinema: {self.cinema}"
    
    def get_absolute_url(self):
        return reverse('angajat_detail', kwargs={'id': self.id})

class Sali(models.Model):
    cinema = models.ForeignKey('Cinemauri', on_delete=models.CASCADE)
    curata = models.ManyToManyField('Angajati', related_name='sali', blank=True)

    def __str__(self):
        return f"{self.id}"

class Filme(models.Model):
    nume_film = models.CharField(max_length=255)
    durata = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    regizor = models.CharField(max_length=255, null=True, blank=True)
    anul_lansarii = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nume_film} | durata: {self.durata} | regizor: {self.regizor} | anul lansarii: {self.anul_lansarii}"
    
    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'id': self.id})

class Difuzari(models.Model):
    data_ora = models.DateTimeField(null=True, blank=True)
    sala = models.ForeignKey('Sali', on_delete=models.CASCADE)
    film = models.ForeignKey('Filme', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.data_ora}"

class Achizitii(models.Model):
    email = models.EmailField(null=True, blank=True)
    nr_telefon = models.PositiveBigIntegerField(null=True, blank=True)

    def __str__(self):
        return f"email: {self.email} | telefon: +40{self.nr_telefon}"

class Bilete(models.Model):
    rand = models.PositiveSmallIntegerField()
    coloana = models.PositiveSmallIntegerField()
    difuzare = models.ForeignKey('Difuzari', on_delete=models.CASCADE, related_name='bilete_difuzare')
    angajat = models.ForeignKey('Angajati', on_delete=models.CASCADE, related_name='bilete_angajat')
    achizitie = models.ForeignKey('Achizitii', on_delete=models.CASCADE, related_name='bilete_achizitie')

    def __str__(self):
        return f"achizitie: {self.achizitie.id} | rand: {self.rand}, coloana: {self.coloana}"

class CustomUser(AbstractUser):
    nume = models.CharField(max_length=50, blank=True)
    prenume = models.CharField(max_length=50, blank=True)
    telefon = models.CharField(max_length=15, blank=True)
    adresa = models.TextField(blank=True)
    data_nasterii = models.DateField(null=True, blank=True)
    gen = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Feminin')], null=True, blank=True)
    ocupatie = models.CharField(max_length=50, blank=True)
    cod = models.CharField(max_length=100, null=True, blank=True)
    email_confirmat = models.BooleanField(default=False)
    blocat = models.BooleanField(default=False)
    
    class Meta:
        permissions = [
            ("vizualizeaza_oferta", "Afiseaza oferta, pentru unii clienti."),
            ("editeaza_campuri_nume_prenume_email", "Editeaza campurile nume, prenume, email"),
            ("blocare_utilizatori", "Blocheaza utilizatori")
        ]
    
    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'id': self.id})

class Produse(models.Model):
    nume = models.CharField(max_length=255)
    categorie = models.CharField(max_length=100)
    pret = models.DecimalField(max_digits=10, decimal_places=2)
    descriere = models.TextField(blank=True)
    stoc = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nume
    
    def get_absolute_url(self):
        return reverse('produs_detail', kwargs={'id': self.id})

class Categorii(models.Model):
    nume = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nume

class Vizualizari(models.Model):
    utilizator = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    produs = models.ForeignKey('Produse', on_delete=models.CASCADE)
    data_vizualizare = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_vizualizare']

class Promotii(models.Model):
    nume = models.CharField(max_length=255)
    data_creare = models.DateTimeField(auto_now_add=True)
    data_expirare = models.DateTimeField()
    subiect = models.CharField(max_length=255)
    mesaj = models.TextField()
    categorii = models.ManyToManyField('Categorii', related_name='promotii')
    reducere_procentuala = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    suma_minima_comanda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nume

class Comanda(models.Model):
    utilizator = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    produs = models.ForeignKey('Produse', on_delete=models.CASCADE)
    cantitate = models.PositiveIntegerField()
    data_comanda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comanda #{self.id} | {self.utilizator.username} - {self.produs.nume} ({self.cantitate})"