from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View


from .forms import RegisterForm, LoginForm, ProfileUpdateForm


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        context = {
            'form': register_form
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        create_form = RegisterForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            form = RegisterForm()
            context = {
                'form': form
            }
            messages.error(request, "Foydalanuvchi qo'shilmadi")
            return render(request, 'users/register.html', context)


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        context = {
            'form': login_form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        user_form = AuthenticationForm(request, data=request.POST)
        if user_form.is_valid():
            user = user_form.get_user()
            login(request, user)
            return redirect('users:profile')
        else:
            form = AuthenticationForm()
            context = {
                'form': form
            }
            return render(request, 'users/login.html', context)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('landing')


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            'user': request.user
        }
        return render(request, 'users/profile.html', context)


class ProfileUpdateView(LoginRequiredMixin, View):

    def get(self, request):
        update_form = ProfileUpdateForm(instance=request.user)
        context = {
            'form': update_form
        }
        return render(request, 'users/profile_edit.html', context)

    def post(self, request):
        user_update_form = ProfileUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if user_update_form.is_valid():
            user_update_form.save()
            return redirect("users:profile")
        else:
            return render(request, 'users/profile_edit.html', {'form': user_update_form})

