from django.utils.text import slugify
from .models import Comment, Post
from django import forms


class TagWidget(forms.TextInput):
    def format_value(self, value):
        if isinstance(value, list):
            return ', '.join(str(tag) for tag in value)
        return value


class NewPost(forms.ModelForm):
    save_draft = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Post
        template_name = 'add_post.html'
        fields = [
            'title', 'excerpt', 'featured_image', 
            'category', 'tags','ingredients', 'instructions',
            'preparation_time', 'cooking_time', 'portions'
        ]
        # How to use widgets with class form control
        # https://www.youtube.com/watch?v=6-XXvUENY_8&list=PLxED07G8CYrqly5rRO93Xi5HNo8kRT6GO&index=1
        # How to fix tags input in the form field 
        # https://stackoverflow.com/questions/64957025/how-to-display-just-the-tags-in-form-instead-of-all-the-list-elements-in-django
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': TagWidget(attrs={'class': 'form-control'}),
            'portions': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''
        self.fields['body'].widget = forms.Textarea(
            attrs={'placeholder': 'What do you think?', 'rows': 2})