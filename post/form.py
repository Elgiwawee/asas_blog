from django import forms
from .models import Post, Image, Document
from django.utils.translation import activate, gettext_lazy as _

class CreatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Ensure form initializes first
        activate('ar')  # Set Arabic language
        
        # Apply Bootstrap classes for better styling
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'أدخل عنوان المنشور'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'rows': 5, 'placeholder': 'أدخل محتوى المنشور'})
        self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Post
        fields = ('title', 'body', 'is_published', 'image')
        labels = {
            'title': _('العنوان'),
            'body': _('المحتوى'),
            'is_published': _('منشور؟'),
            'image': _('الصورة'),       
        }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Ensure form initializes first
        activate('ar')  # Set Arabic language
        
        # Apply Bootstrap classes for better styling
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'أدخل عنوان المنشور'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'rows': 5, 'placeholder': 'أدخل محتوى المنشور'})
        self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Post
        fields = ('title', 'body', 'is_published', 'image')
        labels = {
            'title': _('العنوان'),
            'body': _('المحتوى'),
            'is_published': _('منشور؟'),
            'image': _('الصورة'),       
        }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
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

