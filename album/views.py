from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.contrib.auth.models import User
form django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from .forms import UserCreateForm, UserAuthenticateForm


# Create your views here.
class RegisterView(FormView):
    template_name = 'form.html'
    form_class = UserCreateForm
    success_url = 'main'

    def form_valid(self, form):
        u = User()
        u.username = form.cleaned_data['username']
        u.first_name = form.cleaned_data['first_name']
        u.last_name = form.cleaned_data['last_name']
        u.email = form.cleaned_data['email']
        u.set_password(form.cleaned_data['password'])
        u.save()

        return super(RegisterView, self).form_valid(form)


class LoginView(View):
    def get(self, request):
        form = UserAuthenticateForm
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = UserAuthenticateForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')