import schedule
import time
import django
import os
import logging
from django.core.mail import send_mail
from datetime import timedelta
from django.utils.timezone import now
from .models import CustomUser


logger = logging.getLogger('django')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'laborator_django.settings')
django.setup()

def delete_unconfirmed_users():
    users_to_delete = CustomUser.objects.filter(email_confirmat=False)
    count = users_to_delete.count()
    if count > 0:
        users_to_delete.delete()
        logger.info(f"{count} utilizatori neconfirmati au fost stersi.")
    else:
        logger.info("Niciun utilizator neconfirmat nu a fost sters.")

def send_newsletter():
    users = CustomUser.objects.filter(email_confirmat=True, date_joined__lte=now() - timedelta(minutes=1))
    if users.exists():
        for user in users:
            send_mail(
                subject="Newsletter saptamanal",
                message="Newsletter-ul saptamanal. Bla bla bla",
                from_email="viceroyow@gmail.com",
                recipient_list=[user.email],
                fail_silently=False,
            )
            logger.info(f"Newsletter trimis către {user.username} ({user.email}).")
    else:
        logger.info("Niciun utilizator eligibil pentru newsletter.")

def log_system_health():
    logger.debug("Sistemul functioneaza corect.")

def generate_weekly_report():
    logger.info("Raport zilnic generat cu succes.")
