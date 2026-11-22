from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


class StaffLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Your username",
            "autocomplete": "username",
        })
        form.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Your password",
            "autocomplete": "current-password",
        })
        return form

    def form_valid(self, form):
        if not form.get_user().is_staff:
            form.add_error(None, "This account does not have dashboard access.")
            return self.form_invalid(form)
        return super().form_valid(form)


class StaffLogoutView(LogoutView):
    pass
