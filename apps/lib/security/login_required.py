
from django.shortcuts import redirect


class LoginRequired(object):

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated is False:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
