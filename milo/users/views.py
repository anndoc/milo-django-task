from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from users.forms import UserForm


class UserListView(ListView):
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'users/user_list.html'
    paginate_by = 10


class UserDetailView(DetailView):
    model = get_user_model()


class UserCreateView(CreateView):
    model = get_user_model()
    template_name = 'users/user_create.html'
    form_class = UserForm
    success_url = reverse_lazy('users:list')


class UserUpdateView(UpdateView):
    model = get_user_model()
    form_class = UserForm
    template_name = 'users/user_create.html'
    success_url = reverse_lazy('users:list')


class UserDeleteView(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('users:list')
    http_method_names = ('post',)
