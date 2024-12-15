import datetime
from datetime import datetime, date, timedelta
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.sitemaps import Sitemap
from django.core.mail import send_mail, send_mass_mail, mail_admins
from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q, Count
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from django.views.decorators.cache import never_cache
from .forms import ContactViewForm, FilmeFilterForm, ContactForm, AngajatiForm, CustomUserCreationForm, CustomLoginForm, CustomPasswordChangeForm, PromotieForm
import json
import logging
from .models import Cinemauri, Angajati, Sali, Filme, Difuzari, Achizitii, Bilete, CustomUser, Produse, Vizualizari
import os
import re
import time

# Create your views here.

logger = logging.getLogger('django')

nr_total_accesari = 0

def index(request):
    global nr_total_accesari
    nr_total_accesari += 1
    return HttpResponse("Primul raspuns")

def pag1(request):
    global nr_total_accesari
    nr_total_accesari += 1
    return HttpResponse(2+3)

l = []
def pag2(request):
    global l
    global nr_total_accesari
    nr_total_accesari += 1
    a = request.GET.get("a",10)
    print(request.GET)
    l.append(a)
    return HttpResponse(f"<b>Am primit<b>: {l}")

def mesaj(request):
    global nr_total_accesari
    nr_total_accesari += 1
    return HttpResponse("Buna ziua!")

current_time = now()
def data(request):
    global nr_total_accesari
    nr_total_accesari += 1
    return HttpResponse(current_time)

def nr_accesari(request):
    global nr_total_accesari
    nr_total_accesari += 1
    return HttpResponse(nr_total_accesari)

def suma(request):
    global nr_total_accesari
    nr_total_accesari += 1
    a = int(request.GET.get("a", 0))
    b = int(request.GET.get("b", 0))
    return HttpResponse(a+b)

texts = []
def text(request):
    global nr_total_accesari
    nr_total_accesari += 1
    global texts
    t = request.GET.get("t", "")
    if t.isalpha():
        texts.append(t)
    paragraphs = "".join([f"<p>{txt}</p>" for txt in texts])
    return HttpResponse(paragraphs)

def nr_parametri(request):
    global nr_total_accesari
    nr_total_accesari += 1
    return HttpResponse(len(request.GET))

def operatie(request):
    global nr_total_accesari
    nr_total_accesari += 1
    a = int(request.GET.get("a", 0))
    b = int(request.GET.get("b", 0))
    op = request.GET.get("op", "sum")
    if op == "sum":
        result = a + b
    elif op == "dif":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        result = a / b if b != 0 else "Impartire la 0!"
    elif op == "mod":
        result = a % b if b != 0 else "Modulo cu 0!"
    else:
        result = "Operatie necunoscuta!"
    return HttpResponse(result)

def tabel(request):
    global nr_total_accesari
    nr_total_accesari += 1
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    table_html = "<table border='1'>"
    for row in matrix:
        table_html += "<tr>" + "".join([f"<td>{col}</td>" for col in row]) + "</tr>"
    table_html += "</table>"
    return HttpResponse(table_html)

def lista(request):
    global nr_total_accesari
    nr_total_accesari += 1
    words = ["apple", "banana", "cherry", "date", "fig"]
    highlight = request.GET.get("cuvinte", "").split(',')
    list_html = "<ul>"
    for word in words:
        if word in highlight:
            list_html += f"<li style='color:red'>{word}</li>"
        else:
            list_html += f"<li>{word}</li>"
    list_html += "</ul>"
    return HttpResponse(list_html)

elevi = []
def elev(request):
    global nr_total_accesari
    nr_total_accesari += 1
    global elevi
    nume = request.GET.get("nume", "")
    prenume = request.GET.get("prenume", "")
    clasa = int(request.GET.get("clasa", 0))
    if nume and prenume and clasa:
        elevi.append({"nume": nume, "prenume": prenume, "clasa": clasa})
    if not elevi:
        return HttpResponse("Nu sunt elevi inregistrati.")
    elevi_ordonati = sorted(elevi, key=lambda x: (x["clasa"], x["nume"], x["prenume"]))
    clasa_mica = elevi_ordonati[0]["clasa"]
    clasa_mare = elevi_ordonati[-1]["clasa"]
    elevi_clasa_mica = [elev for elev in elevi_ordonati if elev["clasa"] == clasa_mica]
    elevi_clasa_mare = [elev for elev in elevi_ordonati if elev["clasa"] == clasa_mare]
    response = f"Elevii din clasa cea mai mica (clasa {clasa_mica}):<br>"
    for elev in elevi_clasa_mica:
        response += f"{elev['nume']} {elev['prenume']}<br>"
    response += f"<br>Elevii din clasa cea mai mare (clasa {clasa_mare}):<br>"
    for elev in elevi_clasa_mare:
        response += f"{elev['nume']} {elev['prenume']}<br>"
    return HttpResponse(response)

accesari = 0
suma_numere = 0
def aduna_numere(request, path):
    global accesari
    global suma_numere
    accesari += 1
    suma_numere += int(re.findall(r'\d+', path)[-1])
    return HttpResponse(f"numar cereri: {accesari} suma numere: {suma_numere}")

def afiseaza_liste(request):
    dict_param = request.GET
    response = ""
    for i in dict_param.keys(): 
        lista_param = request.GET.getlist(i)
        response += f"{i}:<ul>"
        for j in lista_param:
            response += f"<li>{j}</li>"
        response += "</ul>"
    return HttpResponse(response)

# http://localhost:8000/aplicatie1/nume_corect/Matei-Stefan%20Ungureanu/
# %20 in loc de spatiu
def numara_nume(request, path):
    nr = len(re.findall(r'\s|-', path)) + 1
    return HttpResponse(nr)

def cauta_subsir(request, path):
    nr = len(re.search(r'[ab]+', path).group())
    return HttpResponse(nr)

def afiseaza_operatii(request):
    d = {
        "lista": [
            {"a": 10, "b": 20, "operatie": "suma"},
            {"a": 40, "b": 20, "operatie": "diferenta"},
            {"a": 25, "b": 30, "operatie": "suma"},
            {"a": 40, "b": 30, "operatie": "diferenta"},
            {"a": 100, "b": 50, "operatie": "diferenta"},
        ]
    }
    for elem in d["lista"]:
        if elem["operatie"] == "suma":
            elem["rezultat"] = elem["a"] + elem["b"]
        elif elem["operatie"] == "diferenta":
            elem["rezultat"] = elem["a"] - elem["b"]
    return render(request, 'dictionar_lista.html', d)

# from .models import Prajitura
# def afis_prajituri(request):
#     return render(request, "prajituri.html",
#         {
#             "prajituri": Prajitura.objects.all()
#         }
#     )

def filtrare_filme(request):
    filme = Filme.objects.all()
    nume_film = request.GET.get('nume_film')
    if nume_film:
        filme = filme.filter(nume_film__icontains=nume_film)
    min_durata = request.GET.get('min_durata')
    max_durata = request.GET.get('max_durata')
    if min_durata and max_durata:
        filme = filme.filter(durata__gte=min_durata, durata__lte=max_durata)
    min_rating = request.GET.get('min_rating')
    max_rating = request.GET.get('max_rating')
    if min_rating and max_rating:
        filme = filme.filter(rating__gte=min_rating, rating__lte=max_rating)
    regizor = request.GET.get('regizor')
    if regizor:
        filme = filme.filter(regizor__icontains=regizor)
    min_anul_lansarii = request.GET.get('min_anul_lansarii')
    max_anul_lansarii = request.GET.get('max_anul_lansarii')
    if min_anul_lansarii and max_anul_lansarii:
        filme = filme.filter(anul_lansarii__year__gte=min_anul_lansarii, anul_lansarii__year__lte=max_anul_lansarii)
    paginator = Paginator(filme, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    response_text = f"Pagina {page_obj.number} din {page_obj.paginator.num_pages}<br>"
    response_text += f"Total filme: {page_obj.paginator.count}<br><br>"
    filme_text = "<br>".join(str(film) for film in page_obj)
    response_text += filme_text
    return HttpResponse(response_text)

def mesaj_trimis(request):
    return HttpResponse("Mesajul s-a trimis")

def contact_view(request):
    if request.method == 'POST':
        form = ContactViewForm(request.POST)
        if form.is_valid():  
            nume = form.cleaned_data['nume']
            email = form.cleaned_data['email']
            mesaj = form.cleaned_data['mesaj']
            print(1)
            return redirect('mesaj_trimis')
    else:
        form = ContactViewForm()
    return render(request, 'contact.html', {'form': form})

def filtrare_filme_2(request):
    if request.method == 'POST':
        filme = Filme.objects.all().order_by('id')
        form = FilmeFilterForm(request.POST)
        if form.is_valid():
            nume_film = form.cleaned_data.get('nume_film')
            if nume_film:
                filme = filme.filter(nume_film__icontains=nume_film)
            min_durata = form.cleaned_data.get('min_durata')
            max_durata = form.cleaned_data.get('max_durata')
            if min_durata is not None and max_durata is not None:
                filme = filme.filter(durata__gte=min_durata, durata__lte=max_durata)
            min_rating = form.cleaned_data.get('min_rating')
            max_rating = form.cleaned_data.get('max_rating')
            if min_rating is not None and max_rating is not None:
                filme = filme.filter(rating__gte=min_rating, rating__lte=max_rating)
            regizor = form.cleaned_data.get('regizor')
            if regizor:
                filme = filme.filter(regizor__icontains=regizor)
            min_anul_lansarii = form.cleaned_data.get('min_anul_lansarii')
            max_anul_lansarii = form.cleaned_data.get('max_anul_lansarii')
            if min_anul_lansarii is not None and max_anul_lansarii is not None:
                filme = filme.filter(anul_lansarii__year__gte=min_anul_lansarii, anul_lansarii__year__lte=max_anul_lansarii)
    else:
        form = FilmeFilterForm()
        filme = Filme.objects.all().order_by('id')
    return render(request, 'filme_filtrare.html', {
        'form': form,
        'filme': filme
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data_formular = form.cleaned_data.copy()
            mesaj = data_formular.get('mesaj', '')
            mesaj = ' '.join(mesaj.split())
            data_formular['mesaj'] = mesaj
            data_nasterii = data_formular.get('data_nasterii')
            if data_nasterii:
                today = date.today()
                ani = today.year - data_nasterii.year
                luni = today.month - data_nasterii.month
                if luni < 0:
                    ani -= 1
                    luni += 12
                data_formular['varsta'] = f"{ani} ani si {luni} luni"
                data_formular.pop('data_nasterii')
            data_formular.pop('confirmare_email')
            mesaje_folder = os.path.join(settings.BASE_DIR, 'mesaje')
            if not os.path.exists(mesaje_folder):
                os.makedirs(mesaje_folder)
            timestamp = int(time.time())
            fisier_nume = f"mesaj_{timestamp}.json"
            fisier_cale = os.path.join(mesaje_folder, fisier_nume)
            with open(fisier_cale, 'w', encoding='utf-8') as fisier_json:
                json.dump(data_formular, fisier_json, ensure_ascii=False, indent=4)
            return redirect('mesaj_trimis')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def creare_angajati(request):
    if not request.user.has_perm('aplicatie1.view_angajati'):
        return HttpResponseForbidden(render(request, '403.html', {
            'titlu': "Eroare adaugare angajati",
            'mesaj': "Nu ai voie sa adaugi angajati.",
        }))
    if request.method == 'POST':
        form = AngajatiForm(request.POST)
        if form.is_valid():
            angajat = form.save(commit=False)
            nivel_studii = form.cleaned_data['nivel_studii']
            angajat.salariu += (int(nivel_studii[0])-1) * 0.1 * angajat.salariu
            zile_vacanta = form.cleaned_data['zile_vacanta']
            angajat.salariu -= 237 * (zile_vacanta - 21)
            angajat.save()
            messages.success(request, "Angajatul a fost adaugat.")
            return redirect('lista_angajati')
    else:
        form = AngajatiForm()
    return render(request, 'creare_angajati.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            if username == 'admin':
                logger.critical("Tentativa de inregistrare cu username-ul 'admin'.")
                messages.critical(request, "Tentativa de inregistrare cu username-ul 'admin'.")
                adresa = form.cleaned_data['email']
                subject="Cineva incearca sa ne preia site-ul"
                message=f'Logare admin neautorizata de pe adresa {adresa}'
                html_message=f"""
                    <h1 style="color:red;">{subject}</h1>
                    <p><strong>Logare admin neautorizata</strong></p>
                    <p>Adresa: {adresa}</p>
                """
                mail_admins(subject, message, html_message=html_message, fail_silently=False)
                return HttpResponse("'admin' nu e un username valabil.")
            user.cod = get_random_string(50)
            user.is_active = False
            user.save()
            confirm_url = request.build_absolute_uri(f"/aplicatie1/confirm_email/{user.cod}/")
            email_message = render_to_string('email_confirmation.html', {
                'user': user,
                'confirm_url': confirm_url,
            })
            send_mail(
                'Confirma-ti adresa de e-mail',
                '',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                html_message=email_message,
            )
            logger.info(f"Utilizator creat: {user.username} | email: {user.email}.")
            messages.success(request, f"Contul tau a fost creat cu succes.")
            return redirect('user_login')
        else:
            logger.error("Formularul de inregistrare nu este valid.")
            messages.error(request, "Formularul de inregistrare nu este valid.")
    else:
        form = CustomUserCreationForm()
        logger.debug("Formularul de inregistrare a fost initializat.")
        messages.debug(request, "Formularul de inregistrare a fost initializat.")
    return render(request, 'register.html', {'form': form})

def confirm_email(request, cod):
    try:
        user = CustomUser.objects.get(cod=cod)
        if not user.email_confirmat:
            user.email_confirmat = True
            user.is_active = True
            user.save()
            logger.info(f"Email confirmat pentru utilizatorul {user.username}.")
            return render(request, 'email_confirmed.html', {'user': user})
        else:
            logger.warning(f"Email deja confirmat pentru utilizatorul {user.username}.")
            messages.warning(request, f"Email deja confirmat pentru utilizatorul {user.username}.")
            # return render(request, 'email_confirmed.html') #, {'message': 'E-mailul a fost deja confirmat.'})
    except CustomUser.DoesNotExist:
        logger.error(f"Cod invalid sau utilizator inexistent: {cod}")
        messages.error(request, f"Cod invalid sau utilizator inexistent: {cod}")
    return render(request, 'email_confirmed.html') #, {'message': 'Cod invalid sau utilizator inexistent.'})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
    logger.debug(f"IP client detectat: {ip}")
    return ip

failed_logins = {}
def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST, request=request)
        if form.is_valid():
            user = form.get_user()
            if user.blocat:
                messages.error(request, "Contul tau a fost blocat. Nu te poti autentifica.")
                return redirect('user_login')
            login(request, user)
            logger.info(f"Autentificare reusita pentru utilizatorul {user.username}.")
            username = form.cleaned_data.get('username')
            if username in failed_logins:
                del failed_logins[username]
            if not form.cleaned_data.get('ramane_logat'):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(86400)
            messages.success(request, "Te-ai logat cu succes.")
            return redirect('profile')
        else:
            username = request.POST.get('username')
            ip_address = get_client_ip(request)
            current_time = now()
            if username not in failed_logins:
                failed_logins[username] = []
            failed_logins[username].append((ip_address, current_time))
            failed_logins[username] = [
                (ip, time) for ip, time in failed_logins[username]
                if (current_time - time) < datetime.timedelta(minutes=2)
            ]
            if len(failed_logins[username]) >= 3:
                subject = "Logari suspecte"
                message = f"Username: {username}\nIP: {ip_address}"
                html_message = f"""
                    <h1 style="color: red;">{subject}</h1>
                    <p>Username: {username}</p>
                    <p>IP: {ip_address}</p>
                """
                mail_admins(subject, message, html_message=html_message, fail_silently=False)
                logger.critical(f"Logari suspecte detectate pentru utilizatorul {username} de la IP: {ip_address}.")
                messages.critical(request, f"Logari suspecte detectate pentru utilizatorul {username} de la IP: {ip_address}.")
    else:
        
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
@never_cache
def profile(request):
    user_data = {
        "username": request.user.username,
        "email": request.user.email,
        "telefon": request.user.telefon,
        "adresa": request.user.adresa,
        "data_nasterii": request.user.data_nasterii.strftime('%Y-%m-%d') if isinstance(request.user.data_nasterii, date) else None,
        "gen": request.user.gen,
        "ocupatie": request.user.ocupatie,
    }
    request.session['user_data'] = user_data
    logger.debug(f"Profil accesat de utilizatorul {request.user.username}.")
    return render(request, 'profile.html', {'user_data': user_data})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            logger.info(f"Parola schimbata pentru utilizatorul {request.user.username}.")
            messages.success(request, "Parola a fost schimbata cu succes.")
            return redirect('profile')
        else:
            logger.warning(f"Schimbarea parolei esuata pentru utilizatorul {request.user.username}.")
            messages.warning(request, "A aparut o eroare. Va rugam sa verificati datele.")
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

def user_logout(request):
    logger.info(f"Utilizatorul {request.user.username} s-a deconectat.")
    messages.success(request, "Te-ai delogat cu succes.")
    logout(request)
    return redirect('user_login')

def adauga_vizualizare(request):
    utilizator_username = request.GET.get('utilizator_username')
    produs_nume = request.GET.get('produs_nume')
    if not utilizator_username or not produs_nume:
        logger.warning("Parametri lipsa pentru adaugarea unei vizualizari.")
        return HttpResponse("Eroare: Parametrii 'utilizator_username' si 'produs_nume' sunt necesari!", status=400)
    try:
        utilizator = CustomUser.objects.get(username__iexact=utilizator_username)
        produs = Produse.objects.get(nume__iexact=produs_nume)
    except CustomUser.DoesNotExist:
        logger.error(f"Utilizator inexistent: {utilizator_username}")
        return HttpResponse("Eroare: Utilizatorul cu username-ul furnizat nu exista!", status=404)
    except Produse.DoesNotExist:
        logger.error(f"Produs inexistent: {produs_nume}")
        return HttpResponse("Eroare: Produsul cu numele furnizat nu exista!", status=404)
    except Exception as e:
        logger.critical(f"Eroare grava in adauga_vizualizare: {e}")
        subject = "Eroare in functia adauga_vizualizare"
        message = f"Eroare: {str(e)}"
        html_message = f"""
            <h1 style="color: red;">{subject}</h1>
            <p style="background-color: red; color: white;">{str(e)}</p>
        """
        mail_admins(subject, message, html_message=html_message, fail_silently=False)
        return HttpResponse("A aparut o eroare interna. Administratorii au fost notificati.", status=500)
    Vizualizari.objects.create(utilizator=utilizator, produs=produs)
    logger.debug(f"Vizualizare adaugata: utilizator={utilizator.username}, produs={produs.nume}.")
    vizualizari = Vizualizari.objects.filter(utilizator=utilizator).order_by('-data_vizualizare')
    if vizualizari.count() > 5:
        for vizualizare in vizualizari[5:]:
            vizualizare.delete()
            logger.info(f"Vizualizare veche stearsa pentru utilizatorul {utilizator.username}.")
    return HttpResponse("Vizualizare adaugata cu succes!", status=200)

def promotie_lansata(request):
    return HttpResponse("Promotie lansata cu succes!")

TEMPLATE_CATEGORII = {
    'Electronice': 'email_promo_electronice.html',
    'Haine': 'email_promo_haine.html',
}

def pagina_promotii(request):
    if request.method == 'POST':
        form = PromotieForm(request.POST)
        if form.is_valid():
            promotie = form.save()
            logger.info(f"Promotie creata: {promotie.nume}")
            messages.success(f"Promotie creata: {promotie.nume}")
            categorii_selectate = form.cleaned_data['categorii']
            k = 3
            datatuple = []
            for categorie in categorii_selectate:
                utilizatori = (
                    Vizualizari.objects.filter(produs__categorie=categorie.nume)
                    .values('utilizator')
                    .annotate(numar_vizualizari=Count('utilizator'))
                    .filter(numar_vizualizari__gte=k)
                )
                print(utilizatori)
                for utilizator in utilizatori:
                    try:
                        user = CustomUser.objects.get(id=utilizator['utilizator'])
                        print(user.username)
                        template = TEMPLATE_CATEGORII.get(categorie.nume, 'email_promo.html')
                        email_message = render_to_string(template, {
                            'subiect': promotie.subiect,
                            'user': user.username,
                            'mesaj': promotie.mesaj,
                            'data_expirare': promotie.data_expirare,
                        })
                        datatuple.append((
                            promotie.subiect,
                            email_message,
                            'viceroyow@gmail.com',
                            [user.email],
                        ))
                        logger.debug(f"Email pregatit pentru utilizatorul {user.username} la categoria {categorie.nume}.")
                        messages.debug(request, f"Email pregatit pentru utilizatorul {user.username} la categoria {categorie.nume}.")
                    except Exception as e:
                        logger.error(f"Eroare la pregatirea emailului pentru utilizatorul {user.username}: {e}")
                        messages.error(request, f"Eroare la pregatirea emailului pentru utilizatorul {user.username}: {e}")
            send_mass_mail(datatuple, fail_silently=False)
            logger.info(f"Emailuri trimise pentru promotia {promotie.nume}.")
            messages.success(request, f"Emailuri trimise pentru promotia {promotie.nume}.")
            return redirect('promotie_lansata')
    else:
        form = PromotieForm()
    return render(request, 'promotii.html', {'form': form})

def ofera_permisiune(request):
    if request.user.is_authenticated:
        permission = Permission.objects.get(codename='vizualizeaza_oferta')
        request.user.user_permissions.add(permission)
        logger.info(f"Utilizatorul {request.user.username} a primit permisiunea sa vada oferta.")
        messages.success("Poti vedea oferta.")
        return redirect('oferta')
    return HttpResponseForbidden("Nu ai permisiunea sa accesezi aceasta pagina.")

def oferta(request):
    if request.user.is_authenticated and request.user.has_perm('aplicatie1.vizualizeaza_oferta'):
            logger.info(f"Utilizatorul {request.user.username} si-a luat teapa.")
            return HttpResponse("Teapa! Nu e nicio oferta! ;)")
    return render(request, '403.html', {
        "titlu": "Eroare afisare oferta",
        "mesaj": "Nu ai voie sa vizualizezi oferta.",
    })

@login_required
def block_user(request, user_id):
    if not request.user.groups.filter(name='Moderatori').exists():
        return HttpResponseForbidden("Nu ai permisiunea de a vedea aceasta pagina.")
    user_to_block = get_object_or_404(CustomUser, id=user_id)
    if not user_to_block.blocat:
        user_to_block.blocat = True
        user_to_block.save()
        return HttpResponse('Utilizatorul a fost blocat cu succes.')
    else:
        return HttpResponseForbidden("Utilizatorul este deja blocat.")

@login_required
def unblock_user(request, user_id):
    if not request.user.groups.filter(name='Moderatori').exists():
        return HttpResponseForbidden("Nu ai permisiunea de a vedea aceasta pagina.")
    user_to_block = get_object_or_404(CustomUser, id=user_id)
    if user_to_block.blocat:
        user_to_block.blocat = False
        user_to_block.save()
        return HttpResponse('Utilizatorul a fost deblocat cu succes.')
    else:
        return HttpResponseForbidden("Utilizatorul nu este blocat.")

def cinema_detail(request, id):
    cinema = get_object_or_404(Cinemauri, id=id)
    return render(request, 'cinema_detail.html', {'cinema': cinema})

def angajat_detail(request, id):
    angajat = get_object_or_404(Angajati, id=id)
    return render(request, 'angajat_detail.html', {'angajat': angajat})

def film_detail(request, id):
    film = get_object_or_404(Filme, id=id)
    return render(request, 'film_detail.html', {'film': film})

def produs_detail(request, id):
    produs = get_object_or_404(Produse, id=id)
    return render(request, 'produs_detail.html', {'produs': produs})

def utilizator_detail(request, id):
    utilizator = get_object_or_404(CustomUser, id=id)
    return render(request, 'utilizator_detail.html', {'utilizator': utilizator})

def lista_cinemauri(request):
    cinemauri = Cinemauri.objects.all()
    return render(request, 'lista_cinemauri.html', {'cinemauri': cinemauri})

def lista_angajati(request):
    angajati = Angajati.objects.all()
    return render(request, 'lista_angajati.html', {'angajati': angajati})

def lista_filme(request):
    filme = Filme.objects.all()
    return render(request, 'lista_filme.html', {'filme': filme})

def lista_produse(request):
    produse = Produse.objects.all()
    return render(request, 'lista_produse.html', {'produse': produse})

def lista_utilizatori(request):
    utilizatori = CustomUser.objects.all()
    return render(request, 'lista_utilizatori.html', {'utilizatori': utilizatori})

def cos_virtual(request):
    produse = Produse.objects.all()
    produse_serializate = json.dumps(list(produse.values('id', 'nume', 'pret', 'stoc')), cls=DjangoJSONEncoder)
    return render(request, 'cos_virtual.html', {'produse_json': produse_serializate})