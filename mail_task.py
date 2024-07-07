from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail

from celeryproject import settings
@shared_task(bind=True)
def test_mail(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_sub="Hello Everyone"
        m="Good Morning"
        to_email=user.email
        send_mail(
            subject=mail_sub,
            message=m,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "done"