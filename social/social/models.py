from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()

POST_STATUS=(
    ('NoPublicado', 'NoPublicado'),
    ('NoRevisado', 'NoRevisado'),
    ('Publicado', 'Publicado'),
)

def user_directory_path(instance, filename):
	return 'users/socialposts/{0}'.format(filename)


class SocialPost(models.Model):
    body=models.TextField()
    #ADMINS
    verified = models.CharField(max_length=100, choices=POST_STATUS, default='NoRevisado')
    body=models.TextField(default='')
    ##################
    image = models.ManyToManyField('Image', blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_post_author')
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    ##### REPORTAR
    reports = models.ManyToManyField(User, blank=True, related_name='reports')

    class Meta:
        ordering = ['-created_on']

#comentarios :D
class SocialComment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_comment_author')
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
    post = models.ForeignKey('SocialPost', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    @property #entramos como porpiedad pq queremos acceder a esto desde el template
    def children(self):
        return SocialComment.objects.filter(parent=self).order_by('-created_on').all()

    @property
    def is_parent(self):#asi sabemos si un comentario tiene o no comentario adentro
        if self.parent is None:
            return True
        return False
    
    

    class Meta:
        ordering = ['-created_on']


class Image(models.Model):
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)



class NotificationSocial(models.Model):
    de = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_sent')
    para = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_received')
    mensaje = models.CharField(max_length=500)
    creat = models.DateTimeField(default=timezone.now)
    post = models.CharField(max_length=50000)

    class Meta:
        ordering = ['-creat']