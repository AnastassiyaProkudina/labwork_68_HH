from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from accounts.forms import LoginForm, CustomUserCreationForm, UserChangeForm
from app.forms import CVCreationMultiForm
from app.models import CV
from app.models.cv import EducationLevelChoice


class LoginView(TemplateView):
    template_name = "login.html"
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {"form": form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            messages.error(request, "Некорректные данные")
            return redirect("index")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if not user:
            messages.warning(request, "Пользователь не найден")
            return redirect("index")
        login(request, user)
        next = request.GET.get("next")
        if next:
            return redirect(next)
        return redirect("index")


def logout_view(request):
    logout(request)
    return redirect("index")


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {"form": form}
        return self.render_to_response(context)


class AccountView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "profile.html"
    context_object_name = "user_obj"

    def get_context_data(self, **kwargs):
        kwargs["cvs"] = CV.objects.filter(author_id=self.request.user.pk).exclude(status='NOT_ACTIVE').order_by(
            '-created_at')
        kwargs["change_form"] = UserChangeForm(instance=self.request.user)
        kwargs["change_cv_form"] = CVCreationMultiForm()
        kwargs["education_level_choices"] = EducationLevelChoice.choices
        return super().get_context_data(**kwargs)


class UserUpdateView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    context_object_name = "user_obj"

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER")
