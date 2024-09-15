from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView

from trans_operator.forms import OperatorCreateForm


class OperatorListView(TemplateView):
    template_name = 'operator-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operators'] = User.objects.filter(is_staff=False)
        return context


class OperatorCreateView(TemplateView):
    template_name = 'operator-create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OperatorCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        form = OperatorCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operator-list')
        return render(request, 'operator-create.html', {'form': form})
