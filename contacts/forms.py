from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    first_name = forms.CharField(label='نام', max_length=100,
                                 widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    last_name = forms.CharField(label='نام خانوادگی', max_length=100)
    user_name = forms.CharField(label='نام کاربری', min_length=3, max_length=50)
    email = forms.CharField(label='ایمیل', min_length=3, max_length=50)
    password1 = forms.CharField(label='رمز عبور', min_length=3, max_length=50,
                                widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
    password2 = forms.CharField(label='تکرار رمز عبور', min_length=3, max_length=50,
                                widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))

    # last_login = forms.CharField(label='Last login', min_length=3, max_length=50)

    def clean_user_name(self):

        user = self.cleaned_data["user_name"]
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('این نام کاربری قبلا ثبت شده است.')
        else:
            return user

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل از قبل وجود داشته است.')
        return email

    def clean_password2(self):
        if self.cleaned_data["password2"] != self.cleaned_data["password1"]:
            raise forms.ValidationError('رمز ها مطابقت ندارند.')
        elif len(self.cleaned_data["password2"]) < 8:
            raise forms.ValidationError('باید بیشتر از 8 کارکتر باشد')
        elif not any(i.isupper() for i in self.cleaned_data["password2"]):
            raise forms.ValidationError("حداقل یک حرف بزرگ باید باشد")
        elif not any(i.isdigit() for i in self.cleaned_data["password2"]):
            raise forms.ValidationError("باید شامل عدد باشد")



        # elif "@" or "_" or "-" not in self.cleaned_data["password2"]:
        #     raise forms.ValidationError("رمز عبور شما باید دارای یکی از کارکتر های @ یا _ یا -")
        else:
            return self.cleaned_data["password2"]


class UserLoginForm(forms.Form):
    user = forms.CharField(label="نام کاربری", max_length=100)
    password = forms.CharField(label="رمز عبور", max_length=100)


class ChangePasswordForm(forms.Form):
    old_pass = forms.CharField(label='رمز عبور', min_length=3, max_length=50,
                               widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور قدیمی'}))
    new_pass1 = forms.CharField(label='رمز عبور', min_length=3, max_length=50,
                                widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور1'}))
    new_pass2 = forms.CharField(label='رمز عبور', min_length=3, max_length=50,
                                widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور2'}))
