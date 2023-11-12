from django.utils.text import slugify
from .models import Comment, Post
from django import forms


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        template_name = 'add_post.html'
        fields = [
            'title', 'excerpt', 'featured_image', 
            'category', 'ingredients', 'instructions',
            'preparation_time', 'cooking_time', 'portions'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'portions': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''  # Set an empty label for the body field
        self.fields['body'].widget = forms.Textarea(
            attrs={'placeholder': 'What do you think?', 'rows': 2})
