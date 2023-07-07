from django import forms
from .models import SocialPost, SocialComment, NotificationSocial


class SocialPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'rounded-md bg-green-100 border p-2 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md mx-auto',
            'rows': '3',
            'placeholder': 'Nuevo texto...'
            }),
        required=True)

    image = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'relative dark:text-dark-txt dark:bg-dark-second cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500',
        'multiple': True
        }),
        required=False
        )
    
    widgets = {
            'body': forms.Textarea(attrs={'class': 'rounded-md bg-green-100 border p-2 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md mx-auto'}),
        }

    class Meta:
        model=SocialPost
        fields=['body']

class SocialCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md block',
            'rows': '1',
            'placeholder': 'Comment Something...',
            'id': 'comment-holderPrincipal'
            }),
        required=True
        )

    class Meta:
        model=SocialComment
        fields=['comment']


class NotificationSocialForm(forms.ModelForm):  
    mensaje = forms.CharField()
    ##################
    class Meta:
        model=NotificationSocial
        fields=['mensaje']
