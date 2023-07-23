from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from MYpetstagram import settings

UserModel = get_user_model()


def send_successful_registration_email(user):
    html_message = render_to_string('email-greeting.html', {'user': user})
    plain_message = strip_tags(html_message)
    send_mail(
        subject="Registration greetings",
        message=plain_message,
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,),
    )


@receiver(signal=post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        send_successful_registration_email(instance)