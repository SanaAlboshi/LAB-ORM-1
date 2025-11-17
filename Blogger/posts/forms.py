from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'poster', 'is_published']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter post title...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Write your story...',
                'rows': 15
            }),
            'poster': forms.ClearableFileInput(attrs={
                'class': 'form-input'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }

        labels = {
            'title': 'Post Title',
            'content': 'Content',
            'poster': 'Upload Image',
            'is_published': 'Publish immediately'
        }
