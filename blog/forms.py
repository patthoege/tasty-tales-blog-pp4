from django.utils.text import slugify
from .models import Comment, Post
from django import forms


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        template_name = 'add_post.html'
        fields = [
            'title', 'featured_image', 'excerpt',
            'category', 'ingredients', 'instructions',
            'preparation_time', 'cooking_time', 'portions'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''  # Set an empty label for the body field
        self.fields['body'].widget = forms.Textarea(
            attrs={'placeholder': 'Leave a comment...'})
