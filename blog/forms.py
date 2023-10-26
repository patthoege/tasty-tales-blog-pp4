from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''  # Set an empty label for the body field
        self.fields['body'].widget = forms.Textarea(
            attrs={'placeholder': 'Leave a comment...'})
