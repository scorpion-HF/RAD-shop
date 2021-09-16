from allauth.account.forms import LoginForm, PasswordField, SignupForm, AddEmailForm,\
    ChangePasswordForm, ResetPasswordForm, SetPasswordForm, ResetPasswordKeyForm
from captcha.fields import CaptchaField
from django import forms
from .models import User


class CustomLoginForm(LoginForm):
    password = PasswordField(label="کلمه عبور", autocomplete="current-password")
    remember = forms.BooleanField(label="مرا به خاطر بسپار", required=False)
    captcha = CaptchaField(label='عبارت تصویر')
    error_messages = {
        "account_inactive":
            "این حساب کاربری در حال حاضر مسدود می باشد",
        "email_password_mismatch":
            "نام کاربری یا کلمه عبور صحیح نمی باشد",
        "username_password_mismatch":
            "نام کاربری یا کلمه عبور صحیح نمی باشد",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].label = 'آدرس ایمیل'
        self.fields['login'].widget.attrs.update({
            'class': 'form-control',
            'style': 'direction: ltr;',
            'placeholder': 'ایمیل',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'style': 'direction: ltr;',
        })
        self.fields['remember'].widget.attrs.update({
            'class': 'form-check-input float-none text-black',
        })
        self.fields['captcha'].widget.attrs.update({
            'class': 'form-control m-2',
            'style': 'direction: ltr;',
            'placeholder': 'عبارت تصویر',
        })
        self.fields['captcha'].error_messages = {
            'required': 'این فیلد الزامی است',
            'invalid': 'عدد تصویر اشتباه وارد شده است',
            'incomplete': 'مقدار کامل را وارد کنید'
        }


class CustomSignupForm(SignupForm):
    captcha = CaptchaField(label='عبارت تصویر')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'آدرس ایمیل'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'style': 'direction: ltr;',
            'placeholder': 'ایمیل',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'style': 'direction: ltr;',
            'placeholder': 'کلمه عبور',
        })
        self.fields['password1'].error_messages = {
            'required': 'این فیلد الزامی است',
        }
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'style': 'direction: ltr;',
            'placeholder': 'تکرار کلمه عبور',
        })
        self.fields['password2'].error_messages = {
            'required': 'این فیلد الزامی است',
        }
        self.fields['captcha'].widget.attrs.update({
            'class': 'form-control m-2',
            'style': 'direction: ltr;',
            'placeholder': 'عبارت تصویر',
        })


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'postal_code', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'id': 'address',
            'rows': 5,
        })
        self.fields['postal_code'].widget.attrs.update({
            'class': 'form-control',
            'id': 'postal-code',
            'style': 'direction: ltr;',
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'id': 'phone-number',
            'style': 'direction: ltr;',
        })
        self.fields["first_name"].error_messages = {
            'required': 'این فیلد الزامی است'
        }
        self.fields["last_name"].error_messages = {
            'required': 'این فیلد الزامی است'
        }
        self.fields["address"].error_messages = {
            'required': 'این فیلد الزامی است'
        }
        self.fields["postal_code"].error_messages = {
            'required': 'این فیلد الزامی است'
        }
        self.fields["phone_number"].error_messages = {
            'required': 'این فیلد الزامی است'
        }


class CustomAddEmailForm(AddEmailForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'آدرس ایمیل'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control text-black bg-wb',
            'placeholder': 'ایمیل',
            'style': 'direction: ltr;',
        })
        self.fields["email"].error_messages = {
            'required': 'این فیلد الزامی است'
        }


class CustomChangePasswordForm(ChangePasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['oldpassword'].label = 'کلمه عبور فعلی'
        self.fields['password1'].label = 'کلمه عبور جدید'
        self.fields['password2'].label = 'تکرار کلمه عبور جدید'
        self.fields['oldpassword'].widget.attrs.update({
            'class': 'form-control text-black bg-wb',
            'placeholder': 'کلمه عبور فعلی',
            'style': 'direction: ltr;',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control text-black bg-wb',
            'placeholder': 'کلمه عبور جدید',
            'style': 'direction: ltr;',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control text-black bg-wb',
            'placeholder': 'تکرار کلمه عبور جدید',
            'style': 'direction: ltr;',
        })
        self.fields["oldpassword"].error_messages = {
            'required': 'این فیلد الزامی است'
        }
        self.fields["password1"].error_messages = {
            'required': 'این فیلد الزامی است'
        }
        self.fields["password2"].error_messages = {
            'required': 'این فیلد الزامی است'
        }


class CustomResetPasswordForm(ResetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'آدرس ایمیل'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control text-black bg-wb',
            'placeholder': 'آدرس ایمیل',
            'style': 'direction: ltr;',
        })
        self.fields["email"].error_messages = {
            'required': 'این فیلد الزامی است'
        }


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'کلمه عبور جدید'
        self.fields['password2'].label = 'تکرار کلمه عبور جدید'

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control text-black bg-wb',
            'placeholder': 'کلمه عبور جدید',
            'style': 'direction: ltr;',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control text-black bg-wb',
            'placeholder': 'تکرار کلمه عبور جدید',
            'style': 'direction: ltr;',
        })
        self.fields["password1"].error_messages = {
            'required': 'این فیلد الزامی است'
        }
        self.fields["password2"].error_messages = {
            'required': 'این فیلد الزامی است'
        }


class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'کلمه عبور جدید'
        self.fields['password2'].label = 'تکرار کلمه عبور جدید'

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control text-black bg-wb',
            'placeholder': 'کلمه عبور جدید',
            'style': 'direction: ltr;',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control text-black bg-wb',
            'placeholder': 'تکرار کلمه عبور جدید',
            'style': 'direction: ltr;',
        })
        self.fields["password1"].error_messages = {
            'required': 'این فیلد الزامی است'
        }
        self.fields["password2"].error_messages = {
            'required': 'این فیلد الزامی است'
        }