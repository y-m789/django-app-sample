from .models import Information
from app.forms import LoginForm
from app.forms import InformationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.views.generic import TemplateView


# ログイン画面
class MyLoginView(LoginView):
    from_class = LoginForm
    template_name = "./login.html"


# ログアウト画面
class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "./login.html"  # ログアウトするとログイン画面へ飛ぶ


# リスト画面(top画面)
class ListView(LoginRequiredMixin, TemplateView):
    template_name = "./list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["infor"] = Information.objects.all().order_by('id')
        return context


# 詳細表示画面
class MyDetailView(LoginRequiredMixin, DetailView):
    template_name = "./detail.html"
    model = Information

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["infor"] = Information.objects.filter(id=self.kwargs['pk'])
        return context


# 登録画面
class RegisterView(LoginRequiredMixin, CreateView):
    template_name = "./register.html"
    model = Information
    form_class = InformationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RegisterView, self).form_valid(form)

    success_url = reverse_lazy('list')


# 編集画面
class EditView(LoginRequiredMixin, UpdateView):
    template_name = "./edit.html"
    model = Information
    form_class = InformationForm
    success_url = reverse_lazy('list')


# 削除画面
class MyDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "./delete.html"
    model = Information
    success_url = reverse_lazy('list')

