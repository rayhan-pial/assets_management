from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name


@receiver(post_save, sender = User)
def create_company_for_user(sender, instance, created, **kwargs):
    if created:
        Company.objects.create(user=instance, company_name=instance.email)
