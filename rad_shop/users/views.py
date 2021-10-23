from django.views.generic import UpdateView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ProfileUpdateForm
from django.shortcuts import HttpResponseRedirect, reverse


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    login_url = reverse_lazy('account_login')
    form_class = ProfileUpdateForm

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
        else:
            return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user
