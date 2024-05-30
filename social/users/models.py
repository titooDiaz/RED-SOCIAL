from django.db import models
#extender usuairos
from django.contrib.auth.models import AbstractUser

#importar mas cosas...
from django.conf import settings # usar los settings
import os
from PIL import Image
from django.db.models.signals import post_save #cuando creamos un usuairo crearemos su perfil



#directorio de foto de perfil
#crear un directorio apra cada usuario (instance al nombre de usuario, filename al nombre del archivo)
def user_directory_path_profile(instance, filename):
    # el cero es el format
    profile_picture_name = 'users/{0}/profile.jpg'.format(instance.user.username)
    #que archivo guardamos..
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    #si el full_path existe lo sacamos y ponemos otro
    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name

#directorio de banner
def user_directory_path_banner(instance, filename):
    profile_picture_name = 'users/{0}/banner.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name


VERIFICATION_OPTIONS=(
    ('unverified', 'unverified'),
    ('teacher', 'teacher'),
    ('verified', 'verified'),
    ('admin', 'admin'),
)


class User(AbstractUser):
    stripe_customer_id = models.CharField(max_length=50) # intercambio entre usuarios
    #esto es para poder hacer trading


class Profile(models.Model): # este es el perfil
    # en este modelo vamos a sacar las cosas que queremos extender :3

    #cada perfil esta vinculado a un usuario... (OneToOneField - un perfil tiene un usuario)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #imagen de perfil (ya esta trabajando en media (upload_to=user_directory_path_profile - cada usuario tendra su propia carpeta))
    picture = models.ImageField(default='users/user_default_profile.png', upload_to=user_directory_path_profile, null=True, blank=True)
    #banner
    banner = models.ImageField(default='users/user_default_bg.png', upload_to=user_directory_path_banner, null=True, blank=True)
    #admin? variables definidas arriba
    verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='verified')
    #monedas- decimal field significa numeros, blank - por lo menos 0
    coins = models.DecimalField(max_digits=19, decimal_places=2, default=0, blank=False)
    
    followers = models.ManyToManyField(User, blank=True, related_name="followers")

    
    #fecha de registro, automaticamente se agrega la fecha cuando se crea el user
    date_created = models.DateField(auto_now_add=True)

    #name
    name = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)

    #User info - completa el usuario
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=150, null=True, blank=True)

    def __str__(self):
        #para el admin
        return self.user.username

# se;al cuando el usuario se registre
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # si el usuario se cre, creamos una instancia del perfil
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# created profile
post_save.connect(create_user_profile, sender=User)
# save created profile
post_save.connect(save_user_profile, sender=User)
