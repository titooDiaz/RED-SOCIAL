#para iniciar el servidor debemos inciiarlo tambien colocando 
#python manage.py tailwind
from pathlib import Path
import os
import environ
#para poder cambiar el idioma 
from django.utils.translation import gettext_lazy as _


#lenguajes del humanize
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
]

#idioma por defecto en espa;ol
LANGUAGE_CODE = 'es'



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#crearemos una variale de ambiente con un archivo .env
#copiamos la secret key (SECRET_KEY = "django-insecure-)t#w_(6@-m&=x9saw&xb7bt!p9m77h^&3+c#cznnd6g_26fj+0" DEBUG = True)
# 333sin espacios y sin (django-insecure-)
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
#modelo para inicio de sec..
    'accounts',

    
    #apps con django
    'core',
    'social',
    'users',


    #externo de tailwind 
    'tailwind', #python manage.py tailwind init
    'theme',#python manage.py tailwind install *(recordar lo del modo oscuro en theme)
]

#autenticacion de usuario...
SITE_ID = 1

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
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT =300
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "account_login"




#AGREGAR NODE JS A NUESTRO ENTORNO DE TRABAJO (recuerda agregarlo al path)
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"


MIDDLEWARE = [
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


############### EJECUTANTO DJANGO CON WSGI ##################
#(DESPLEGAR CON CALQUIER SERVICIO)
WSGI_APPLICATION = "core.wsgi.application"


#CONFIGURACION PARA POSTGRESQL
DATABASES = {
    "default": env.db("DATABASE_URL", default="postgres:///PeriodicoCoal"),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True


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


LANGUAGE_CODE = "en-us"

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

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'


####################################################################
#conexion con aws
if not DEBUG:
    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = env('EMAIL_PORT')
    EMAIL_USE_TLS = env('EMAIL_USE_TLS')

    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # django-ckeditor will not work with S3 through django-storages without this line in settings.py
    AWS_QUERYSTRING_AUTH = False

    # aws settings

    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')


    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_DEFAULT_ACL = 'public-read'

    # s3 static settings

    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # s3 public media settings

    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'core.storage_backends.MediaStore'

    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    #descargar finalmente (pip install django-tailwind) E IR A LA LINEA DE APPS INSTALADAS


