from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm, EditUserProfileForm

User = get_user_model()


class UserCreateView(CreateView):
    template_name = 'registration/registration_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('blog:index')


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditUserProfileForm
    template_name = 'blog/user.html'

    def get_object(self):
        return self.request.user
