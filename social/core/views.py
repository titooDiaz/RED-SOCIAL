from social.models import Image, SocialPost, SocialComment
from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin # si alguien no inicia su cuenta se va al login
from social.forms import SocialPostForm
import time
from users.models import Profile

from social.models import NotificationSocial, SocialPost


#obligar cache
def timestamp():
    return str(int(time.time() * 1000))



#eliminar notidicacion
class notification_redirect(View):
    def get(self, request, dato, notification_id, *args, **kwargs):
        # Obtener la notificación
        notification = NotificationSocial.objects.get(pk=notification_id)
        
        if notification.mensaje == f'{notification.de} comenzo a seguirte':
            # Eliminar notifi...
            notification.delete()
            # Redirigir a la página del post
            return redirect('users:profile', username=notification.de)
        else:
            # Eliminar notifi...
            notification.delete()
            # Redirigir a la página del post
            post = SocialPost.objects.get(pk=int(dato))
            return redirect('social:post-detail', pk=int(post.pk))
    
class notifications_delete(View):
    def get(self, request, user, *args, **kwargs):
        # Obtener las notificaciones
        notifications = NotificationSocial.objects.filter(para=user)
        notifications.delete()
        return redirect('home')


class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        #notificaciones
        SocialNotification = NotificationSocial.objects.filter(para=request.user)

        posts = SocialPost.objects.all()
        #para ver solamente a los que seguimos:
        form = SocialPostForm()
        img=timestamp()

        user = request.user
        profile = Profile.objects.get(user=user)

        followers = profile.followers.all()
        follow = profile.followers.all()

        if len(followers) == 0:
                is_following = False
            
        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)

        context = {
            'user':user,
            'profile':profile,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
            'follow':follow,
            'img':img,
            'posts':posts,
            'form':form,
            'SocialNotification': SocialNotification,
            #notification (poder eliminar) abajo
        }
        return render(request, 'pages/index.html', context)

    def post(self, request, *args, **kwargs):
        logged_in_user=request.user

        posts = SocialPost.objects.all()

        form = SocialPostForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = logged_in_user
            new_post.save()

            for f in files:
                img = Image(image=f)
                img.save()
                new_post.image.add(img)

            new_post.save()
        context={
            'posts':posts,
            'form':form
        }
        return render(request, 'pages/index.html', context)