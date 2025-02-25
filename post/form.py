from django import forms
from .models import Post, Image, Document
from django.utils.translation import activate, gettext_lazy as _


class CreatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Activate the desired language when the form is initialized
        activate('ar')  # Replace 'ar' with the desired language code
        super().__init__(*args, **kwargs)


    class Meta:
        model = Post
        fields = ('title', 'body', 'is_published', 'image')
        labels = {
            'title': _('Title'),
            'body': _('Body'),
            'is_published': _('Is_published?'),
            'image': _('Image'),       
        }

class UpdatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Activate the desired language when the form is initialized
        activate('ar')  # Replace 'ar' with the desired language code
        super().__init__(*args, **kwargs)


    class Meta:
        model = Post
        fields = ('title', 'body', 'is_published', 'image')
        labels = {
            'title': _('Title'),
            'body': _('Body'),
            'is_published': _('Is_published?'),
            'image': _('Image'),
        }

class ImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Activate the desired language when the form is initialized
        activate('ar')  # Replace 'ar' with the desired language code
        super().__init__(*args, **kwargs)

    class Meta:
        model = Image
        fields = ['caption', 'image',]
        label = {
            'caption' : _('Caption'),
            'image' : _('Image'),
        }


class DocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Activate the desired language when the form is initialized
        activate('ar')  # Replace 'ar' with the desired language code
        super().__init__(*args, **kwargs)

    class Meta:
        model = Document
        fields = ['title', 'document',]
        label = {
            'title' : _('Title'),
            'document' : _('Ducument'),
        }

