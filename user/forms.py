from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

# import datetime  # datetime.datetime.now()
# from .models import Person

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30, label = "Логин")
    password = forms.CharField(max_length = 30, widget=forms.PasswordInput , label = "Пароль")
    rememberme = forms.BooleanField(required=False)


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length = 30,
                               label = "Введите пароль",
                               widget = forms.PasswordInput)
    password2 = forms.CharField(max_length = 30,
                                label = "Введите пароль повторно",
                                widget = forms.PasswordInput)
    first_name = forms.CharField(max_length = 30, required = False, label = "Имя")
    last_name = forms.CharField(max_length = 30, required = False, label = "Фамилия")
    date_of_birth = forms.DateField(required = False, label = "Дата рождения",
                                    input_formats=['%d.%m.%Y',],
                                    widget=forms.DateInput(format = '%d.%m.%Y'),
                                    help_text = 'Введите дату в формате "дд.мм.гггг"')
    GENDER_CHOICES = (("М", "Мужской"), ("Ж", "Женский"))
    gender = forms.CharField(required = False, max_length = 1, label = "Пол", widget=forms.Select(choices = GENDER_CHOICES))
    photo = forms.ImageField(required = False, label = "Фотография")

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': _("Логин"),
            'email': _('Email')
        }
        help_texts = {
            'username': _(""),
            'email': _('Например: user@mail.com'),
        }

    def clean_username(self):
        try:
            user = User.objects.get(username = self.cleaned_data["username"])
        except User.DoesNotExist:
            return self.cleaned_data["username"]
        raise forms.ValidationError('Аккаунт с таким именем уже существует')

    def clean_email(self):
        try:
            user = User.objects.get(email = self.cleaned_data["email"])
        except User.DoesNotExist:
            return self.cleaned_data["email"]
        raise forms.ValidationError('На данный email уже заведён аккаунт')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] == cd['password2']:
            return cd["password2"]
        else:
            raise forms.ValidationError("Пароли не соответствуют друг другу")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.date_of_birth = self.cleaned_data["date_of_birth"]
        user.gender = self.cleaned_data["gender"]
        user.photo = self.cleaned_data["photo"]

        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )
        labels = {
            'first_name': _("Имя"),
            'last_name': _("Фамилия"),
            'email': _('Email'),
        }


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(required = False, label = "Дата рождения",
                                    input_formats=['%d.%m.%Y',],
                                    widget=forms.DateInput(format = '%d.%m.%Y'),
                                    help_text = 'Введите дату в формате "дд.мм.гггг"')
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'gender', 'photo', )
