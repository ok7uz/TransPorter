from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views.generic import TemplateView

from transportation.forms import TransportationForm
from transportation.models import Transportation


class TransportationView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['form'] = TransportationForm()
        if user.is_staff:
            print(self.request, self.request.GET)
            operator = self.request.GET.get('operator', None)
            print(self.request.GET.get('operator', None))
            context['transportations'] = Transportation.objects.all()
            context['transportations'] = context['transportations'].filter(operator__username=operator) if operator else context['transportations']
            print(context['transportations'])
        else:
            context['transportations'] = Transportation.objects.filter(operator=user)
        context['operators'] = User.objects.filter(is_staff=False)
        return context


class TransportationCreateView(TemplateView, LoginRequiredMixin):
    template_name = 'create_transportation.html'
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = TransportationForm()
        print(context['form'])
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = TransportationForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('transportation-list')
        return render(request, self.template_name, {'form': form})