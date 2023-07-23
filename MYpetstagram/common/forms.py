from django import forms
from MYpetstagram.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment_text',
        ]
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Add comment...',
            }
        )


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by pet name...'
            }
        )
    )