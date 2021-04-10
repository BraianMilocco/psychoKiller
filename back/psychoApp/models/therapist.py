from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

#   First will be class that need to be overwrite for using the AbstractBaseUser as
#   super class of our Therapist class.
#   Secondly will be the actual Therapist Class


class MyAccountManager(BaseUserManager):
    def create_user(
        self,
        email,
        username,
        last_name,
        professional_registration,
        degree,
        phone_number=None,
        password=None,
    ):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        if not username:
            raise ValueError("The given username must be set")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            last_name=last_name,
            professional_registration=professional_registration,
            degree=degree,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        username,
        last_name,
        professional_registration,
        password,
        degree = "El mas pijudo",
        phone_number=None,
    ):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            last_name=last_name,
            professional_registration=professional_registration,
            degree=degree,
        )
        user.phone_number = None
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self.db)
        return user


# Observations
# is_active in development can be True by default, in actual work should be false, until
# we can confirm that the profesional_registretion is real.


class Therapist(AbstractBaseUser):

    # Our fields
    email = models.CharField("Mail", max_length=50, unique=True)
    # username is something we need because the AbstractBaseUser
    username = models.CharField("Nombre", max_length=30)
    last_name = models.CharField("Apellido", max_length=30)
    phone_number = models.CharField("Telefono", max_length=30, blank=True, null=True)
    professional_registration = models.CharField(
        "Matricula", max_length=30, unique=True
    )
    degree = models.CharField("Título", max_length=50)
    # Fields that need to be overwrite for the extension of AbstracBaseUser
    date_joined = models.DateTimeField(
        verbose_name="Fecha de creacion", auto_now_add=True
    )
    last_login = models.DateField(verbose_name="ultimo logueo", auto_now=True)
    is_admin = models.BooleanField(default=False, verbose_name="es admin")
    is_active = models.BooleanField(default=True, verbose_name="está activo")
    is_staff = models.BooleanField(default=False, verbose_name=" es personal")
    is_superuser = models.BooleanField(default=False, verbose_name="es super usuario")

    # Define To Ask mail in  the login
    USERNAME_FIELD = "email"
    # Define to see which fields are completely required to create a user (must be show in the Account manager)
    REQUIRED_FIELDS = ["username", "last_name", "professional_registration"]
    # Another steps overwrite of the AbstractBaseUser class
    objects = MyAccountManager()

    # Functions to overwrite  of the AbstractBaseUser
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    # Our Functions
    def __str__(self):
        return "%s %s" % (self.username, self.last_name)

    class Meta:
        verbose_name = "Especialista"
        verbose_name_plural = "Especialistas"
