from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'challenge_app/home.html'
