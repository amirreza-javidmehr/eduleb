from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import User
import re


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["phone", "password1", "password2"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["phone", "first_name", "last_name", "email", "password", "image", "is_active", "is_admin"]


class SubmitUserForm(forms.ModelForm):
    password_confirm = forms.CharField(max_length=128)

    class Meta:
        model = User
        fields = ["phone", "password", "password_confirm"]

    def __init__(self, *args, **kwargs):
        super(SubmitUserForm,self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':'لطفا این فیلد را پر کنید.'}

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        user = User.objects.filter(phone=phone)
        if user.exists():
            raise ValidationError("این شماره موبایل قبلا ثبت شده است.", code='already_exists')
        return phone

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search(
                "[0-9]", password):
            raise ValidationError("رمزعبور باید حداقل 8 کاراکتر شامل کاراکتر خاص، عدد، حرف بزرگ و حرف کوچک باشد.",
                                  code="invalid_password")
        return password

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get('password_confirm')
        if password:
            if password != password_confirm:
                raise ValidationError("رمز عبور یکسان نیست.", code="password_mismatch")
            return password_confirm

class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginUserForm,self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':'لطفا این فیلد را پر کنید.'}

    def clean(self):
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        user = authenticate(phone=phone, password=password)
        if user is None:
            raise ValidationError("شماره موبایل یا رمز عبور وارد شده صحیح نمیباشد.")
