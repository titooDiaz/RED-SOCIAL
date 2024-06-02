#para iniciar el servidor debemos inciiarlo tambien colocando 
#python manage.py tailwind
from pathlib import Path
import os
import environ
#para poder cambiar el idioma 


#lenguajes del humanize
LANGUAGES = [
    ('es', ('Spanish')),
]

#idioma por defecto en espa;ol
LANGUAGE_CODE = 'es'



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#crearemos una variale de ambiente con un archivo .env
#copiamos la secret key (SECRET_KEY = "django-insecure-)t#w_(6@-m&=x9saw&xb7bt!p9m77h^&3+c#cznnd6g_26fj+0" DEBUG = True)
# sin espacios y sin (django-insecure-)
SECRET_KEY = os.environ.get('SECRET_KEY')
#PARA DESPLEGAR CON RENDER
DEBUG = 'RENDER' not in os.environ


#variables de entorno
env = environ.Env()
environ.Env.read_env()
ENVIRONMENT = env
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = [
    '*' #TRABAJAREMOS CON CUALQUIER URL QUE QUIERA ACCEDER AL SITIO
    #aun no tenemos dominio entonces no lo puedo especificar
]

#agregar external host IMPORTANTE PARA RENDER
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #atenticacion de usuarios
    'django.contrib.sites',
    #tiempo...
    'django.contrib.humanize',

    #autenticacion de usuarios
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
############
    'crispy_forms',
    "crispy_tailwind",
############# 
    #apps con django
    'core',
    'social',
    'users',
    #externo de tailwind 
    'tailwind', #python manage.py tailwind init
    'theme',#python manage.py tailwind install *(recordar lo del modo oscuro en theme)
]

#externo de tailwind
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]#despues de ahcer esto colocar #python manage.py tailwind install


CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"


#autenticar usuarios #login o logaut funcione
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# ================ MODIFICAR ALLAUTH ==================== #
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
AUTH_USER_MODEL="users.User"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT =300
# https://docs.allauth.org/en/latest/account/rate_limits.html
ACCOUNT_RATE_LIMITS = {
    'login_failed': "10/m/ip,5/5m/key"
}
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Hgost Media - "

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "account_login"




#AGREGAR NODE JS A NUESTRO ENTORNO DE TRABAJO (recuerda agregarlo al path)
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
NPM_BIN_PATH = "/home/miguel/nodejs/bin/npm" 
#npm install cross-env --save-dev
#npm install tailwindcss --save-dev


MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')], #################
        ############ os.path.join(BASE_DIR, 'templates') ###############
        ################# AGREGADO DESDE EL TECLADO ####################
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


#CONFIGURACION PARA POSTGRESQL
DATABASES = {
    "default": env.db("DATABASE_URL", default="postgres:///red_social"),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

#pip install argon2-cffi
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



#ARCHIVOS DE TODO TIPO CON CONEXION POSGRESQL
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

##correo
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'miguelitodiaz169@gmail.com'
EMAIL_HOST_PASSWORD = 'bxdegfpiqbqksich'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'miguelitodiaz169@gmail.com'


SITE_ID = 1

