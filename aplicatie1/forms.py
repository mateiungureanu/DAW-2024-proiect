from django import forms
from datetime import date
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser
from .models import Angajati
from .models import Promotii, Categorii

def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Acest camp trebuie sa contina doar litere.")

class ContactViewForm(forms.Form):
    nume = forms.CharField(
        label="Nume",
        required=True,
        max_length=50,
        error_messages={
            'required': 'Numele de utilizator este obligatoriu.',
            'max_length': 'Numele de utilizator nu poate depasi 50 de caractere.'
        }
    )
    email = forms.EmailField(
        label='Email', 
        required=True,
        error_messages={
            'invalid': 'Introduceti o adresa de email valida.'
        }
    )
    mesaj = forms.CharField(widget=forms.Textarea, label='Mesaj', required=True)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Adresa de email trebuie sa fie de la gmail.com")
        return email
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        if email and confirm_email and email != confirm_email:
            raise forms.ValidationError("Adresele de email nu coincid.")

class FilmeFilterForm(forms.Form):
    nume_film = forms.CharField(required=False, label="Nume Film")
    min_durata = forms.IntegerField(required=False, label="Durata Minima")
    max_durata = forms.IntegerField(required=False, label="Durata Maxima")
    min_rating = forms.DecimalField(required=False, label="Rating Minim")
    max_rating = forms.DecimalField(required=False, label="Rating Maxim")
    regizor = forms.CharField(required=False, label="Regizor")
    min_anul_lansarii = forms.IntegerField(required=False, label="An Lansare Min.")
    max_anul_lansarii = forms.IntegerField(required=False, label="An Lansare Max.")

class ContactForm(forms.Form):
    nume = forms.CharField(required=True, label="Nume", validators=[validate_only_letters])
    prenume = forms.CharField(required=False, label="Prenume", validators=[validate_only_letters])
    data_nasterii = forms.DateField(required=False, label="Data nasterii")
    email = forms.EmailField(required=True, label='Email')
    confirmare_email = forms.EmailField(required=True, label='Confirmare email')
    TIPURI_MESAJ = [
        ('reclamatie', 'Reclamatie'),
        ('intrebare', 'Intrebare'),
        ('review', 'Review'),
        ('cerere', 'Cerere'),
        ('programare', 'Programare'),
        ('none', 'None')
    ]
    tip_mesaj = forms.ChoiceField(required=False, choices=TIPURI_MESAJ, label="Tipuri mesaj")
    subiect = forms.CharField(required=True, label="Subiect", validators=[validate_only_letters])
    minim_zile_asteptare = forms.IntegerField(required=False, label="Minim zile asteptare")
    mesaj = forms.CharField(required=False, widget=forms.Textarea, label='Mesaj (+semnatura)')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Adresa de email trebuie sa fie de la gmail.com")
        return email
    
    def clean_data_nasterii(self):
        data_nasterii = self.cleaned_data.get('data_nasterii')
        if data_nasterii:
            today = date.today()
            age = today.year - data_nasterii.year - ((today.month, today.day) < (data_nasterii.month, data_nasterii.day))
            if age < 18:
                raise ValidationError("Utilizatorul trebuie sa fie major.")
        return data_nasterii

    def clean_mesaj(self):
        mesaj = self.cleaned_data.get('mesaj')
        if mesaj:
            cuvinte = re.findall(r'\w+', mesaj)
            if not 4 < len(cuvinte) < 101:
                raise forms.ValidationError("Mesaj prea scurt / lung.")
            if re.search(r'http[s]?://', mesaj):
                raise forms.ValidationError("Mesajul contine link(uri).")
        return mesaj

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirmare_email = cleaned_data.get("confirmare_email")
        if email and confirmare_email and email != confirmare_email:
            raise forms.ValidationError("Adresele de email nu coincid.")
        mesaj = self.cleaned_data.get('mesaj')
        cuvinte = re.findall(r'\w+', mesaj)
        prenume = self.cleaned_data.get('prenume')
        if mesaj and prenume and cuvinte[-1] != prenume:
            raise forms.ValidationError("Semnatura lipseste sau e invalida.")
        return cleaned_data

class AngajatiForm(forms.ModelForm):
    NIVEL_STUDII_CHOICES = [
        ('1.liceu', 'Liceu'),
        ('2.licenta', 'Licenta'),
        ('3.master', 'Master'),
        ('4.doctorat', 'Doctorat'),
    ]
    nivel_studii = forms.ChoiceField(
        label="Nivel de Studii",
        choices=NIVEL_STUDII_CHOICES,
        help_text="Selectati cel mai inalt nivel de studii finalizat.",
        required=True
    )
    zile_vacanta = forms.IntegerField(
        label="Zile de Vacanta",
        help_text="Numarul de zile disponibile anual.",
        required=True
    )

    class Meta:
        model = Angajati
        fields = ['nume', 'prenume', 'email', 'nr_telefon', 'salariu', 'pct_comision', 'data_angajarii', 'cinema']
        labels = {
            'nume': 'Nume',
            'prenume': 'Prenume',
            'email': 'Email',
            'nr_telefon': 'Telefon',
            'salariu': 'Salariu Brut',
            'pct_comision': 'Comision (%)',
            'data_angajarii': 'Data Angajarii',
            'cinema': 'Cinema',
        }
        error_messages = {
            'nume': {'required': 'Introduceti un nume valid.'},
            'pct_comision': {'invalid': 'Introduceti un numar valid.'},
        }

    def clean_nr_telefon(self):
        nr_telefon = self.cleaned_data.get('nr_telefon')
        if nr_telefon and len(str(nr_telefon)) != 9:
            raise forms.ValidationError("Numarul de telefon (fara prefix) trebuie sa aiba exact 9 cifre.")
        return nr_telefon

    def clean_pct_comision(self):
        pct_comision = self.cleaned_data.get('pct_comision')
        if pct_comision < 0 or pct_comision > 100:
            raise forms.ValidationError("Comisionul trebuie sa fie intre 0% si 100%.")
        return pct_comision / 100

    def clean_zile_vacanta(self):
        zile_vacanta = self.cleaned_data.get('zile_vacanta')
        if zile_vacanta <= 0 or zile_vacanta > 365:
            raise forms.ValidationError("Numarul de zile de vacanta trebuie sa fie intre 1 si 365.")
        return zile_vacanta

    def clean(self):
        cleaned_data = super().clean()
        nume = cleaned_data.get('nume')
        prenume = cleaned_data.get('prenume')
        if nume == prenume:
            raise forms.ValidationError("Numele si prenumele nu pot fi identice.")
        return cleaned_data

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "nume", "prenume", "telefon", "adresa", "data_nasterii", "gen", "ocupatie", "password1", "password2")

    def clean_telefon(self):
        telefon = self.cleaned_data.get('telefon')
        if telefon and not telefon.isdigit():
            raise forms.ValidationError("Numarul de telefon trebuie sa contina doar cifre.")
        return telefon

    def clean_data_nasterii(self):
        data_nasterii = self.cleaned_data.get('data_nasterii')
        if data_nasterii and data_nasterii.year < 1900:
            raise forms.ValidationError("Anul nasterii trebuie sa fie dupa 1900.")
        return data_nasterii
    
    def clean_ocupatie(self):
        ocupatie = self.cleaned_data.get('ocupatie')
        if ocupatie and len(ocupatie) < 3:
            raise forms.ValidationError("Ocupația trebuie să conțină cel puțin 3 caractere.")
        return ocupatie

class CustomLoginForm(AuthenticationForm):
    ramane_logat = forms.BooleanField(required=False, initial=False, label='Rămâi logat')

class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')
        if len(password) < 8:
            raise forms.ValidationError("Parola trebuie să aibă cel puțin 8 caractere.")
        return password

TEMPLATE_CATEGORII = {
    'Electronice': 'email_promo_electronice.html',
    'Haine': 'email_promo_haine.html',
}

class PromotieForm(forms.ModelForm):
    categorii = forms.ModelMultipleChoiceField(
        queryset=Categorii.objects.filter(nume__in=TEMPLATE_CATEGORII.keys()),  # Doar categoriile cu template-uri
        widget=forms.CheckboxSelectMultiple,
        initial=lambda: Categorii.objects.filter(nume__in=TEMPLATE_CATEGORII.keys()),
        label="Categorii pentru promoție"
    )

    class Meta:
        model = Promotii
        fields = ['nume', 'data_expirare', 'subiect', 'mesaj', 'reducere_procentuala', 'suma_minima_comanda', 'categorii']
        widgets = {
            'data_expirare': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }