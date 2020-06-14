from django.contrib.auth.mixins import LoginRequiredMixin


class NoCommunityRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_community:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
