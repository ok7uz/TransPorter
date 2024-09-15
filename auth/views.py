from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View

from auth.forms import LoginForm


class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        return context

    @staticmethod
    def post(request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)
                return redirect('transportation-list')
        return render(request,'login.html', context={'form': form})


class LogoutView(View):

    @staticmethod
    def get(request):
        logout(request)
        return redirect('login')
