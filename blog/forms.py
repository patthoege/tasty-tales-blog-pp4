from django.utils.text import slugify
from .models import Comment, Post, Category
from django import forms
from django.core.exceptions import ValidationError


# How to create choices for the category
# https://www.youtube.com/watch?v=_ph8GF84fX4
choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class NewCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        undesired_characters = [
            '?', '!', '#', '&', '@',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
            ]

        for char in undesired_characters:
            if char in name:
                raise ValidationError(
                    f'Invalid input: "{char}" is not allowed.'
                )

        return name


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
            'category', 'tags', 'ingredients', 'instructions',
            'preparation_time', 'cooking_time', 'portions'
        ]
        # How to use widgets with class form control
        # https://www.youtube.com/watch?v=6-XXvUENY_8&list=PLxED07G8CYrqly5rRO93Xi5HNo8kRT6GO&index=1
        # How to fix tags input in the form field
        # https://stackoverflow.com/questions/64957025/how-to-display-just-the-tags-in-form-instead-of-all-the-list-elements-in-django
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(
                choices=choices, attrs={'class': 'form-control'}
            ),
            'tags': TagWidget(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}), 
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'preparation_time': forms.TextInput(attrs={'class': 'form-control'}),
            'cooking_time': forms.TextInput(attrs={'class': 'form-control'}),
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
