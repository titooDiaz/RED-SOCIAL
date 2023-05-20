from users.models import Profile
from django import forms


class EditProfileStaticForm(forms.ModelForm):
    picture = forms.ImageField(label='Profile Picture',required=False, widget=forms.FileInput)
    banner = forms.ImageField(label='Banner Picture',required=False, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ('picture', 'banner',)

class EditProfileForm(forms.ModelForm):
    # first_name = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md bg-blue-500',
    #         })
    # )
    # last_name = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
    #         })
    # )
    
    # picture = forms.ImageField(label='Profile Picture',required=True, widget=forms.FileInput)
    # banner = forms.ImageField(label='Banner Picture',required=True, widget=forms.FileInput)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=25, required=False)
    url = forms.URLField(label='Website URL', widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=60, required=False)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=260, required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=260, required=False)
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=260, required=False)
    birthday = forms.DateField(widget= forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), required=False)

    class Meta:
        model = Profile
        fields = ('location','url','bio','birthday', 'name', 'lastname')