from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

class RoleRequiredMixin(LoginRequiredMixin):
    redirect_field_name = 'next'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        elif not self.has_permission(request.user):
            return HttpResponseRedirect(self.get_redirect_url())
        return super().dispatch(request, *args, **kwargs)

    def has_permission(self, user):
        raise NotImplementedError("Subclasses must implement has_permission() method.")

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('Login:main_login'))
