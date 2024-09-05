from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from contacts.models import ContactUs
from .forms import UserRegisterForm, UserLoginForm, ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def ViewContactUs(request):
    if request.method == 'POST':
        form_register = UserRegisterForm(request.POST)
        if form_register.is_valid():
            data = form_register.cleaned_data
            User.objects.create_user(username=data["user_name"],
                                     email=data["email"],
                                     password=data["password1"])

            return redirect("forms:view-form")

    else:
        form_register = UserRegisterForm()
    return render(request, 'contacts/contactus.html', {'form_register': form_register})

    # data = request.POST
    # ContactUs.objects.create(name=data['name'], email=data['email'], last_name=data['last_name'] ,phone=data['phone_number'])

    # return render(request, 'contacts/contactus.html')


def ViewLogin(request):
    if request.method == 'POST':
        userlogin = UserLoginForm(request.POST)
        if userlogin.is_valid():
            data = userlogin.cleaned_data
            user = authenticate(request, username=data["user"], password=data["password"])
            if user is not None:
                login(request, user)
                return redirect("forms:view-form")
            # else:
            #     return redirect("contanct:contact_us")

    else:
        UserLogin = UserLoginForm()
    context = {'userlogin': UserLogin}
    return render(request, 'contacts/login_page.html', context)


def Viewlogout(request):
    logout(request)
    messages.success(request, 'همینو میخواستی؟؟ خارج شدی')
    return redirect("login")


@login_required()
def ViewChangePass(request):
    if request.method == 'POST':
        changepasswordform = ChangePasswordForm(request.POST)
        user = request.user
        if changepasswordform.is_valid():
            data = changepasswordform.cleaned_data
            old_password = data["old_pass"]
            new_password1 = data["new_pass1"]
            new_password2 = data["new_pass1"]
            if not user.check_password(old_password):
                return HttpResponse("پسووردت اشتباهه")
            elif  new_password1 != new_password2:
                return HttpResponse("پسووردا با هم برابر نیستنااا")
            else:
                user.set_password(new_password1)
                login(request, user)
                user.save()

                return redirect('contact_us')




    else:
        changepasswordform = ChangePasswordForm()
    return render(request, 'contacts/changepass.html', {'changepasswordform': changepasswordform})
