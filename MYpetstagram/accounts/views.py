from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth import views as auth_views
from django.core.paginator import Paginator

from MYpetstagram.accounts.forms import PetstagramUserCreateForm, UserLoginForm, PetstagramUserEdirForm
from MYpetstagram.accounts.models import PetstagramUser
from MYpetstagram.pets.models import Pet


# Create your views here.
class UserRegisterView(generic.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    model = PetstagramUser
    form_class = PetstagramUserEdirForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home-page')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


@method_decorator(login_required, name='dispatch')
class UserDetailsView(generic.DetailView):
    model = PetstagramUser
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        total_likes_count = sum(p.like_set.count() for p in self.object.photo_set.all())
        photos = self.object.photo_set.all()
        paginator = Paginator(photos, 2)
        page_number = self.request.GET.get('page') or 1
        page_obj = paginator.get_page(page_number)
        pets = self.object.pet_set.all()


        context.update({
            'total_likes_count': total_likes_count,
            'is_owner': user == self.request.user,
            'paginator': paginator,
            'page_number': page_number,
            'page_obj': page_obj,
            'pets': pets,
            'user': user,

        })

        return context


class UserDeleteView(generic.DeleteView):
    model = PetstagramUser
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home-page')

    def delete(self, request, *args, **kwargs):
        self.request.user.delete()
        return redirect(self.get_success_url())
