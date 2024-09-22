from datetime import date, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import F, CharField, Value
from django.db.models.functions import Concat, Cast
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views import View
from django.views.generic import TemplateView

from transportation.forms import TransportationForm, TransportationUpdateForm, TransportationAdminUpdateForm
from transportation.models import Transportation


class TransportationView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['form'] = TransportationForm()
        if user.is_staff:
            operator = self.request.GET.get('operator', None)
            date_from = self.request.GET.get('date_from', None)
            date_to = self.request.GET.get('date_to', None)
            date_to = date.today().strftime('%Y-%m-%d') if not date_to else date_to
            date_from = (date.today() - timedelta(days=30)).strftime('%Y-%m-%d') if not date_from else date_from
            context['transportations'] = Transportation.objects.all()
            context['transportations'] = context['transportations'].filter(operator__username=operator) if operator else context['transportations']
            context['transportations'] = context['transportations'].filter(created__range=[date_from, date_to]) if date_from and date_to else context['transportations']
        else:
            context['transportations'] = Transportation.objects.filter(operator=user)
        search = self.request.GET.get('search', None)
        status = self.request.GET.get('status', None)
        context['transportations'] = context['transportations'].annotate(
            full_string=Concat(
                Cast('route', CharField()),
                Value(' '),
                Cast('cargo_owner', CharField()),
                Value(' '),
                Cast('license_plate', CharField()),
                Value(' '),
                Cast('transport_price', CharField()),
                Value(' '),
                Cast('paid_to', CharField()),
                Value(' '),
                Cast('remaining_amount', CharField()),
                Value(' '),
                Cast('business_trip', CharField()),
                Value(' '),
                Cast('additional', CharField()),
                Value(' '),
                Cast('status', CharField())
            )
        )
        context['transportations'] = context['transportations'].filter(full_string__icontains=search) if search else context['transportations']
        context['transportations'] = context['transportations'].filter(status=status) if status else context['transportations']
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
        print(request.POST)
        form = TransportationForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('transportation-list')
        return render(request, self.template_name, {'form': form})


class TransportationUpdateView(TemplateView, LoginRequiredMixin):
    template_name = 'transportation-update.html'
    login_url = 'login'

    def get(self, request, pk, *args, **kwargs):
        transportation = Transportation.objects.get(id=pk)
        context = self.get_context_data(**kwargs)
        if request.user.is_staff:
            context['form'] = TransportationAdminUpdateForm(instance=transportation)
        else:
            context['form'] = TransportationUpdateForm(instance=transportation)
        context['transportation'] = transportation
        return render(request, self.template_name, context=context)

    def post(self, request, pk, *args, **kwargs):
        transportation = Transportation.objects.get(id=pk)
        if request.user.is_staff:
            form = TransportationAdminUpdateForm(instance=transportation, data=request.POST)
        else:
            form = TransportationUpdateForm(instance=transportation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('transportation-list')
        return render(request, self.template_name, {'form': form})


class TransportationDeleteView(View, LoginRequiredMixin):

    def get(self, request, pk, *args, **kwargs):
        if request.user.is_staff:
            transportation = Transportation.objects.get(id=pk)
            transportation.delete()
        return redirect('transportation-list')