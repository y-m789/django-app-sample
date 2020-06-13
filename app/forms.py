# 入力フォームの設定
from django import forms
from .models import Information
from django.contrib.auth.forms import AuthenticationForm


# 情報フォーム
class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ('name', 'email', 'age', 'sex', 'memo')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '記入例：山田　太郎'}),
            'email': forms.TextInput(attrs={'placeholder': '記入例：mail@mail.jp'}),
            'age': forms.NumberInput(attrs={'min': 1}),
            'sex': forms.RadioSelect(),
            'memo': forms.Textarea(attrs={'rows': 4}),
        }


# ログインフォーム
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
