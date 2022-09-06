from unittest.util import _MAX_LENGTH
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }

        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please enter your content'
        }
    )

    class Meta:
        model = Article
        fields = '__all__'
    # NATION_A = 'kr'
    # NATION_B = 'ch'
    # NATION_C = 'jp'
    # NATION_CHOICE = [
    #     (NATION_A, '한국'),
    #     (NATION_B, '중국'),
    #     (NATION_C, '일본'),
    # ]
    # title = forms.CharField(max_length=10)
    # content = forms.CharField(widget=forms.Textarea)
    # nation = forms.ChoiceField(choices=NATION_CHOICE, widget=forms.RadioSelect)
    