from django.shortcuts import redirect


class IsAuthenticatedMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:main')
        return super(IsAuthenticatedMixin, self).dispatch(request, *args, **kwargs)