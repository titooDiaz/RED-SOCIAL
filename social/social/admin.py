from django.contrib import admin
from .models import SocialPost, SocialComment, Image,NotificationSocial

admin.site.register(SocialPost)
admin.site.register(SocialComment)
admin.site.register(Image)
admin.site.register(NotificationSocial)
