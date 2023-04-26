from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, TemplateView
from .forms import UserRegisterForm, UserLoginForm, PasswordResetForm, NewPasswordForm
from django.contrib import messages, auth
from django.contrib.auth import views

from django.utils.translation import gettext_lazy as _


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'new_template/registration/register.html', context)

    def post(self, request, *args, **kwargs):
        signup_form = UserRegisterForm(request.POST)
        context = {
            'form': signup_form,
        }
        email = request.POST['email']
        password = request.POST['password1']
        if signup_form.is_valid():
            signup_form.save()
            user = auth.authenticate(
                request, username=email, password=password)
            auth.login(request, user)
            messages.success(request, _(
                "Thanks for signing up. We appriciate you"))
            return redirect('pages:home')
        else:
            errorStr = ""
            errorDict = dict(signup_form.errors)
            for i in errorDict:
                errorStr += errorDict[i]
            messages.error(request, errorStr)
            return render(request, 'new_template/registration/register.html', context)


class LoginView(views.LoginView):
    template_name = 'new_template/registration/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        else:
            return reverse('pages:home')


class PasswordReset(views.PasswordResetView):
    template_name = 'new_template/registration/password_reset.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')


class PasswordResetDone(views.PasswordResetDoneView):
    template_name = 'new_template/registration/password_reset_done.html'


class PasswordResetConfirm(views.PasswordResetConfirmView):
    template_name = 'new_template/registration/password_reset_confirm.html'
    form_class = NewPasswordForm


class PasswordResetComplete(views.PasswordResetCompleteView):
    template_name = 'new_template/registration/password_reset_complete.html'
