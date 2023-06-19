from django import forms


class EmailPostForm(forms.Form):

    name = forms.CharField(max_length=25, label='Имя отправителя')
    email = forms.EmailField(label='Адрес электронной почты отправителя')
    to = forms.EmailField(label='Адрес электронной почты получателя')
    comments = forms.CharField(required=False, label='Сообщение', widget=forms.Textarea)
