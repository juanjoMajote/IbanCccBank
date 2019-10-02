from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Client(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    name = models.CharField(max_length=100, verbose_name='Nombre')
    surnames = models.CharField(max_length=200, null=True, blank=True, verbose_name='Apellidos')
    iban = models.CharField(max_length=200,unique=True, null=True, blank=True, verbose_name='Iban')
    phone = models.CharField(validators=[phone_regex], max_length=14, null=True, blank=True, verbose_name='Telefono') # validators should be a list
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='Email')
    userCreated = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='PartnerUser',)
    updated = models.DateTimeField(auto_now=True,null=True, blank=True, verbose_name="Fecha Modificación")
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True, verbose_name="Fecha Creación")
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['name']

    def __str__(self):
        return self.name