from django.db import models

class Terapist(models.Model):
    first_name = models.CharField("Nombre", max_length=30)
    last_name = models.CharField("Apellido", max_length=30)
    phone_number = models.CharField("Telefono", max_length=30, blank=True, null=True)
    email = models.CharField("Mail", max_length=50, unique=True)
    professional_registration = models.CharField("Matricula", max_length=30, unique=True)
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)