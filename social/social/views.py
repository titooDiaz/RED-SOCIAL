from social.forms import SocialCommentForm, NotificationSocialForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic.base import View
from .models import SocialPost, SocialComment, User
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from users.models import Profile
from django.http import JsonResponse
import json

#crear un html desde la vista
from django.template import loader

from django.db.models import Q #importar datos de la base de datos
import time

#para poder cambiar el idioma
from django.utils.translation import activate

import datetime



#NOTIFICACIONES
def Notification(userde, userpara, context, ver, request):
    if userde != userpara:
        form = NotificationSocialForm()
        new_notification = form.save(commit=False)
        new_notification.de = userde
        id = int(ver)
        new_notification.post = str(id)
        new_notification.para = userpara
        new_notification.mensaje = context
        new_notification.save()
        return 'EXITOSO'
    else:
        return 'MISMO USUARIO'



#obligar cache
def timestamp():
    return str(int(time.time() * 1000))


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        activate('es')  # Establece el contexto de traducción en español
        post = SocialPost.objects.get(pk=pk)
        form = SocialCommentForm()

        comments = SocialComment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments':comments
        }

        return render(request, 'pages/social/detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        activate('es')  # Establece el contexto de traducción en español
        post = SocialPost.objects.get(pk=pk)
        form = SocialCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            ###########################
            userde = request.user
            userpara = post.author
            context = f'{userde} agrego un comentario'
            ver = post.pk
            Notification(userde, userpara, context, ver, request)
            ###########################
            new_comment.save()
        else:
            print(form.errors," ERROR EN LA SOLICITUD DE INTRODUCIR DATOS A LA BASE DE DATOS")

        comment = SocialComment.objects.filter(pk=new_comment.pk).order_by('-created_on')#comentario creado
        context = {
            'post': post,
            'form': form,
            'comments':comment
        }

        html = render(request, 'pages/social/comment_ajax.html', context)
        #print(html) --> TENEMOS EL DOCUEMNTO HTML CORRECTAMENTE!

        comments = SocialComment.objects.filter(post=post).order_by('-created_on')
        comments_data = [{'text': comment.comment, 'author': comment.author.username} for comment in comments]
        html_content = html.content.decode('utf-8')  # Obtener el contenido HTML como una cadena
        #print(html_content) --> LITERALMENTE EL HTML QUE NECESITAMOS RESPONDER!

        response_data = {
            'comments': comments_data,
            'html_generado': html_content,
        }
        return JsonResponse(response_data)



#VISTA DE VIDEOS MULTIMEDIA
class HomeMediaView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        posts = SocialPost.objects.all()
        #para ver solamente a los que seguimos:
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
            #notification (poder eliminar) abajo
        }
        return render(request, 'pages/index.html', context)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    activate('es')  # Establece el contexto de traducción en español
    model=SocialPost
    fields=['body']
    template_name='pages/social/edit.html'

    def get_success_url(self):
        activate('es')  # Establece el contexto de traducción en español
        pk = self.kwargs['pk']
        return reverse_lazy('social:post-detail', kwargs={'pk':pk})

    def test_func(self):
        activate('es')  # Establece el contexto de traducción en español
        post = self.get_object()
        return self.request.user == post.author



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    activate('es')  # Establece el contexto de traducción en español
    model=SocialPost
    template_name='pages/social/delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



class AddLike(LoginRequiredMixin, View):
    activate('es')  # Establece el contexto de traducción en español
    def post(self, request, pk, *args, **kwargs):
        post = SocialPost.objects.get(pk=pk)

        is_dislike = False
        
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        
        if not is_like:
            userde = request.user
            userpara = post.author
            context = f'a {userde} le gusto tu publicacion'
            ver = post.pk
            Notification(userde, userpara, context, ver, request)
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)


        like_count = post.likes.count()

        #variable para contar dislikes
        dislike_count = post.dislikes.count()


        # Construir la respuesta en formato JSON
        response_data = {
            'liked': not is_like,
            'like_count': like_count,
            #dislike count
            'dislike_count': dislike_count,
        }

        # Devolver la respuesta JSON
        return JsonResponse(response_data)


class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = SocialPost.objects.get(pk=pk)
        activate('es')  # Establece el contexto de traducción en español

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        dislike_count = post.dislikes.count()

        #contar los likes poara retornar al javascript
        like_count = post.likes.count()



        # Construir la respuesta en formato JSON
        response_data1 = {
            'disliked': not is_dislike,
            'dislike_count': dislike_count,
            #like coun
            'like_count': like_count
        }

        # Devolver la respuesta JSON
        return JsonResponse(response_data1)



class AddCommentLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        activate('es')  # Establece el contexto de traducción en español
        comment = SocialComment.objects.get(pk=pk)
        post = comment.post

        is_dislikeCom = False
        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislikeCom = True
                break

        if is_dislikeCom:
            comment.dislikes.remove(request.user)

        is_likeCom = False
        for like in comment.likes.all():
            if like == request.user:
                is_likeCom = True
                break
        
        if not is_likeCom:
            userde = request.user##
            userpara = comment.author
            ver = post.pk
            context = f' a {userde} le gusto tu comentario: {comment.comment[:15]}...'##
            Notification(userde, userpara, context, ver, request)##
            comment.likes.add(request.user)

        if is_likeCom:
            comment.likes.remove(request.user)

        comment_dislike_count = comment.dislikes.count()

        #contar los likes poara retornar al javascript
        comment_like_count = comment.likes.count()

        
        # Construir la respuesta en formato JSON
        response_data_Com = {
            'dislike_count': comment_dislike_count,
            'like_count': comment_like_count,
            'liked': not is_likeCom,
        }
        #json_data = json.dumps(response_data_Com)
        #print(json_data)
        return JsonResponse(response_data_Com)


class AddCommentDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        activate('es')  # Establece el contexto de traducción en español
        comment = SocialComment.objects.get(pk=pk)

        is_likeCom = False
        for like in comment.likes.all():
            if like == request.user:
                is_likeCom = True
                break

        if is_likeCom:
            comment.likes.remove(request.user)

        is_dislikeCom = False
        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislikeCom = True
                break

        if not is_dislikeCom:
            comment.dislikes.add(request.user)

        if is_dislikeCom:
            comment.dislikes.remove(request.user)

        # Construir la respuesta en formato JSON
        comment_dislike_count = comment.dislikes.count()

        #contar los likes poara retornar al javascript
        comment_like_count = comment.likes.count()
        response_data_Com = {
            'dislike_count': comment_dislike_count,
            'like_count': comment_like_count,
            'disliked': not is_dislikeCom,
        }
        return JsonResponse(response_data_Com)
        

class CommentReplyView(LoginRequiredMixin, View):
    def post(self, request, post_pk, pk, *args, **kwargs):
        activate('es')  # Establece el contexto de traducción en español
        post=SocialPost.objects.get(pk=post_pk)
        parent_comment = SocialComment.objects.get(pk=pk)
        form=SocialCommentForm(request.POST)
        print(form.is_valid, "AAAAAAAAAAAAAA")
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.parent = parent_comment

            ###########################
            #notificacion al del post
            userde = request.user
            userpara = post.author
            context = f'{userde} agrego un comentario: {new_comment.comment[:15]}...'
            ver = post.pk
            Notification(userde, userpara, context, ver, request)
            #notificacion al que se responde el comentario
            userpara = parent_comment.author
            context = f'{userde} respondio tu comentario: {new_comment.comment[:15]}...'
            Notification(userde, userpara, context, ver, request)
            ###########################
            new_comment.save()

        comment = SocialComment.objects.filter(pk=new_comment.pk).order_by('-created_on')#comentario creado
        context = {
            'post': post,
            'form': form,
            'comments':comment
        }
        html = render(request, 'pages/social/comment_ajax_reply.html', context)
        #print(html) --> TENEMOS EL DOCUEMNTO HTML CORRECTAMENTE!

        comments = SocialComment.objects.filter(post=post).order_by('-created_on')
        comments_data = [{'text': comment.comment, 'author': comment.author.username} for comment in comments]
        html_content = html.content.decode('utf-8')  # Obtener el contenido HTML como una cadena
        #print(html_content) --> LITERALMENTE EL HTML QUE NECESITAMOS RESPONDER!
        print(html_content)

        response_data = {
            'comments': comments_data,
            'html_generado': html_content,
        }
        return JsonResponse(response_data)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=SocialComment
    template_name="pages/social/comment_delete.html"

    def get_success_url(self):
        activate('es')  # Establece el contexto de traducción en español
        pk = self.kwargs['post_pk']
        return reverse_lazy('social:post-detail', kwargs={'pk': pk})

    def test_func(self):
        activate('es')  # Establece el contexto de traducción en español
        post = self.get_object()
        return self.request.user == post.author


class CommentEditView(UpdateView):
    model = SocialComment
    fields = ['comment']
    template_name = 'pages/social/comment_edit.html'

    def get_success_url(self):
        activate('es')  # Establece el contexto de traducción en español
        pk = self.kwargs['post_pk']
        return reverse_lazy('social:post-detail', kwargs={'pk':pk})
    
class UserSearch(View):
    def get(self, request, *args, **kwargs):
        activate('es')  # Establece el contexto de traducción en español
        query = self.request.GET['query']
        profile_list=Profile.objects.filter(Q(user__username__icontains=query))#filtrar lso datos que escribimos
        img = timestamp()
        context={
            'profile_list':profile_list,
            'img' : img,
        }
        return render(request, 'pages/social/search.html', context)
    

class AddReport(LoginRequiredMixin, View):
    activate('es')  # Establece el contexto de traducción en español
    def post(self, request, pk, *args, **kwargs):
        post = SocialPost.objects.get(pk=pk)

        is_report = False
        for report in post.reports.all():
            if report == request.user:
                is_report = True
                break
        
        if not is_report:
            post.reports.add(request.user)

        if is_report:
            post.reports.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)









#########################################CONTROL#####################################
class ControlReports(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        posts = SocialPost.objects.all().order_by('reports')
        context = {
            'posts':posts,
        }
        return render(request, 'pages/social/revisar.html', context)

class ControlPost(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        posts = SocialPost.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'pages/social/reportes.html', context)
