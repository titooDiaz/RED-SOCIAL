from django.urls import path

from .views import UserProfileView, EditProfile, AddFollower, RemoveFollower, ListFollowers, EditProfileStatic


app_name="users"

urlpatterns = [
    path('<username>/', UserProfileView.as_view(), name="profile"),
    path('myprofile/edit/', EditProfile, name="edit-profile"),
    path('myprofile/edit/static/', EditProfileStatic, name="edit-profile-static"),

    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
	path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    
    path('profile/<int:pk>/followers/',ListFollowers.as_view(), name='followers-list'),

]
