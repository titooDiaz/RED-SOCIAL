from django.urls import path
from .views import (
    PostDeleteView, 
    PostDetailView, 
    PostEditView, 
    AddDislike, 
    AddLike, 
    CommentDeleteView, 
    CommentEditView, 
    CommentReplyView,
    AddCommentDislike, 
    AddCommentLike,
    UserSearch,
    #reportes
    AddReport,
    ControlReports,
    ControlPost,

    )


app_name="social"

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name="post-edit"),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name="post-delete"),

    #like dislike y comentarios!
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),

    #REPORTES
    path('post/<int:pk>/report', AddReport.as_view(), name='report'),

    #BUESQUEDA DE USUARIOS
    path('share/', UserSearch.as_view(), name='profile-search'),

    #ELIMINAR EDITAR COEMENTARIOS
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name="comment-delete"),
    path('post/<int:post_pk>/comment/edit/<int:pk>/', CommentEditView.as_view(), name="comment-edit"),

    #DAR LIKE DISLIKE A LOS COMENTARIOS
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name="comment-like"),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name="comment-dislike"),

    #RESPONDERA UN COEMNTARIO
    path('post/<int:post_pk>/comment/<int:pk>/reply',CommentReplyView.as_view(), name='comment-reply'),


    #### ADMINISTRAR
    #reportes
    path('Control/Reportes/admin', ControlReports.as_view(), name='ControlReports'),
    #aprobar
    path('Control/Post/admin', ControlPost.as_view(), name='ControlPost'),
]