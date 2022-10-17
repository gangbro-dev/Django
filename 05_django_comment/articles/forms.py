from django import forms
<<<<<<< HEAD
from .models import Article
=======
from .models import Article, Comment
>>>>>>> 453aefd82c356c5398bc0fedd06718d41e3455c2


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용을 입력하세요.',
        }
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
<<<<<<< HEAD
=======


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('article',)
        fields = '__all__'
>>>>>>> 453aefd82c356c5398bc0fedd06718d41e3455c2
