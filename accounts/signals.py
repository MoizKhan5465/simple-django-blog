from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()


@receiver(post_save,sender=User)
def send_welcome_email(sender,instance,created,**kwargs):
    try:
        if created:
            print(f"New user created: {instance.username}")
            subject = "Welcome to our website"
            message = f"Hello {instance.first_name}, welcome to our platform!"
            send_mail(
                subject,
                message,
                "moizsardar056@gmail.com",
                [instance.email],
                fail_silently=False


            )
    except Exception as e:
        print(f"Error sending email: {e}")
            