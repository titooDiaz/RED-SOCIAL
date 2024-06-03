from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from users.models import Profile
from django.contrib.auth import get_user_model # todos los modelos de usuarios existentes
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, EditProfileStaticForm
User = get_user_model()
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
#from django.core.cache import cache
import time
from social.forms import NotificationSocialForm

#obligar cache
def timestamp():
    return str(int(time.time() * 1000))

#NOTIFICACIONES
def Notification(userde, userpara, context, ver, request):
    if userde != userpara:
        form = NotificationSocialForm()
        new_notification = form.save(commit=False)
        new_notification.de = userde
        new_notification.post = str(id)
        new_notification.para = userpara
        new_notification.mensaje = context
        new_notification.save()
        return 'EXITOSO'
    else:
        return 'MISMO USUARIO'



#metodo para una clase
class UserProfileView(View):
    def get(self, request, username,*args, **kwargs):
        img=timestamp()
        user = get_object_or_404(User, username=username)
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
        context={
            'img':img,
            'user':user,
            'profile':profile,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
            'follow':follow,
        }
        return render(request, 'users/detail.html', context)

@login_required
def EditProfile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile', username=user.username)
    else:
        form = EditProfileForm(instance=profile)

    # check if user is the owner of the profile being edited
    if profile.user != user:
        return redirect('home')
    img = timestamp()
    context = {
        'img':img,
        'form': form,
    }

    return render(request, 'users/edit.html', context)






def EditProfileStatic(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = EditProfileStaticForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile', username=request.user.username)
    else:
        form = EditProfileStaticForm(instance=profile)
        img = timestamp()
    return render(request, 'users/edit_static.html', {'form': form, 'img':img,})




class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.add(request.user)

        userde = request.user
        userpara = profile.user
        context = f'{userde} comenzo a seguirte'
        ver = profile.user
        Notification(userde, userpara, context, ver, request)

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Usuario segido :D'
        )
        return redirect('users:profile', username=profile.user.username)


class RemoveFollower(LoginRequiredMixin, View):
	def post(self, request, pk, *args, **kwargs):
		profile = Profile.objects.get(pk=pk)
		profile.followers.remove(request.user)
		messages.add_message(
            self.request,
            messages.SUCCESS,
            'Dejaste de seguir al usuario D:'
        )
		return redirect('users:profile', username=profile.user.username)


class ListFollowers(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        followers = profile.followers.all()
        img = timestamp()
        context = {
            'profile': profile,
            'followers': followers,
            'img':img,
        }

        return render(request, 'pages/social/followers_list.html', context)