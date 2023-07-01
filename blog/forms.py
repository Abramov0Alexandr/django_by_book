from django import forms
from blog.models import Comment


class EmailPostForm(forms.Form):

    name = forms.CharField(max_length=25, label='Имя отправителя')
    email = forms.EmailField(label='Адрес электронной почты отправителя')
    to = forms.EmailField(label='Адрес электронной почты получателя')
    comments = forms.CharField(required=False, label='Сообщение', widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body',)


class SearchForm(forms.Form):
    query = forms.CharField(label='Ваш запрос')



