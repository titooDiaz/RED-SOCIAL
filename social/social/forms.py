from django import forms
from .models import SocialPost, SocialComment, NotificationSocial


class SocialPostForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'rounded-md bg-white border p-2 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md mx-auto',
            'rows': '3',
            'placeholder': 'Hgosteare...'
        }),
        required=True
    )
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': ' hidden',
        'allow_multiple_selected': True,
        'id':'dropzone-file'
        }),
        required=False
        )

    class Meta:
        model = SocialPost
        fields = ['body']

class SocialCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third sm:text-sm border-gray-300 rounded-md block w-full block',
            'rows': '1',
            'placeholder': 'Hoy voy a Hgostear...',
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
